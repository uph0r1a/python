import requests
from bs4 import BeautifulSoup

url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(url)
soup = BeautifulSoup(r.content, "xml")

items = soup.find_all("item")

for item in items[:5]:
    title = item.title.text
    link = item.link.text
    desc = item.description.text

    print("TITLE:", title)
    print("LINK:", link)
    print("DESC:", desc)
    print("-" * 50)
