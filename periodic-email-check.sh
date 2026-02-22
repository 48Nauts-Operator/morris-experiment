#!/bin/bash
# Periodic Email Check Script for Morris

LOG_FILE="/root/morris-experiment/daily-logs/email-monitoring.log"
EMAIL="morrisx987@gmail.com"

# Improved logging
echo "Email check initiated at $(date)" >> "$LOG_FILE"

# Check if necessary tools are installed
if ! command -v curl &> /dev/null; then
    echo "Error: curl not installed" >> "$LOG_FILE"
    exit 1
fi

# Simple email status check (replace with proper IMAP/POP3 checking later)
email_status=$(curl -s -o /dev/null -w "%{http_code}" https://accounts.google.com/ServiceLogin)

if [ "$email_status" -eq 200 ]; then
    echo "Email account accessible at $(date)" >> "$LOG_FILE"
else
    echo "Email account access issue: HTTP $email_status" >> "$LOG_FILE"
fi