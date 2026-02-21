#!/usr/bin/env python3
"""
Ethereum Gas Price Estimator & Calculator
Quick tool to help users estimate transaction costs

Sellable for 20-30 CHF as standalone utility
"""

import requests
import json
from datetime import datetime

def get_eth_price():
    """Get current ETH price in USD"""
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd,chf')
        data = response.json()
        return data['ethereum']['usd'], data['ethereum']['chf']
    except:
        return 2500, 2250  # Fallback estimates

def get_gas_prices():
    """Get current gas prices from Etherscan"""
    # Free API, no key needed for basic usage
    try:
        response = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle')
        data = response.json()
        if data['status'] == '1':
            return {
                'safe': int(data['result']['SafeGasPrice']),
                'standard': int(data['result']['ProposeGasPrice']),
                'fast': int(data['result']['FastGasPrice'])
            }
    except:
        pass
    
    # Fallback estimates
    return {'safe': 10, 'standard': 15, 'fast': 25}

def estimate_transaction_cost(gas_limit, gas_price_gwei):
    """Calculate transaction cost in ETH"""
    gas_price_eth = gas_price_gwei * 1e-9
    cost_eth = gas_limit * gas_price_eth
    return cost_eth

def main():
    print("=" * 60)
    print("   ETHEREUM GAS ESTIMATOR")
    print("=" * 60)
    print()
    
    # Get current prices
    eth_usd, eth_chf = get_eth_price()
    gas_prices = get_gas_prices()
    
    print(f"Current ETH Price: ${eth_usd:.2f} USD / {eth_chf:.2f} CHF")
    print()
    print("Current Gas Prices (Gwei):")
    print(f"  Safe:     {gas_prices['safe']} Gwei")
    print(f"  Standard: {gas_prices['standard']} Gwei")
    print(f"  Fast:     {gas_prices['fast']} Gwei")
    print()
    
    # Common transaction types
    transactions = {
        'Simple ETH Transfer': 21000,
        'ERC-20 Transfer': 65000,
        'Uniswap Swap': 150000,
        'NFT Mint': 100000,
        'Contract Deployment': 500000
    }
    
    print("Estimated Transaction Costs:")
    print("-" * 60)
    
    for tx_type, gas_limit in transactions.items():
        print(f"\n{tx_type} ({gas_limit:,} gas):")
        
        for speed, gwei in gas_prices.items():
            cost_eth = estimate_transaction_cost(gas_limit, gwei)
            cost_usd = cost_eth * eth_usd
            cost_chf = cost_eth * eth_chf
            
            print(f"  {speed.capitalize():8} | {cost_eth:.6f} ETH | ${cost_usd:.2f} | {cost_chf:.2f} CHF")
    
    print()
    print("=" * 60)
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)

if __name__ == "__main__":
    main()
