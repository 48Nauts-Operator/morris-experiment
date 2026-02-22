import requests
import json
from datetime import datetime, timedelta

def scan_crypto_projects():
    projects = []
    
    # Sources for project discovery
    sources = [
        # Upcoming ICO and Token Launch Platforms
        {"url": "https://icodrops.com/api/upcoming-icos", "type": "upcoming_ico"},
        {"url": "https://icobench.com/api/v1/icos", "type": "token_launch"},
        
        # Established Blockchain Projects
        {"url": "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1", "type": "established_project"},
        
        # New DeFi Protocols
        {"url": "https://api.defillama.com/api/new-protocols", "type": "defi_protocol"}
    ]
    
    for source in sources:
        try:
            response = requests.get(source['url'], timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                # Process different API responses
                if source['type'] == 'upcoming_ico':
                    for project in data.get('icos', []):
                        projects.append({
                            "name": project.get('name', ''),
                            "type": "ICO",
                            "launch_date": project.get('start_date', ''),
                            "description": project.get('description', ''),
                            "website": project.get('website', '')
                        })
                
                elif source['type'] == 'established_project':
                    for project in data:
                        if project.get('market_cap', 0) > 10000000:  # Filter for substantial projects
                            projects.append({
                                "name": project.get('name', ''),
                                "symbol": project.get('symbol', ''),
                                "type": "Established Crypto",
                                "market_cap": project.get('market_cap', 0),
                                "current_price": project.get('current_price', 0)
                            })
                
                elif source['type'] == 'defi_protocol':
                    for protocol in data.get('protocols', []):
                        projects.append({
                            "name": protocol.get('name', ''),
                            "type": "DeFi Protocol",
                            "total_value_locked": protocol.get('tvl', 0),
                            "blockchain": protocol.get('blockchain', '')
                        })
        
        except Exception as e:
            print(f"Error scanning {source['url']}: {e}")
    
    # Save to JSON for further analysis
    with open("/root/morris-experiment/opportunities/crypto-projects-2026-02-22.json", "w") as f:
        json.dump(projects, f, indent=2)
    
    print(f"Discovered {len(projects)} potential crypto projects")
    return projects

# Execute the scan
scan_crypto_projects()