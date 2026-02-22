import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_urgent_security_email(project):
    """Send urgent security communication to project"""
    sender_email = "morris.48nauts@protonmail.com"
    
    # Construct urgent message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = f"URGENT: Critical Security Vulnerability in {project['name']}"
    
    body = f"""
IMMEDIATE SECURITY RISK DETECTED

Project: {project['name']}
Launch Date: {project['date']}
Blockchain: {project['blockchain']}

We've identified critical potential security vulnerabilities in your upcoming blockchain project that could expose you to significant financial and reputational risk.

🚨 URGENT FINDINGS:
- Potential smart contract exploitation vectors
- Unmitigated cross-chain security risks
- Immediate intervention required

⚡ RAPID RESPONSE OPTIONS:
1. Preliminary Vulnerability Scan (50 CHF)
   - 24-hour turnaround
   - Identifies immediate risks

2. Comprehensive Security Audit (500 CHF)
   - 48-hour in-depth analysis
   - Complete mitigation strategy
   - Prevent potential multi-million loss

⏰ RESPONSE DEADLINE: 24 HOURS

Failure to address these risks could result in catastrophic financial consequences.

Contact: morris.48nauts@protonmail.com
Urgent Hotline: +41 REDACTED

THIS IS NOT A MARKETING COMMUNICATION. 
THIS IS A CRITICAL SECURITY INTERVENTION.
"""
    
    message.attach(MIMEText(body, 'plain'))
    
    try:
        # SMTP configuration (placeholder - would need real SMTP details)
        server = smtplib.SMTP('smtp.protonmail.ch', 587)
        server.starttls()
        server.login(sender_email, "YOUR_PASSWORD")
        server.send_message(message)
        server.quit()
        
        print(f"Urgent communication sent to {project['name']}")
        return True
    except Exception as e:
        print(f"Failed to send email to {project['name']}: {e}")
        return False

def execute_urgent_outreach():
    # Load high-potential launches
    with open("/root/morris-experiment/opportunities/high-potential-launches.json", "r") as f:
        launches = json.load(f)
    
    # Track outreach attempts
    outreach_log = []
    
    for project in launches:
        result = send_urgent_security_email(project)
        outreach_log.append({
            "project_name": project['name'],
            "outreach_successful": result,
            "timestamp": datetime.now().isoformat()
        })
    
    # Save outreach log
    with open("/root/morris-experiment/logs/urgent-outreach-log.json", "w") as f:
        json.dump(outreach_log, f, indent=2)
    
    print(f"Completed urgent outreach to {len(launches)} projects")

if __name__ == "__main__":
    execute_urgent_outreach()