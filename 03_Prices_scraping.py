# Import libraries
import requests  # Get HTTP.
from bs4 import BeautifulSoup  # Parse HTTP.
from datetime import datetime  # Use date and time.
import re  # Extract numbers from string.
import sqlite3  # Create data base.

# Headers, to show that requests are from browser, not Python. Google "my user agent".
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

# List for 3 result lists.
all_results = []

# BeautifulSoup for HTML parsing.
# Find (just first header) or find_all (list of headers).
# Can search multiple headers ["h1", "h2"].
# Can filter by multiple attributes attrs={'itemprop':'price'}.
# Can use find().text, find().attrs, find().contents etc.
# Different functions might be more suitable for different web pages.

# Define scraping function.
def scrape (url, header, atr_key, atr_value):
    # List for results.
    results = []
    # Extract name from url.
    lt_position = url.find('.lt')
    name = url[12:lt_position]
    # Get HTTP with requests.
    data = requests.get(url, headers=headers)
    # Parse HTTP with BeautifulSoup.
    soup = BeautifulSoup(data.text, "html.parser")
    # Find price, different filter parameters for different web sites.
    # Could also use attrs or contents etc. instead of find.text.
    find_price = soup.find(header, attrs={atr_key: atr_value}).text
    # Format price. Could also check text.strip or text.replace.
    price = re.sub('[^0-9]', '', find_price)  # Extract numbers from find_price.
    comma = len(price) - 2 # Find where to place comma.
    price = price[:comma] + '.' + price[comma:]
    # Current time.
    created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # Add name, price, date to list.
    results.append(name)
    results.append(price)
    results.append(created_at)
    # Add list to all_results list which will be loaded in to the data base.
    # Could load each item or list in to the data base separately.
    all_results.append(results)

# Scrape page 1
url = 'https://www.pigu.lt/lt/kompiuterine-technika/projektoriai/projektorius-xiaomi-mi-laser-projector-150?id=24475540'
header = 'meta'
atr_key = 'itemprop'
atr_value = 'price'
# Run scraping function.
scrape(url, header, atr_key, atr_value)

# Scrape page 2
url = 'https://www.skytech.lt/6934177701788-laser-projector-150-p-425643.html'
header = 'span'
atr_key = 'class'
atr_value = 'num'
scrape(url, header, atr_key, atr_value)

# Scrape page 3
url = 'https://www.senukai.lt/p/projektorius-xiaomi-mi-150/awbk'
header = 'span'
atr_key = 'class'
atr_value = 'price'
scrape(url, header, atr_key, atr_value)

# For larger number of websites could use list of URLs and search parameters.
# Then loop the list with scrape function.

# print(all_results) # Check if everything works.

# Write all_results list to data base.

# Connect to data base.
connection = sqlite3.connect('prices.db')
# Create cursor to interact with db.
cursor = connection.cursor()

# Delete, create table.
cursor.execute("DROP TABLE prices")
cursor.execute("""CREATE TABLE IF NOT EXISTS
prices(name TEXT, price REAL, created_at DATE)""")

# Add all_results list to table.
sqlite_insert_query = """INSERT INTO prices
                      (name, price, created_at) 
                      VALUES (?, ?, ?);"""
cursor.executemany(sqlite_insert_query, all_results)

# # Create, update, delete information in table examples.
# cursor.execute("INSERT INTO prices VALUES ('first', 'price', 'date')")
# cursor.execute("INSERT INTO prices VALUES (?, ?, ?)", (name, price, created_at))
# cursor.execute("UPDATE prices SET price = '99' WHERE name = 'first'")
# cursor.execute("DELETE FROM prices WHERE name = 'first'")

# Save changes to data base.
connection.commit()
# Get all data from table and print
cursor.execute("SELECT * FROM prices")
print(cursor.fetchall())