import subprocess
import sys
import sys
import os
from termcolor import colored

def display_dns(domains):

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file_path = os.path.join(downloads_folder, "missingdnsdomains.txt")
    
    with open(output_file_path, "w") as file:
        for domain in domains:
            print(f"Checking {domain}...")
            try:
                result = subprocess.run(['whois', domain], capture_output=True, text=True)
                output = result.stdout
                
                name_servers = [line.split(":")[1].strip() for line in output.splitlines() if "Name Server:" in line]
                
                if name_servers:
                    for ns in name_servers:
                        print(ns)
                else:
                    print(colored(f"No nameservers found for {domain}. Writing to file {output_file_path}...", "red"))
                    file.write(domain + "\n") 
                    file.flush()  
                    os.fsync(file.fileno()) 
                    print(colored(f"Domain {domain} written to file {output_file_path}", "green"))
            except Exception as e:
                print(f"Error checking domain {domain}: {e}")
            print()  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 domaindnschecker.py path/to/domains.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        domains = [line.strip() for line in file if line.strip()]

    display_dns(domains)

if __name__ == "__main__":
    main()
