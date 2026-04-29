import requests
from bs4 import BeautifulSoup

url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(url)
soup = BeautifulSoup(r.content, "xml")

items = soup.find_all("item")

name = input("Enter the name of output file: ")
try:
    with open(f"{name}.txt", "w") as f:
        for item in items:
            title = item.title.text
            link = item.link.text
            desc = item.description.text
            f.write(f"TITLE: {title}\nLINK: {link}\nDESC: {desc}\n")
except Exception as e:
    print(f"Error: {e}")
