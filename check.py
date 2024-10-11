import subprocess
import time
import requests
import json
import os
import re

# Set your VirusTotal API key
VT_API_KEY = "your_virustotal_api_key"

# Define how often to check DNS cache (in seconds)
CHECK_INTERVAL = 600  # 10 minutes

# VirusTotal API URL
VT_API_URL = "https://www.virustotal.com/vtapi/v2/ip-address/report"

# Log file to store detected malicious IPs
LOG_FILE = "malicious_ips_log.txt"

# Function to get DNS cache using ipconfig command on Windows
def get_dns_cache():
    try:
        # Run ipconfig command and capture the output
        result = subprocess.run(["ipconfig", "/displaydns"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error retrieving DNS cache: {e}")
        return ""

# Function to extract IP addresses from DNS cache output
def extract_ips(dns_cache_output):
    ip_addresses = set()
    lines = dns_cache_output.splitlines()
    
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    

    # Check each line for IP-like patterns (simple regex for IPv4)
    for line in lines:
        line = line.strip()
        if ip_pattern.search(line):  # Check if line contains an IP address
            ip = ip_pattern.search(line).group(0)  # Extract the first found IP address
            ip_addresses.add(ip)
            print(f"Found IP: {ip}")  # Print the found IP address
            
    
    return ip_addresses
    
    

# Function to check if an IP is malicious using VirusTotal API
def check_ip_virustotal(ip):
    params = {"apikey": VT_API_KEY, "ip": ip}
    try:
        response = requests.get(VT_API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error querying VirusTotal API for IP {ip}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error querying VirusTotal for IP {ip}: {e}")
        return None

# Function to store malicious IPs in a log file
def log_malicious_ip(ip, report):
    with open(LOG_FILE, "a") as log:
        log.write(f"Malicious IP: {ip}\n")
        log.write(json.dumps(report, indent=4))
        log.write("\n" + "="*40 + "\n")

# Function to send an alert (print/log)
def send_alert(ip, report):
    print(f"ALERT! Malicious IP found: {ip}")
    log_malicious_ip(ip, report)

# Main function to monitor DNS cache periodically
def monitor_dns_cache():
    print("Starting DNS cache monitoring...")
    
    while True:
        # Step 1: Collect DNS cache
        dns_cache_output = get_dns_cache()
        if not dns_cache_output:
            print("No DNS cache found. Skipping this check.")
            time.sleep(CHECK_INTERVAL)
            continue

        # Step 2: Extract IP addresses from cache
        ip_addresses = extract_ips(dns_cache_output)
        if not ip_addresses:
            print("No IP addresses found in DNS cache. Skipping this check.")
            time.sleep(CHECK_INTERVAL)
            continue

        print(f"Checking {len(ip_addresses)} IP addresses from DNS cache...")

        # Step 3: Check each IP with VirusTotal API
        for ip in ip_addresses:
            report = check_ip_virustotal(ip)
            if report and report.get("response_code") == 1:
                if report.get("positives", 0) > 0:  # If VirusTotal detects it as malicious
                    send_alert(ip, report)

        # Wait for the next check interval
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_dns_cache()
