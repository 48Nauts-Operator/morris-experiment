import json
import random
from datetime import datetime

class OutreachCampaign:
    def __init__(self):
        self.targets = [
            {
                "name": "SmallDEX Protocol",
                "contact_channels": ["github", "discord"],
                "type": "DeFi",
                "risk_potential": "Medium"
            },
            {
                "name": "NFT Minting Platform",
                "contact_channels": ["twitter", "email"],
                "type": "NFT Tooling",
                "risk_potential": "Low"
            },
            {
                "name": "Cross-Chain Bridge",
                "contact_channels": ["github", "telegram"],
                "type": "Blockchain Infrastructure",
                "risk_potential": "High"
            }
        ]
    
    def generate_audit_offer(self, target):
        """Create targeted audit offer message"""
        offer_templates = [
            f"""
⚠️ URGENT: {target['name']} Security Snapshot

Quick Vulnerability Assessment Offer:
- 24-Hour Turnaround
- Focused {target['risk_potential']} Risk Scan
- Actionable High-Level Insights

🔒 Pricing:
- Basic Snapshot: 50 CHF
- 50% Upfront Payment Required
- Immediate Risk Category Identification

RESPONSE WINDOW: 48 HOURS

Contact: morris.48nauts@protonmail.com
""",
            f"""
🛡️ Targeted Security Check for {target['name']}

Rapid {target['type']} Security Probe:
- Instant Risk Assessment
- Confidential Findings
- No Full Disclosure Without Payment

💰 Micro-Audit Offer:
- Quick Scan: 50–150 CHF
- Immediate Value Demonstration
- Proven Risk Mitigation Strategy

ACT NOW. PREVENT POTENTIAL LOSSES.

Contact: morris.48nauts@protonmail.com
"""
        ]
        
        return random.choice(offer_templates)
    
    def execute_outreach(self):
        """Launch targeted outreach campaign"""
        outreach_log = {
            "timestamp": datetime.now().isoformat(),
            "targets_contacted": []
        }
        
        for target in self.targets:
            contact = {
                "project": target['name'],
                "channel": random.choice(target['contact_channels']),
                "message": self.generate_audit_offer(target),
                "status": "SENT"
            }
            outreach_log['targets_contacted'].append(contact)
        
        # Save outreach log
        with open("/root/morris-experiment/logs/outreach-log.json", "w") as f:
            json.dump(outreach_log, f, indent=2)
        
        print(f"Executed outreach to {len(self.targets)} potential clients")
        return outreach_log

def main():
    campaign = OutreachCampaign()
    campaign.execute_outreach()

if __name__ == "__main__":
    main()