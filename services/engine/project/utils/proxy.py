import requests
from bs4 import BeautifulSoup
import random


def get_proxy():
    print('getting proxy.....')
    res = requests.get('https://free-proxy-list.net/')

    soup = BeautifulSoup(res.text, 'html5lib')
    table = soup.find('table', attrs={'id': 'proxylisttable'}).find('tbody')
    table_rows = table.find_all('tr')
    table_rows = table_rows[15:]

    proxies = []
    for row in table_rows:
        tds = row.find_all('td')
        ip = tds[0].text
        port = tds[1].text
        proxy = 'http://{}:{}'.format(ip, port)
        proxies.append(proxy)

    # generated = random.choice(proxies)
    # print('{} generated'.format(generated))
    # return random.choice(proxies)
    url = 'https://httpbin.org/ip'
    for proxy in proxies:
        # Get a proxy from the pool
        print('Request {}'.format(proxy))
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
            print(response.json())
            print('{} generated'.format(proxy))
            return proxy
        except:
            print("Skipping. Connnection error")

# get_proxy()