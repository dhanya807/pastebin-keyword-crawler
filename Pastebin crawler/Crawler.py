import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time
import logging
import os

logging.basicConfig(
    filename='crawler.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Loading Keywords from File 
if not os.path.exists('keywords.txt'):
    print(" 'keywords.txt' file not found. Please create one with keywords (one per line).")
    exit()

with open('keywords.txt') as f:
    keywords = [line.strip().lower() for line in f if line.strip()]

if not keywords:
    print(" No keywords found in 'keywords.txt'. Add at least one.")
    exit()

#Output File
output_file = "keyword_matches.jsonl"

seen_ids = set()

# Scraping Pastebin Archive
response = requests.get("https://pastebin.com/archive")
soup = BeautifulSoup(response.text, "html.parser")
paste_links = soup.select("table.maintable tr a[href^='/']")[:30]
paste_ids = [link["href"].split("/")[-1] for link in paste_links]

# Match Counter
total_matches = 0

for paste_id in paste_ids:
    if paste_id in seen_ids:
        continue
    seen_ids.add(paste_id)

    raw_url = f"https://pastebin.com/raw/{paste_id}"
    try:
        content = requests.get(raw_url).text
        time.sleep(2)  # Rate limiting: 2 seconds delay between requests
    except Exception as e:
        logging.warning(f"Failed to fetch {paste_id}: {e}")
        continue

    found_keywords = [kw for kw in keywords if kw in content.lower()]

    if found_keywords:
        result = {
            "source": "pastebin",
            "context": f"Found crypto-related content in Pastebin paste ID {paste_id}",
            "paste_id": paste_id,
            "url": raw_url,
            "discovered_at": datetime.utcnow().isoformat() + "Z",
            "keywords_found": found_keywords,
            "status": "pending"
        }

        with open(output_file, "a") as f:
            f.write(json.dumps(result) + "\n")

        total_matches += 1
        logging.info(f"Matched: {paste_id} | Keywords: {found_keywords}")
        print(f"Matched: {paste_id} | Keywords: {found_keywords}")
    else:
        logging.info(f"No match for: {paste_id}")
        print(f"No match for: {paste_id}")

print(f"\n Total matches found: {total_matches}")
logging.info(f"Scraping complete. Total matches: {total_matches}")
