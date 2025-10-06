# SmartProxyRules

AutoProxy/GFWList generator for [SmartProxy](https://github.com/salarcode/SmartProxy) extension.

## Description

This repository contains a script for automatically generating proxy rule lists in AutoProxy/GFWList format from SmartProxy settings and additional domains.

## Files

- **SmartProxyRules.json** - Exported settings from SmartProxy
- **domains.txt** - Additional domains (one domain per line)
- **generate_gfwlist.py** - GFWList generation script
- **gfwlist.txt** - Generated rule list (AutoProxy format)
- **gfwlist.base64.txt** - Base64-encoded version of the list

## Usage

### 1. Generate rule list

#### Automatic generation (GitHub Actions)

Whenever `SmartProxyRules.json` or `domains.txt` is changed, GitHub Actions automatically generates new `gfwlist.txt` and `gfwlist.base64.txt` files.

You can also trigger it manually:
1. Go to the Actions tab in the repository
2. Select "Generate GFWList"
3. Click "Run workflow"

#### Local generation

```bash
python generate_gfwlist.py
```

The script:
- Extracts domains from SmartProxyRules.json (only active rules with proxy enabled)
- Adds domains from domains.txt
- Generates gfwlist.txt and gfwlist.base64.txt

### 2. Use in SmartProxy

Use the direct link to gfwlist.txt from GitHub:

```
https://raw.githubusercontent.com/YOUR_USERNAME/SmartProxyRules/main/gfwlist.txt
```

Or for the base64 version:

```
https://raw.githubusercontent.com/YOUR_USERNAME/SmartProxyRules/main/gfwlist.base64.txt
```

In SmartProxy:
1. Go to "Smart Proxy" profile settings
2. Add a Rules Subscription
3. Specify the URL of your file

## AutoProxy/GFWList Format

```
[AutoProxy 0.2.9]
! Title: SmartProxy Rules
! Last Modified: 2025-10-06
||domain1.com
||domain2.com
```

Where `||domain.com` means proxying the domain and all its subdomains.

## License

Apache License 2.0
