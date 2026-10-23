#!/bin/bash

clear
echo -e "\e[1;36m[+] Initializing Deployment Script for Core.Scrapper v3.2.4...\e[0m"
echo -e "\e[1;32m[+] Lead Engineer: Mr. Core\e[0m"
echo -e "\e[1;33m[+] Communications Path: t.me/real_mrcore\e[0m\n"

# Step 1: Detect and Fix missing Python3
if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[-] System Error: 'Python3' is missing. Installing package...\e[0m"
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install python3 -y
    elif command -v pkg &> /dev/null; then
        pkg install python3 -y
    fi
fi

# Step 2: Detect and Fix missing pip automatically (VPS Fix)
if ! python3 -m pip --version &> /dev/null; then
    echo -e "\e[1;33m[*] Package manager 'pip' not found. Deploying standalone pip installer...\e[0m"
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install python3-pip -y
    elif command -v pkg &> /dev/null; then
        pkg install python3-pip -y
    else
        curl -sS https://pypa.io | python3
    fi
fi

# Step 3: Install application requirements with OS bypass flags
echo -e "\e[1;34m[*] Provisioning modern application libraries...\e[0m"
python3 -m pip install -r requirements.txt --break-system-packages 2>/dev/null || python3 -m pip install -r requirements.txt

# Step 4: Provision headless binaries for Playwright Core
echo -e "\e[1;34m[*] Downloading system binary drivers for browser environments...\e[0m"
python3 -m playwright install chromium
if command -v apt &> /dev/null; then
    sudo python3 -m playwright install-deps 2>/dev/null || sudo python3 -m playwright install-deps
fi

echo -e "\e[1;34m[*] Tweaking execution layer flags...\e[0m"
chmod +x core_scrapper.py

echo -e "\e[1;32m\n[+] Framework Installation Finished Successfully!\e[0m"
echo -e "\e[1;35m[+] Launch application engine using: python3 core_scrapper.py\e[0m"
