import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.python.org/")
soup = BeautifulSoup(web.content, "html.parser")

[
    print(c.find("a").text)
    for c in soup.select_one("ul[aria-label='Main Navigation']").findChildren(
        "li", recursive=False
    )
]
