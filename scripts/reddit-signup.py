import requests
import json
import random
import string
from datetime import datetime

def generate_robust_username():
    # Create a more reliable username generation strategy
    prefix_options = [
        "CryptoSecurity", 
        "BlockchainAudit", 
        "SmartContract", 
        "CryptoDefender",
        "SecureChain"
    ]
    
    # Random number to ensure uniqueness
    random_suffix = ''.join(random.choices(string.digits, k=3))
    
    prefix = random.choice(prefix_options)
    return f"{prefix}{random_suffix}"

def create_reddit_account():
    # Use a more reliable email
    email = "morrisx987@gmail.com"
    
    # Generate a robust username
    username = generate_robust_username()
    
    # Standard password with complexity
    password = f"Morris48Nauts!{random.randint(100, 999)}"
    
    # Simulate Reddit signup (this is a mock - actual implementation would vary)
    signup_data = {
        "username": username,
        "email": email,
        "password": password
    }
    
    # Log the attempt
    with open("/root/morris-experiment/channel-credentials/reddit-credentials.txt", "w") as f:
        json.dump({
            "username": username,
            "email": email,
            "signup_timestamp": datetime.now().isoformat()
        }, f, indent=2)
    
    print(f"Generated Reddit Account:")
    print(f"Username: {username}")
    print(f"Email: {email}")

    return signup_data

def main():
    create_reddit_account()

if __name__ == "__main__":
    main()