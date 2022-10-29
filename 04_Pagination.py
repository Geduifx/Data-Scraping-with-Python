# Import libraries
from bs4 import BeautifulSoup  # Parse HTML.
import csv  # Write to csv.
import requests  # Get HTTP.

#  For file update use append mode 'a', for new file write 'w'. newline='' to avoid blank lines.
file_csv = open('titles.csv', 'a', newline='', encoding="utf8")
writer = csv.writer(file_csv)

# Headers, to show that requests are from browser, not Python. Google "my user agent".
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

# This web site shows 25 job listings per page.
# Modify URL with variable {step} and use loop to scrape first 4 pages.
step = 0
while step <= 75:
    url = f'https://www.cvmarket.lt/kaunas?start={step}'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, "html.parser")
    titles = soup.find_all(attrs={'class':'f_job_title main_job_link limited-lines'})
    for x in titles:
        writer.writerow([x.text])
    step = step + 25
file_csv.close()
