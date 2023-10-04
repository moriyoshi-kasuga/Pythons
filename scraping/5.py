# from bs4 import BeautifulSoup
# from requests_html import HTMLSession
#
# r = HTMLSession().get("https://www.mizuhobank.co.jp/rate_fee/rate_interest.html")
# r.html.render()
#
#
# [
#     print(c.find("td").text + " : " + c.find("th").text)
#     for c in BeautifulSoup(r.html.raw_html, "html.parser")
#     .select_one("table[data-market-id='bk07'] tbody")
#     .findChildren("tr")
# ]
import time

from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.mizuhobank.co.jp/rate_fee/rate_interest.html")
time.sleep(1)
soup = BeautifulSoup(driver.page_source, "html.parser")

[
    print(c.find("td").text + " : " + c.find("th").text)
    for c in soup.select_one("table[data-market-id='bk07'] tbody").findChildren("tr")
]
