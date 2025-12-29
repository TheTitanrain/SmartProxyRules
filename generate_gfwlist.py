#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoProxy/GFWList Generator for SmartProxy
Extracts domains from SmartProxyRules.json, domains.txt, and inside-raw.lst
and generates a GFWList format file.
"""

import json
import base64
from datetime import datetime
from pathlib import Path


def extract_domains_from_json(json_file):
    """Extract enabled proxy domains from SmartProxyRules.json"""
    domains = set()

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Iterate through all proxy profiles
    for profile in data.get('proxyProfiles', []):
        # Get proxy rules from the profile
        for rule in profile.get('proxyRules', []):
            # Only include enabled rules that are not whitelisted
            if rule.get('enabled', False) and not rule.get('whiteList', False):
                hostname = rule.get('hostName', '')
                if hostname:
                    domains.add(hostname)

    return domains


def extract_domains_from_txt(txt_file):
    """Extract domains from domains.txt (one domain per line)"""
    domains = set()

    if not Path(txt_file).exists():
        print(f"Warning: {txt_file} not found, skipping...")
        return domains

    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            domain = line.strip()
            # Skip empty lines and comments
            if domain and not domain.startswith('#') and not domain.startswith('!'):
                domains.add(domain)

    return domains


def generate_gfwlist(domains, output_file='gfwlist.txt', title='SmartProxy Rules'):
    """Generate AutoProxy/GFWList format file"""

    # Sort domains alphabetically
    sorted_domains = sorted(domains)

    # Generate file content
    lines = [
        '[AutoProxy 0.2.9]',
        f'! Title: {title}',
        f'! Last Modified: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        f'! Total Rules: {len(sorted_domains)}',
        '! Homepage: https://github.com/salarcode/SmartProxy',
        ''
    ]

    # Add domain rules with || prefix
    for domain in sorted_domains:
        lines.append(f'||{domain}')

    # Write to file
    content = '\n'.join(lines)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Generated {output_file} with {len(sorted_domains)} domains')

    # Also generate base64 encoded version (common for GFWList)
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    encoded_file = str(output_file).replace('.txt', '.base64.txt')

    with open(encoded_file, 'w', encoding='utf-8') as f:
        f.write(encoded_content)

    print(f'Generated {encoded_file} (base64 encoded)')


def main():
    """Main function"""
    script_dir = Path(__file__).parent

    # Input files
    json_file = script_dir / 'SmartProxyRules.json'
    txt_file = script_dir / 'domains.txt'
    inside_raw_file = script_dir / 'inside-raw.lst'

    # Output file
    output_file = script_dir / 'gfwlist.txt'

    print('AutoProxy/GFWList Generator for SmartProxy')
    print('=' * 50)

    # Extract domains from JSON
    print(f'\nReading {json_file.name}...')
    json_domains = extract_domains_from_json(json_file)
    print(f'   Found {len(json_domains)} domains')

    # Extract domains from TXT
    print(f'\nReading {txt_file.name}...')
    txt_domains = extract_domains_from_txt(txt_file)
    print(f'   Found {len(txt_domains)} domains')

    # Extract domains from inside-raw.lst
    print(f'\nReading {inside_raw_file.name}...')
    inside_raw_domains = extract_domains_from_txt(inside_raw_file)
    print(f'   Found {len(inside_raw_domains)} domains')

    # Combine and deduplicate
    all_domains = json_domains | txt_domains | inside_raw_domains
    print(f'\nTotal unique domains: {len(all_domains)}')

    # Generate GFWList
    print(f'\nGenerating GFWList...')
    generate_gfwlist(all_domains, output_file)

    print(f'\nDone! You can now use {output_file.name} as a subscription URL in SmartProxy')
    print(f'   Or use {output_file.name.replace(".txt", ".base64.txt")} for base64 encoded version')


if __name__ == '__main__':
    main()
