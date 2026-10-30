import csv
import logging
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Configure logging to track architecture health and connection events.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CompetitorIntelligenceScraper:
    def __init__(self, target_url):
        self.target_url = target_url
        # Premium browser header to prevent anti-scraping flags from target competitors.
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

    def fetch_competitor_page(self):
        """Executes a secure network request to pull the raw competitor HTML data."""
        try:
            logging.info(f"Connecting to competitor domain: {self.target_url}")
            response = requests.get(self.target_url, headers=self.headers, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Critical connection failure to competitor catalog: {e}")
            return None

    def parse_intelligence_data(self, html_content):
        """Parses competitor product elements, tracking live pricing and stock indicators."""
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        competitor_products = []

        # Target structural item containers on the e-commerce sandbox architecture.
        products = soup.select('.product_pod')

        for product in products:
            try:
                # Capture Product Identity
                product_name = product.select_one('h3 a')['title']

                # Capture Competitor Price Matrix
                live_price = product.select_one('.price_color').get_text(strip=True)

                # Capture Inventory Availability Signals
                stock_status = product.select_one('.instock.availability').get_text(strip=True)

                competitor_products.append({
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'product_name': product_name,
                    'competitor_price': live_price,
                    'stock_status': stock_status
                })
            except AttributeError as e:
                # Skip rows or grid cells that don't contain valid product components.
                logging.debug(f"Skipping structural element fragment: {e}")
                continue

        logging.info(f"Extraction complete. Captured data for {len(competitor_products)} competitor items.")
        return competitor_products

    def export_intelligence_report(self, dataset, filename="competitor_market_report.csv"):
        """Compiles tracked metrics into a structured CSV business intelligence report."""
        if not dataset:
            logging.warning("No operational data captured to compile a report.")
            return

        column_headers = dataset[0].keys()
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=column_headers)
                writer.writeheader()
                writer.writerows(dataset)
                logging.info(f"Market data successfully exported to report format: {filename}")
        except IOError as e:
            logging.error(f"Failed to generate CSV data stream output: {e}")

if __name__ == "__main__":
    # Pointing to the functional market catalog sandbox environment.
    COMPETITOR_CATALOG_URL = "http://books.toscrape.com" 

    # Initialize the competitive intelligence pipeline.
    tracker = CompetitorIntelligenceScraper(COMPETITOR_CATALOG_URL)

    # Execute lifecycle steps
    raw_html = tracker.fetch_competitor_page()
    market_metrics = tracker.parse_intelligence_data(raw_html)
    tracker.export_intelligence_report(market_metrics)