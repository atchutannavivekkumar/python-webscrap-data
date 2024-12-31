import requests
from bs4 import BeautifulSoup

req = requests.get("https://newerp.kluniversity.in/")
soup = BeautifulSoup(req.content, "html.parser")

print(soup.find_all("a"))