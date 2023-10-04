import itertools

import requests
from bs4 import BeautifulSoup

web = requests.get("https://qiita.com/advent-calendar/2016/crawler")
soup = BeautifulSoup(web.content, "html.parser")


[
    print(f"{a.get('href')} : {a.text} ")
    for a in itertools.chain.from_iterable(
        [
            [
                td.select_one("div.style-176zglo > div.style-1dctyxx a")
                for td in tr.findChildren("td")
                if td.find("div", {"class": "style-176zglo"})
            ]
            for tr in soup.find("tbody", {"class": "style-azrjx0"})
        ]
    )
]
