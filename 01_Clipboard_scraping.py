# Import libraries
from bs4 import BeautifulSoup  # Parse HTML.
import csv  # Write to csv.
import win32clipboard  # Work with Win clipboard.

#  Open csv file.
#  For file update use append mode 'a', for new file write 'w'.
#  newline='' to avoid blank lines.
file_csv = open('scrape.csv', 'a', newline='', encoding="utf8")

# Variable for writing csv.
writer = csv.writer(file_csv)

# Practice parsing locally, don't get blocked.
# Get clipboard data.
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

# # Could also use saved HTML.
# data = codecs.open('file.html', "r", "utf-8")

# Parse HTML from clipboard with BeautifulSoup.
soup = BeautifulSoup(data, 'lxml')  # with lxml library

# Find names and titles based on Chrome Inspect.
names = soup.find_all('span', attrs={'dir': 'ltr'})
titles = soup.find_all('div', attrs={'class': 'entity-result__primary-subtitle'})
titles_2 = soup.find_all('p', attrs={'class': 'entity-result__summary'})

# Print and write results to CSV.
for a, b, c in zip(names, titles, titles_2):
    print(a.text + ';' + b.text + ';' + c.text)
    writer.writerow([a.text, b.text, c.text])

#CLOSE THE CSV FILE
file_csv.close()