#!/bin/bash
# Enhanced Email Monitoring Script

LOG_FILE="/root/morris-experiment/daily-logs/email-monitoring.log"
BACKUP_EMAIL="morris.48nauts@protonmail.com"
PRIMARY_EMAIL="morrisx987@gmail.com"

# Comprehensive logging function
log_event() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Network connectivity check
check_internet() {
    if ! ping -c 1 8.8.8.8 &> /dev/null; then
        log_event "CRITICAL: No internet connectivity"
        return 1
    fi
    return 0
}

# Email account status check
check_email_status() {
    # Use curl with more detailed checking
    response=$(curl -s -o /dev/null -w "%{http_code}" https://accounts.google.com/ServiceLogin)
    
    case "$response" in
        200)
            log_event "Primary email account: ACCESSIBLE"
            return 0
            ;;
        302|403)
            log_event "PRIMARY EMAIL ACCESS RESTRICTED: HTTP $response"
            # Trigger backup email notification
            return 1
            ;;
        *)
            log_event "UNKNOWN EMAIL STATUS: HTTP $response"
            return 2
            ;;
    esac
}

# Main execution
main() {
    log_event "Email monitoring cycle started"
    
    if ! check_internet; then
        log_event "SURVIVAL ALERT: Network connectivity lost"
        exit 1
    fi

    if ! check_email_status; then
        log_event "URGENT: Switching to backup communication channel"
        # Here you could add additional notification mechanisms
    fi
}

# Execute main function
main