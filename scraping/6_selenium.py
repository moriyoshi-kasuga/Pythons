import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrom()
driver.get("https://www.livedoor.com/")
elem = driver.find_element(By.ID, "topics_category_11")
elem.click()
time.sleep(1)
soup = BeautifulSoup(driver.page_source, "html.parser")
for i in soup.select("#newstopicsbox ol a"):
    print(i.text)
