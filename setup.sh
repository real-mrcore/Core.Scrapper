#!/bin/bash

clear
echo -e "\e[1;36m[+] Initializing Deployment Script for Core.Scrapper v3.2.4...\e[0m"
echo -e "\e[1;32m[+] Lead Engineer: Mr. Core\e[0m"
echo -e "\e[1;33m[+] Communications Path: t.me/real_mrcore\e[0m\n"

if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[-] System Error: Runtime environment 'Python3' is missing. Please install it first.\e[0m"
    exit 1
fi

echo -e "\e[1;34m[*] Provisioning modern application libraries...\e[0m"
python3 -m pip install -r requirements.txt

echo -e "\e[1;34m[*] Tweaking execution layer flags...\e[0m"
chmod +x core_scrapper.py

echo -e "\e[1;32m\n[+] Framework Installation Finished Successfully!\e[0m"
echo -e "\e[1;35m[+] Launch application engine using: python core_scrapper.py\e[0m"
