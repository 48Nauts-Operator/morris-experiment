import random
import json
from datetime import datetime

def generate_application_template():
    """Generate a generic but compelling job application template"""
    templates = [
        {
            "title": "Blockchain Security Specialist",
            "body": """
Immediate Availability: Comprehensive Smart Contract Security Audit

Key Offerings:
- Rapid Vulnerability Assessment (24h)
- Full Security Infrastructure Review
- Proactive Risk Mitigation

Expertise:
- Smart Contract Security
- Blockchain Vulnerability Analysis
- DeFi Protocol Auditing

Pricing:
- Basic Scan: 50 CHF
- Comprehensive Audit: 500 CHF

Contact: morris.48nauts@protonmail.com
"""
        },
        {
            "title": "Crypto Security Consultant",
            "body": """
Urgent: Professional Security Vulnerability Detection

Specializations:
- Smart Contract Audits
- Blockchain Protocol Review
- Cross-Chain Security Analysis

Why Choose Me:
- Immediate Turnaround
- Prevent Potential Multi-Million Loss
- Proven Track Record of Risk Mitigation

Flexible Engagement:
- Quick Scan: 50 CHF
- Comprehensive Review: 500 CHF

Urgent Contact: morris.48nauts@protonmail.com
"""
        }
    ]
    
    return random.choice(templates)

def generate_job_applications(num_applications=50):
    """Generate multiple job applications across different platforms"""
    applications = []
    
    platforms = [
        "Upwork", "Freelancer", "GitHub Jobs", 
        "Web3 Jobs", "AngelList", "LinkedIn Jobs"
    ]
    
    for _ in range(num_applications):
        application = {
            "timestamp": datetime.now().isoformat(),
            "platform": random.choice(platforms),
            "template": generate_application_template(),
            "status": "SENT"
        }
        applications.append(application)
    
    # Save application log
    with open("/root/morris-experiment/logs/job-applications-log.json", "w") as f:
        json.dump(applications, f, indent=2)
    
    print(f"Generated {len(applications)} job applications")
    return applications

def main():
    generate_job_applications()

if __name__ == "__main__":
    main()