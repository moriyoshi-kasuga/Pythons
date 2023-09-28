import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.python.org/")
soup = BeautifulSoup(web.content, "html.parser")

[
    print(c.select_one("a").text)
    for c in soup.select_one("ul.menu[role='tree']").select("li")
]
