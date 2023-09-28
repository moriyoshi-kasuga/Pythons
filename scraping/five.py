from bs4 import BeautifulSoup
from requests_html import HTMLSession

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


[
    r.find("td").text + " : " + r.find("th").text
    for r in BeautifulSoup(
        HTMLSession()
        .get("https://www.mizuhobank.co.jp/rate_fee/rate_interest.html")
        .html.render()
        .raw_html,
        "html.parser",
    )
    .select_one("table[data-market-id='bk07'] tbody")
    .findChildren("tr")
]
