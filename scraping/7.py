import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news.yahoo.co.jp/topics/top-picks")
elem = driver.find_element(By.XPATH, '//*[@id="contentsWrap"]/div/div[1]/ul/li[1]/a')
elem.click()
time.sleep(1)
soup = BeautifulSoup(driver.page_source, "html.parser")
for i in soup.select(".newsFeed_item_title"):
    print(i.text)
