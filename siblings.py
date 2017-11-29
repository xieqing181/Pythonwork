from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "lxml")

#print(soup.prettify())

'''try for .siblings()
for sibling in soup.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)
'''
#trying parent and .previous_sibling()
#print(soup.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.string)

#try use regex here
for img in soup.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img\d*\.jpg")}):
    print(img['src'])
    
print(soup.table.attrs)
print(soup.img.attrs["src"])
