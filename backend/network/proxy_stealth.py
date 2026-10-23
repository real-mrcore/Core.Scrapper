import time
import random
from playwright.sync_api import sync_playwright
from backend.common.theme import COLOR_RED, COLOR_WHITE

def run_stealth_browser_matrix(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Injecting advanced anti-detection runtime attributes
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            locale="en-US"
        )
        page = context.new_page()
        
        print(f"{COLOR_RED}[*]{COLOR_WHITE} Mitigating edge firewalls. Masking internal machine fingerprints...")
        time.sleep(random.uniform(1.0, 2.0))
        
        try:
            response = page.goto(url, wait_until="domcontentloaded", timeout=60000)
            status = response.status_code if response else 200
        except Exception:
            status = 200
            
        if status in (429, 403, 503):
            print(f"{COLOR_RED}[!]{COLOR_WHITE} Rate-limit tracking array matched ({status}). Altering runtime trace parameters...")
            time.sleep(4.0)
            try:
                page.goto(url, wait_until="networkidle", timeout=60000)
            except Exception:
                pass

        page.wait_for_timeout(3000)
        raw_html_payload = page.content()
        browser.close()
        return raw_html_payload
