import os
from bs4 import BeautifulSoup
from backend.common.theme import COLOR_RED, COLOR_WHITE
from backend.filesystem.IO_manager import enforce_storage_directory, clean_input_payload
from backend.network.proxy_stealth import run_stealth_browser_matrix

def execute_css_scraping_routine():
    print(f"{COLOR_RED}[*] --- INITIALIZING ADVANCED CASCADING ELEMENT CSS BLUEPRINT MODULE ---")
    url_input = input(f"{COLOR_WHITE}[?] Enter Target Endpoint Resource URL: ")
    if not url_input.strip():
        print(f"{COLOR_RED} [-] Runtime Execution Fault: Provided URL payload data stream cannot be empty.")
        return

    url = clean_input_payload(url_input)
    print(f"{COLOR_RED}[*]{COLOR_WHITE} Scanning remote elements presentation layers at {url}...")

    try:
        enforce_storage_directory()
        domain = url.split("//")[-1].replace("/", "_").replace(".", "_")
        filename = f"scraped_data/css_{domain}.css"

        extracted_source = run_stealth_browser_matrix(url)
        
        if extracted_source:
            soup = BeautifulSoup(extracted_source, 'html.parser')
            compiled_css_code = ""

            styles = soup.find_all("style")
            for style in styles:
                if style.string:
                    compiled_css_code += "\n/* ==========================================\n   LOCAL EMBEDDED STYLESHEET DATA\n   ========================================== */\n"
                    compiled_css_code += style.string + "\n"

            if compiled_css_code.strip():
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(compiled_css_code)
                print(f"\n{COLOR_RED}[+]{COLOR_WHITE} Pipeline Success! Element styling layout mapped successfully.")
                print(f"{COLOR_RED}[+]{COLOR_WHITE} Absolute Output Destination Vault: {os.path.abspath(filename)}")
            else:
                print(f"{COLOR_RED}[!] System Alert: No inline stylesheet fields identified on root frame level.")
        else:
            print(f"{COLOR_RED}[-]{COLOR_WHITE} Pipeline Exception: Connection pipeline refused by endpoint.")
    except Exception as e:
        print(f"{COLOR_RED}[-]{COLOR_WHITE} Critical Logic Crash within CSS Framework Layer: {str(e)}")
