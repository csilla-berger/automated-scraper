# Python Web Scraper Project

Hi! This is a static web scraper project I coded in Python to fetch data from a competitor website and save it into a spreadsheet.

I built it without using heavy browser tools like Selenium because the website loads its content in static HTML, making this scraper super fast!

## What It Does
* Connects to a competitor website using the 'request' library.
* Uses 'BeautifulSoup' to find things like product names, prices, and links in the HTML code.
* Saves everything automatically into a field called a 'competitor_market_report.csv'.
* Uses a '.gitignore' file so my scraped data does not get pushed to GitHub by accident.

## Code I Used
* Python 3
* Beautiful Soup 4
* Requests

## How to Setup and Run It

1. First, make sure you create a virtual environment so the packages stay separate:

'''bash
python3 -m venv venv
source venv/bin/activate
'''

2. Install the required libraries from the text file:

'''bash
pip install -r requirements.txt
'''

3. Run the script:

'''bash
python3 scraper.py
'''

## Next Steps for This Project
- [] Finish mapping out the HTML tags inside 'scraper.py'
- [] Add code to 'analytics_app.py' to calculate price averages and trends 
- [] Add loops to handle pagination if the website has multiple pages
