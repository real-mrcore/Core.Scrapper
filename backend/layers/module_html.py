import os
from bs4 import BeautifulSoup
from backend.common.theme import COLOR_RED, COLOR_WHITE
from backend.filesystem.IO_manager import enforce_storage_directory, clean_input_payload
from backend.network.proxy_stealth import run_stealth_browser_matrix

def execute_html_scraping_routine():
    print(f"{COLOR_RED}[*] --- INITIALIZING DEEP STRUCTURAL DOM HTML EXTRACTION MODULE ---")
    url_input = input(f"{COLOR_WHITE}[?] Enter Target Endpoint Resource URL: ")
    if not url_input.strip():
        print(f"{COLOR_RED} [-] Runtime Execution Fault: Provided URL payload data stream cannot be empty.")
        return

    url = clean_input_payload(url_input)
    print(f"{COLOR_RED}[*]{COLOR_WHITE} Injecting automated scraping pipelines to target matrix: {url}...")

    try:
        enforce_storage_directory()
        domain = url.split("//")[-1].replace("/", "_").replace(".", "_")
        filename = f"scraped_data/html_{domain}.html"

        extracted_source = run_stealth_browser_matrix(url)
        
        if extracted_source:
            soup = BeautifulSoup(extracted_source, 'html.parser')
            prettified_html = soup.prettify()

            with open(filename, "w", encoding="utf-8") as f:
                f.write(prettified_html)

            print(f"\n{COLOR_RED}[+]{COLOR_WHITE} Pipeline Success! Deep structural document tree saved.")
            print(f"{COLOR_RED}[+]{COLOR_WHITE} Absolute Output Destination Vault: {os.path.abspath(filename)}")
        else:
            print(f"{COLOR_RED}[-]{COLOR_WHITE} Pipeline Exception: Connection pipeline refused by endpoint.")
    except Exception as e:
        print(f"{COLOR_RED}[-]{COLOR_WHITE} Critical Logic Crash within HTML Framework Layer: {str(e)}")
