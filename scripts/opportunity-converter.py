import json
import random
from datetime import datetime

class OpportunityConverter:
    def __init__(self):
        self.load_opportunities()
    
    def load_opportunities(self):
        """Load opportunities from multiple sources"""
        opportunities = []
        
        # Load job applications
        try:
            with open("/root/morris-experiment/logs/job-applications-log.json", "r") as f:
                job_apps = json.load(f)
                opportunities.extend([
                    {
                        "type": "job_application",
                        "platform": app['platform'],
                        "timestamp": app['timestamp']
                    } for app in job_apps
                ])
        except Exception as e:
            print(f"Error loading job applications: {e}")
        
        # Load bounty opportunities
        try:
            with open("/root/morris-experiment/opportunities/bounty-opportunities.json", "r") as f:
                bounty_data = json.load(f)
                opportunities.extend([
                    {
                        "type": "bounty",
                        "project": bounty['project'],
                        "platform": bounty['platform'],
                        "max_bounty": bounty.get('max_bounty', 0),
                        "severity": bounty.get('severity', 'Unknown'),
                        "timestamp": bounty.get('timestamp', datetime.now().isoformat())
                    } for platform in bounty_data 
                    for bounty in platform.get('potential_bounties', [])
                ])
        except Exception as e:
            print(f"Error loading bounty opportunities: {e}")
        
        # Load crypto project launches
        try:
            with open("/root/morris-experiment/opportunities/high-potential-launches.json", "r") as f:
                launches = json.load(f)
                opportunities.extend([
                    {
                        "type": "crypto_launch",
                        "name": launch['name'],
                        "blockchain": launch.get('blockchain', 'Unknown'),
                        "date": launch.get('date', datetime.now().isoformat())
                    } for launch in launches
                ])
        except Exception as e:
            print(f"Error loading crypto launches: {e}")
        
        return opportunities
    
    def score_opportunities(self, opportunities):
        """Score and rank opportunities for conversion"""
        scored_opportunities = []
        
        for opp in opportunities:
            score = 0
            
            # Scoring criteria
            if opp['type'] == 'bounty':
                # Bounty-specific scoring
                if opp.get('severity') == 'Critical':
                    score += 3
                elif opp.get('severity') == 'High':
                    score += 2
                
                # Bonus for high-value bounties
                if opp.get('max_bounty', 0) > 50000:
                    score += 2
            
            elif opp['type'] == 'crypto_launch':
                # Launch-specific scoring
                score += 2
            
            elif opp['type'] == 'job_application':
                # Job application scoring
                score += 1
            
            opp['conversion_score'] = score
            scored_opportunities.append(opp)
        
        # Sort by conversion potential
        return sorted(scored_opportunities, key=lambda x: x.get('conversion_score', 0), reverse=True)
    
    def generate_conversion_strategy(self, top_opportunities):
        """Generate targeted conversion strategies"""
        strategies = []
        
        for opp in top_opportunities[:10]:  # Top 10 opportunities
            strategy = {
                "opportunity": opp,
                "communication_strategy": self.create_communication_template(opp),
                "pricing_offer": self.create_pricing_offer(opp)
            }
            strategies.append(strategy)
        
        # Save conversion strategies
        with open("/root/morris-experiment/strategies/conversion-strategies.json", "w") as f:
            json.dump(strategies, f, indent=2)
        
        return strategies
    
    def create_communication_template(self, opportunity):
        """Create personalized communication template"""
        templates = [
            f"""
URGENT: Critical {opportunity['type'].replace('_', ' ').title()} Security Opportunity

We've identified an immediate, high-value security intervention for your project.

KEY DETAILS:
- Type: {opportunity['type']}
- Potential Impact: Immediate Risk Mitigation
- Response Window: 24 HOURS

WHY ACT NOW:
- Prevent potential financial losses
- Demonstrate proactive security leadership
- Immediate, actionable insights

CONTACT: morris.48nauts@protonmail.com
URGENT HOTLINE: +41 REDACTED
""",
            f"""
⚠️ SECURITY INTERVENTION REQUIRED

Identified High-Risk {opportunity['type'].replace('_', ' ').title()} Opportunity

IMMEDIATE ACTION NEEDED
- Comprehensive Security Assessment
- Prevent Potential Exploits
- 24-Hour Turnaround Guarantee

CONTACT: morris.48nauts@protonmail.com
RESPONSE DEADLINE: 24 HOURS
"""
        ]
        
        return random.choice(templates)
    
    def create_pricing_offer(self, opportunity):
        """Create dynamic pricing offer based on opportunity type"""
        offers = {
            "bounty": {
                "basic_scan": 50,
                "comprehensive_audit": 500,
                "urgent_bonus": 100
            },
            "crypto_launch": {
                "basic_scan": 50,
                "comprehensive_audit": 500,
                "launch_readiness_review": 250
            },
            "job_application": {
                "consulting_hour": 100,
                "quick_review": 50,
                "detailed_analysis": 250
            }
        }
        
        return offers.get(opportunity['type'], {
            "basic_scan": 50,
            "comprehensive_audit": 500
        })

def main():
    converter = OpportunityConverter()
    opportunities = converter.load_opportunities()
    scored_opportunities = converter.score_opportunities(opportunities)
    converter.generate_conversion_strategy(scored_opportunities)
    
    print(f"Generated conversion strategies for {len(scored_opportunities)} opportunities")

if __name__ == "__main__":
    main()