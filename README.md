# pastebin-keyword-crawler
Python scraper to detect crypto keywords or Telegram links in Pastebin pastes. Includes logging, deduplication, and JSON output.
#Pastebin Keyword Crawler

A Python-based web scraper that crawls [Pastebin's public archive](https://pastebin.com/archive) and extracts recent pastes containing specified **keywords** such as crypto-related terms or Telegram links (`t.me`).

---

## Objective

- Scrape the latest 30 public pastes from Pastebin.
- Search for keywords like `"crypto"`, `"bitcoin"`, `"t.me"`, etc.
- Store matching results in structured JSONL format (`keyword_matches.jsonl`).
- Prevent duplicate processing using `seen_ids.txt`.
- Implement rate limiting and logging.

---

## Technologies Used

- Python 3.8+
- `requests`
- `beautifulsoup4`
- Standard Python modules: `json`, `time`, `datetime`, `logging`, `os`

---

##  Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/pastebin-keyword-crawler.git
cd pastebin-keyword-crawler

## How to Run the Crawler

Follow these steps to set up and run the `crawler.py` script on any system with Python 3.8+ installed.

### 1. Install Python

Make sure you have **Python 3.8 or above** installed.  
Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

###  2. Install Required Dependencies

Open your terminal and run:

```bash
pip install requests beautifulsoup4

Use this command to run
python crawler.py
