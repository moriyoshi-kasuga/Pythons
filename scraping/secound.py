import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.python.org/")
soup = BeautifulSoup(web.content, "html.parser")

[
    print(f"{c.find('time').text} : {c.find('a').text}")
    for c in soup.select_one("div.event-widget div ul").select("li")
]
