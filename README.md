Nameserver Checker for Domains

Description
This Python script provides a convenient way to check the nameservers of multiple domains through WHOIS lookups. If a domain doesn't have any associated nameservers, it will be flagged and written to an output file called "missingdnsdomains.txt". This can be particularly useful for domain administrators, IT professionals, or anyone interested in auditing their domain nameservers.

Features
Batch Domain Checking: Efficiently check nameservers for multiple domains in one go.
Detailed Output: For each domain, the script fetches and displays its associated nameservers.
Error Handling: If a domain has no nameservers or an error occurs during the WHOIS lookup, it's captured and noted.
Output File Generation: Domains with missing nameservers are automatically written to "missingdnsdomains.txt" for easy review and action.
Usage
The script is designed to be user-friendly and can be run directly from the terminal.

On macOS:


python3 nameserver-checker.py path/to/domains.txt
File Format:
Ensure the domains are listed in the 'domains.txt' file with one domain per line:


example1.com
example2.org
example3.net
...
