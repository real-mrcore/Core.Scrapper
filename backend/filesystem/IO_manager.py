import os

def enforce_storage_directory():
    if not os.path.exists("scraped_data"):
        os.makedirs("scraped_data")

def clean_input_payload(url):
    url = url.strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url
