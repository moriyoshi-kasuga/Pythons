from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=python")
soup = BeautifulSoup(driver.page_source, "html.parser")
for i in soup.select(".LC20lb.MBeuO.DKV0Md"):
    print(i.text)
