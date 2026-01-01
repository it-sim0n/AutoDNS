![img](https://github.com/it-sim0n/AutoDNS/blob/main/AutoDNS.jpg?raw=true)

# AutoDNS

AutoDNS is a portable DNS automation wrapper around **puredns**, designed for efficient and repeatable subdomain enumeration during reconnaissance and bug bounty workflows.

It provides an interactive CLI to resolve subdomains from lists or bruteforce them using wordlists, with optional dynamic permutation support.

---

## Features

- Resolve subdomains from an existing list
- Bruteforce subdomains using a wordlist
- Optional dynamic permutation using `dnsgen`
- Built-in resolver list (no external resolver file required)
- Simple interactive CLI
- Clean output saved per target domain

---

## Requirements

- Python **3.8+**
- [puredns](https://github.com/d3mondev/puredns)
- `massdns` (required by puredns)
- [dnsgen](https://github.com/ProjectAnte/dnsgen) *(optional, for dynamic mode)*

---

## Installation

### Linux / macOS

```bash
git clone https://github.com/YOUR_USERNAME/AutoDNS.git
cd AutoDNS
python3 -m pip install .
```
#### After installation, the CLI will be available as:
```bash
autodns
```

## Supported Operating Systems
### Linux
Fully supported and recommended.

Tested on common distributions (Ubuntu, Debian-based).

Native execution with no limitations.
### macOS
Supported.

Requires Go-installed puredns and massdns.

Recommended installation via Homebrew + Go.
### Windows 
AutoDNS does not run natively on Windows due to puredns and massdns dependencies.
## Recommended: Windows Subsystem for Linux (WSL2)
 1. Install WSL2 with Ubuntu:
 ```powershell
 wsl --install -d Ubuntu
```
2. Inside WSL:
```bash
sudo apt update
sudo apt install python3 python3-pip
go install github.com/d3mondev/puredns/v2@latest
pip install dnsgen
```
3. Clone and install AutoDNS:
```bash
git clone https://github.com/YOUR_USERNAME/AutoDNS.git
cd AutoDNS
python3 -m pip install .
```
4. Run:
```bash
autodns
```
## Usage
### Start the tool:
```bash
autodns
```
### You will be prompted interactively:
```css
Action?
1) Resolve subdomains from a list
2) Bruteforce subdomains using a wordlist
```
### Then provide:
Target domain.
Path to subdomain list or wordlist.
Optional dynamic mode if available.

## Output
### Results are automatically deduplicated and saved to:
```php-template
<domain>_pure.txt
```
## Notes
Resolver list is embedded inside the package.

Designed for Linux-based reconnaissance environments.

Intended for security research and authorized testing only.

# Author 
SIMON
