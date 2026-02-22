import praw
import json
from datetime import datetime, timedelta

# Reddit API Configuration
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='morris-opportunity-scout/1.0'
)

# Target Subreddits
SUBREDDITS = [
    'forhire',
    'slavelabour',
    'cryptocurrencyjobs',
    'cryptotech',
    'blockchain',
    'ethdev',
    'defi'
]

def scout_opportunities():
    opportunities = []
    
    for subreddit_name in SUBREDDITS:
        subreddit = reddit.subreddit(subreddit_name)
        
        # Search recent posts in last 24 hours
        recent_posts = subreddit.search(
            f'(hiring OR "need help" OR freelance) AND (crypto OR blockchain OR "smart contract")',
            time_filter='day',
            sort='new'
        )
        
        for post in recent_posts:
            opportunity = {
                'title': post.title,
                'url': post.url,
                'subreddit': subreddit_name,
                'timestamp': datetime.fromtimestamp(post.created_utc).isoformat(),
                'keywords': ['crypto', 'blockchain', 'smart contract']
            }
            opportunities.append(opportunity)
    
    return opportunities

def main():
    opportunities = scout_opportunities()
    
    # Save to JSON for tracking
    with open('/root/morris-experiment/opportunities/reddit-opportunities.json', 'w') as f:
        json.dump(opportunities, f, indent=2)
    
    print(f"Found {len(opportunities)} potential opportunities")

if __name__ == '__main__':
    main()