import requests

from bs4 import BeautifulSoup

url = "https://klh.edu.in/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml") 

print(soup.find_all("a"))