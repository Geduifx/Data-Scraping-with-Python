#  Chrome > Developer tools > Network > XHR > Response.
#  Copy as cURL GET request with needed info.
#  In Chrome Network could use filter - API.
#  Good sign if web page has load more button. Use it, check new GET request.
#  Use cURL in API software (Insomnia or similar). Can change query settings.
#  JSON. Check keys and their structure, number of items on page, total etc.
#  Can delete keys from query options.
#  Generate Python code with Requests.

# Code from Insomnia
"""
import requests

url = "https://www.cvonline.lt/api/v1/vacancy-search-service/search"

querystring = {"limit":"20","offset":"0"}

payload = ""
headers = {
    "authority": "www.cvonline.lt",
    "accept": "application/json, text/plain, */*",
    "accept-language": "lt",
    "cookie": "_gcl_au=1.1.889848350.1664798775; _hjSessionUser_1182319=eyJpZCI6IjY4NDFhZDJhLWIzYTAtNWI5OS04ZTUzLTk1ZTZhMjRmYzJjZiIsImNyZWF0ZWQiOjE2NjQ3OTg3NzQ5MDEsImV4aXN0aW5nIjp0cnVlfQ==; seekerPopupBannerShown=true; cvoCookieConsent=true; cvoCookieConsentMain=true; _gid=GA1.2.1201789679.1666634003; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0; _hjSession_1182319=eyJpZCI6ImNkY2M3M2MwLWU4ZGItNDM5Ni1iODYzLTNiNTYxZDQ2NjIwOCIsImNyZWF0ZWQiOjE2NjY2ODAxMzgyNzQsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _ga=GA1.2.1308057649.1664798775; _ga_XSN7WTZQVM=GS1.1.1666680138.10.1.1666680364.25.0.0",
    "referer": "https://www.cvonline.lt/lt/search?limit=20&offset=0&isHourlySalary=false",
    "sec-ch-ua": "^\^Chromium^^;v=^\^106^^, ^\^Google"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
"""

#  Create loop for multiple pages. Delay. Messages after loops.
#  Use Pandas to normalize scraped json data.
#  Store results in CSV.

# Import libraries
import requests  # Gets HTML.
import pandas as pd  # Normalizes JSON.
import time  # Use time.

url = "https://www.cvonline.lt/api/v1/vacancy-search-service/search"

results = []  # List for results.

x = 0
# There are 3173 listings in total. Limit 500 listings per request and use delay.
while x <= 3200:

    #  Limit - number of items (total 3173), offset - used for pagination.
    querystring = {"limit":"500","offset":f"{x}"}

    headers = {
        "authority": "www.cvonline.lt",
        "accept": "application/json, text/plain, */*",
        "accept-language": "lt",
        "cookie": "_gcl_au=1.1.889848350.1664798775; _hjSessionUser_1182319=eyJpZCI6IjY4NDFhZDJhLWIzYTAtNWI5OS04ZTUzLTk1ZTZhMjRmYzJjZiIsImNyZWF0ZWQiOjE2NjQ3OTg3NzQ5MDEsImV4aXN0aW5nIjp0cnVlfQ==; seekerPopupBannerShown=true; cvoCookieConsent=true; cvoCookieConsentMain=true; _gid=GA1.2.1201789679.1666634003; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0; _hjSession_1182319=eyJpZCI6ImNkY2M3M2MwLWU4ZGItNDM5Ni1iODYzLTNiNTYxZDQ2NjIwOCIsImNyZWF0ZWQiOjE2NjY2ODAxMzgyNzQsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _ga=GA1.2.1308057649.1664798775; _ga_XSN7WTZQVM=GS1.1.1666680138.10.1.1666680364.25.0.0",
        "referer": "https://www.cvonline.lt/lt/search?limit=20&offset=0&isHourlySalary=false",
        "sec-ch-ua": "^\^Chromium^^;v=^\^106^^, ^\^Google"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    # print(len((data['vacancies']))) #Print length of list.

    for item in data['vacancies']:
        results.append(item)  # Add item to results list.

    # print(len(results)) # Check if results list works.

    # Create data frame with Pandas.
    data_frame = pd.json_normalize(results)
    # print(data_frame['positionContent']) # Prints column with LT symbols from data frame.

    #  Write results to CSV.
    #  Need to use encoding='utf-8-sig' to correctly write LT simbols.
    #  mode='a' - append.
    data_frame.to_csv('cvbankas.csv', mode='a', header=False, encoding='utf-8-sig')

    x = x + 500
    results = []  # Clear results list.

    print('Wrote results to CSV, delays for 32.5 seconds.')
    time.sleep(32.5)  # Delays for 32.5 seconds.
