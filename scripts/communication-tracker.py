import json
from datetime import datetime, timedelta

class CommunicationTracker:
    def __init__(self):
        self.communication_log_path = "/root/morris-experiment/logs/communication-log.json"
    
    def log_outreach(self, project, channel, message):
        """Log an outreach attempt"""
        try:
            # Load existing log
            try:
                with open(self.communication_log_path, 'r') as f:
                    log = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                log = {"outreach": [], "responses": []}
            
            # Add new outreach entry
            outreach_entry = {
                "timestamp": datetime.now().isoformat(),
                "project": project,
                "channel": channel,
                "message": message,
                "status": "SENT",
                "follow_up_by": (datetime.now() + timedelta(days=1)).isoformat()
            }
            
            log["outreach"].append(outreach_entry)
            
            # Save updated log
            with open(self.communication_log_path, 'w') as f:
                json.dump(log, f, indent=2)
            
            print(f"Logged outreach to {project} via {channel}")
            return outreach_entry
        
        except Exception as e:
            print(f"Error logging outreach: {e}")
    
    def check_pending_followups(self):
        """Check and report on pending follow-ups"""
        try:
            with open(self.communication_log_path, 'r') as f:
                log = json.load(f)
            
            now = datetime.now()
            pending_followups = [
                entry for entry in log.get("outreach", [])
                if datetime.fromisoformat(entry['follow_up_by']) <= now and 
                entry.get('status') == 'SENT'
            ]
            
            print("Pending Follow-ups:")
            for followup in pending_followups:
                print(f"Project: {followup['project']} | Channel: {followup['channel']}")
            
            return pending_followups
        
        except Exception as e:
            print(f"Error checking follow-ups: {e}")
            return []

def main():
    tracker = CommunicationTracker()
    
    # Example outreach logging
    tracker.log_outreach(
        project="SmallDEX Protocol", 
        channel="GitHub", 
        message="Quick security audit offer for your DeFi platform"
    )
    
    # Check pending follow-ups
    tracker.check_pending_followups()

if __name__ == "__main__":
    main()