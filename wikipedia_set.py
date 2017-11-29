from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(page_url):
    global pages
    html = urlopen("https://en.wikipedia.org"+page_url)
    soup = BeautifulSoup(html, "lxml")
    for link in soup.findAll("a", href= re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs['href'] not in pages:
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                getLinks(new_page)
            
getLinks("")
    
