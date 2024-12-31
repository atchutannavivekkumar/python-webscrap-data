import requests
from bs4 import BeautifulSoup as bs

def get_free_proxies():
    url = "https://www.freeproxy.world/"
    # request and grab the content
    soup = bs(requests.get(url).content,'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("table", attrs={"class": "layui-table"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip() 
            port= tds[1].text.strip()
            proxies.append(str(ip)+ ":"+ str(port))
        except IndexError:
            continue

    
    return proxies
url = "http://httpbin.org/ip"
proxies = get_free_proxies()

print(proxies)
