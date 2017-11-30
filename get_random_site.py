from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import random
import datetime

#get all the internal links
def getInternalLinks(soup, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    for link in soup.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startwith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                    
                else:
                    internalLinks.append(link.attrs['href'])
                    
    return internalLinks
    
#get all the external links
def getExternalLinks(soup, excludeUrl):
    externalLinks = []
    for link in soup.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
    
#split URL address
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts
    
#get random External links
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    soup = BeautifulSoup(html, "lxml")
    
    externalLinks = getExternalLinks(soup, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around internal links")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(soup, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,
            len(internalLinks)-1)])
    else:
        return getRandomExternalLink(externalLinks[random.randint(0, len(externalLinks)-1)])
            
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLinks)
    followExternalOnly(externalLink)
'''    
userInput = input("Please enter an URL to start: ")
followExternalOnly(userInput)
'''
followExternalOnly("https://oreilly.com")
