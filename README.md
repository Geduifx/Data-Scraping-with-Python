# Data Scraping with Python
![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=Geduifx.Data-Scraping-with-Python)

## Data extraction methods

I did some research on data scraping. Looks like there are 3 main extraction methods with Python:
- HTML parsing with Requests and Beautiful Soup Python libraries.
- Rendering JavaScript with Scrapy (web-crawling Python framework), Selenium (automation testing tool).
- API based scraping using API software (Insomnia, Postman etc.) and Python.

## My four mini projects

I needed some small-scale data from LinkedIn, but didn’t want to get blocked. So, decided to practice [parsing locally] and used Beautiful Soup to extract data from offline HTML and store that data in CSV file.

[parsing locally]: <https://github.com/Geduifx/Data-Scraping-with-Python/blob/main/01_Clipboard_scraping.py>

With a second mini project I wanted to upscale a bit. Scraped 3173 vacancies with 66k records from job listings website [using API]. On website used Chrome developer tools to check requests and responses and found that site uses API. With Insomnia software examined API calls, modified them and generated initial Python code. Then updated the code with delayed loops for limited multiple requests, used Pandas to normalize scraped JSON data and store it in CSV file.

[using API]: <https://github.com/Geduifx/Data-Scraping-with-Python/blob/main/02_API_scraping.py>

For a third project I decided to scrape product prices from three different sites and store the data in a [data base]. Used Requests, Beautiful Soup and SQLite Python libraries. Wrote single function to extract name, price, date and place all the data in to a list, then used variables from three different websites to run the function. Lastly created an SQLite data base and loaded all the data from nested lists to the data base.

[data base]: <https://github.com/Geduifx/Data-Scraping-with-Python/blob/main/03_Prices_scraping.py>

For forth project I practised coding a solution for [pagination]. Used loop and URLs with variables in them.

[pagination]: <https://github.com/Geduifx/Data-Scraping-with-Python/blob/main/04_Pagination.py>

## Future projects

For next project it would be interesting to extract data by rendering JavaScript. Also, I would like to practice using headless browsers for browser fingerprinting, rotating proxies for IP-rate limiting, residential IPs instead of data center IPs, forge and rotate TLS fingerprints, CAPTCHA-solving tools and services.
