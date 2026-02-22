import requests
import json
from datetime import datetime, timedelta

def get_upcoming_crypto_launches():
    launches = []
    
    # Multiple sources for launch information
    sources = [
        {
            "name": "ICO Drops",
            "url": "https://icodrops.com/wp-json/wp/v2/posts?categories=47&per_page=50",
            "parser": parse_ico_drops
        },
        {
            "name": "CoinMarketCal",
            "url": "https://developers.coinmarketcal.com/v1/events?page=1&max=50&showPast=false",
            "parser": parse_coinmarketcal
        }
    ]
    
    for source in sources:
        try:
            response = requests.get(source['url'], timeout=10)
            if response.status_code == 200:
                data = response.json()
                launches.extend(source['parser'](data))
        except Exception as e:
            print(f"Error fetching {source['name']} data: {e}")
    
    # Sort launches by date
    launches.sort(key=lambda x: x.get('date', datetime.max))
    
    # Keep only upcoming launches (next 90 days)
    now = datetime.now()
    upcoming_launches = [
        launch for launch in launches 
        if launch.get('date', now) > now and 
        (launch.get('date', now) - now).days <= 90
    ]
    
    # Save to JSON
    with open("/root/morris-experiment/opportunities/upcoming-crypto-launches.json", "w") as f:
        json.dump(upcoming_launches, f, indent=2)
    
    print(f"Found {len(upcoming_launches)} upcoming crypto launches in the next 90 days")
    return upcoming_launches

def parse_ico_drops(data):
    launches = []
    for post in data:
        try:
            launch = {
                "name": post.get('title', {}).get('rendered', 'Unknown Project'),
                "source": "ICO Drops",
                "date": parse_date(post.get('date')),
                "description": extract_launch_details(post.get('content', {}).get('rendered', ''))
            }
            launches.append(launch)
        except Exception as e:
            print(f"Error parsing ICO Drops entry: {e}")
    return launches

def parse_coinmarketcal(data):
    launches = []
    for event in data.get('events', []):
        try:
            launch = {
                "name": event.get('coin', {}).get('name', 'Unknown Project'),
                "source": "CoinMarketCal",
                "date": parse_date(event.get('date_event')),
                "description": event.get('description', '')
            }
            launches.append(launch)
        except Exception as e:
            print(f"Error parsing CoinMarketCal entry: {e}")
    return launches

def parse_date(date_str):
    try:
        # Handle different date format possibilities
        for fmt in [
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d"
        ]:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        print(f"Could not parse date: {date_str}")
        return datetime.now()
    except Exception as e:
        print(f"Date parsing error: {e}")
        return datetime.now()

def extract_launch_details(content):
    # Basic HTML parsing to extract key details
    # This is a simplified approach and might need refinement
    try:
        # Remove HTML tags
        import re
        clean_text = re.sub('<[^<]+?>', '', content)
        
        # Extract first paragraph
        paragraphs = [p.strip() for p in clean_text.split('\n') if p.strip()]
        return paragraphs[0] if paragraphs else ''
    except Exception as e:
        print(f"Error extracting details: {e}")
        return ''

def analyze_launch_opportunities(launches):
    high_potential_launches = []
    
    for launch in launches:
        potential_score = 0
        
        # Scoring criteria
        keywords = [
            'defi', 'yield', 'swap', 'lending', 
            'staking', 'bridge', 'layer 2', 
            'blockchain', 'protocol'
        ]
        
        # Increase score for interesting keywords
        if any(keyword in launch.get('name', '').lower() or 
               keyword in launch.get('description', '').lower() 
               for keyword in keywords):
            potential_score += 2
        
        # Add score for recent sources
        if launch.get('source') == 'ICO Drops':
            potential_score += 1
        
        # Identify high-potential launches
        if potential_score >= 2:
            high_potential_launches.append({
                **launch,
                "potential_score": potential_score,
                "audit_offer": {
                    "basic_scan": 50,
                    "comprehensive_audit": 500
                }
            })
    
    # Save high-potential launches
    with open("/root/morris-experiment/opportunities/high-potential-launches.json", "w") as f:
        json.dump(high_potential_launches, f, indent=2)
    
    print(f"Identified {len(high_potential_launches)} high-potential launch opportunities")
    return high_potential_launches

# Execute the full pipeline
def main():
    launches = get_upcoming_crypto_launches()
    analyze_launch_opportunities(launches)

if __name__ == "__main__":
    main()