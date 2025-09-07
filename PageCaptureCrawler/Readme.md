# PageCaptureCrawler

PageCaptureCrawler is a multithreaded web crawler written in Python that uses Selenium and BeautifulSoup to crawl web pages, take screenshots, and cache page content efficiently.

## Features
- Multithreaded crawling for faster performance
- Takes screenshots of each visited page using a headless Chrome browser
- Caches HTML content using an LRU (Least Recently Used) cache
- Only crawls links within the same domain
- Handles network errors gracefully

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup4
- Requests
- Chrome WebDriver (must be installed and available in PATH)

## Installation
1. Install required Python packages:
   ```powershell
   pip install selenium beautifulsoup4 requests
   ```
2. Download and install [Chrome WebDriver](https://sites.google.com/chromium.org/driver/).
   - Make sure the WebDriver executable is in your system PATH.

## Usage
Edit the `Code.py` file to set your desired start URL, number of threads, and cache capacity. Example:
```python
if __name__ == "__main__":
    crawler = WebCrawler("https://google.com", num_threads=4, cache_capacity=10)
    crawler.start()
```
Run the crawler:
```powershell
python Code.py
```

## Output
- Screenshots of each visited page are saved in the `screenshots` directory.
- Console output shows crawling progress and errors.

## Notes
- Only links within the same domain as the start URL are crawled.
- The crawler uses a headless Chrome browser for screenshots.
- Adjust the number of threads and cache size as needed for your use case.

## License
This project is provided for educational purposes.
