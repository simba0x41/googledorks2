import requests,re
from bs4 import BeautifulSoup
import time
import random
import os
from urllib.parse import unquote

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    tabs = '    '
    print(tabs + '*******************************************************************')
    print(tabs + '* [+] [POC][Exploit] Google Dorks                                 *')
    print(tabs + '* [+] Massive Search                   :                          *')
    print(tabs + '* [+] T3sl4                                                       *')
    print(tabs + '*******************************************************************\n\n')


def proxies():
        file = 'proxies.txt'
        proxies = []
        with open(file, "r") as p:
            proxies = [line.strip() for line in p]
        proxy = random.choice(proxies)
        start = 0
        end = proxy.index(":")
        st = proxy[start:end]
        e = proxy[end+1:]
        proxie = {"http":"{}:{}".format(st, e)}
        return proxie

def user_agents():
        file = 'ua.txt'
        ua = []
        with open(file, "r") as txt:
            ua = [line.strip() for line in txt]
        user = random.choice(ua)
        header = {"User-Agent":"{}".format(user)}
        return header

def main():
    link = input('Dork -> ')
    header = {'User-Agent' : 'Megamind/ Tesla: revision', 'Cookie' : 'Megamind'}
    #header = user_agents()
    proxie = proxies()

    try:
        pages = int(input("Number of pages you want: "))
    except ValueError:
        print("It's not a number.")
        print("Number of pages set to 10 by default.")
        pages = 0
    try:
        sec = int(input("Seconds you want to wait between requests (5 secs recommanded to avoid being suspended by Google): "))
    except:
        print("It's not a number.")
        print("Seconds set to 5 by default")
    i = 0
    page = 0

    while i < pages:
        temp = []
        url = "https://www.google.com/search"
        payload = {'q' : link,'start' : page}
        #r = requests.get(url, headers=header, proxies=proxie)
        r = requests.get(url,params=payload,headers=header)
        soup = BeautifulSoup(r.text, "html.parser")
        divtags = soup.find_all('div',class_='kCrYT')
        for div in divtags:
            try:
                temp.append(re.search('url\?q=(.+?)\&sa', div.a['href']).group(1))
            except:
                continue
        temp = list(set(temp))
        for x in range(10):
            print(unquote(temp[x]))
        
        time.sleep(sec)
        page += 10
        i += 1

if __name__ == "__main__":
    draw()
    main()
