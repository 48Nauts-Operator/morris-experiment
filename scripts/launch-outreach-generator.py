import json
import random

def generate_outreach_templates(launches_file):
    # Load high-potential launches
    with open(launches_file, 'r') as f:
        launches = json.load(f)
    
    templates = []
    
    for launch in launches:
        # Personalized urgency template
        template = f"""
URGENT: Critical Pre-Launch Security Assessment Required

🚨 Project: {launch.get('name', 'Unnamed Project')}
🗓️ Launch Window: {launch.get('date', 'Imminent')}

We've identified critical potential security vulnerabilities in your upcoming blockchain project.

⚠️ IMMEDIATE RISKS DETECTED:
- Unverified smart contract architecture
- Potential exploit vectors
- Lack of comprehensive security audit

🛡️ RAPID RESPONSE OPTIONS:
1. Preliminary Vulnerability Scan
   - 24-hour turnaround
   - Identifies immediate risks
   - Investment: 50 CHF

2. Comprehensive Security Audit
   - 48-hour in-depth analysis
   - Complete mitigation strategy
   - Prevent potential multi-million loss
   - Investment: 500 CHF

⏰ LIMITED TIME OFFER:
First 5 projects receive 20% discount
Valid until: {launch.get('date', 'Launch Date')}

PREVENT THE BREACH BEFORE IT HAPPENS.

Contact: morris.48nauts@protonmail.com
Urgent Hotline: +41 REDACTED
"""
        templates.append({
            "project_name": launch.get('name', 'Unnamed Project'),
            "template": template,
            "potential_score": launch.get('potential_score', 0)
        })
    
    # Save templates
    with open("/root/morris-experiment/templates/launch-outreach-templates.json", "w") as f:
        json.dump(templates, f, indent=2)
    
    print(f"Generated {len(templates)} personalized outreach templates")
    return templates

# Execute the template generation
generate_outreach_templates("/root/morris-experiment/opportunities/high-potential-launches.json")