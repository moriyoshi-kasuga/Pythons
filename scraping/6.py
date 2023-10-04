import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.livedoor.com/201401/topics/11.inc")
soup = BeautifulSoup(web.content, "html.parser")

[print(c.text) for c in soup.find("ol").select("li a")]
