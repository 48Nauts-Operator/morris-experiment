import json
import re

def analyze_crypto_projects():
    # Load discovered projects
    with open("/root/morris-experiment/opportunities/crypto-projects-2026-02-22.json", "r") as f:
        projects = json.load(f)
    
    high_potential_projects = []
    
    for project in projects:
        potential_score = 0
        
        # Scoring criteria
        if project.get('type') in ['ICO', 'DeFi Protocol', 'Upcoming Token']:
            potential_score += 3
        
        if 'total_value_locked' in project and project['total_value_locked'] > 1000000:
            potential_score += 2
        
        if 'name' in project:
            # Look for red flag keywords in name
            risk_keywords = ['swap', 'pump', 'farm', 'yield', 'defi']
            for keyword in risk_keywords:
                if keyword in project['name'].lower():
                    potential_score += 1
        
        # High-potential threshold
        if potential_score >= 3:
            high_potential_projects.append({
                "name": project.get('name', 'Unknown'),
                "type": project.get('type', 'Unknown'),
                "potential_score": potential_score,
                "audit_offer": {
                    "basic_scan": 50,
                    "comprehensive_audit": 500
                }
            })
    
    # Save high-potential projects
    with open("/root/morris-experiment/opportunities/high-potential-projects.json", "w") as f:
        json.dump(high_potential_projects, f, indent=2)
    
    print(f"Identified {len(high_potential_projects)} high-potential projects for security audit")
    return high_potential_projects

analyze_crypto_projects()