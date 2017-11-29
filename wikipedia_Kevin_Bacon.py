from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

'''def a function to get the link point to other topic inside Wiki'''
def getLinks(articleUrl):

    html = urlopen("https://en.wikipedia.org"+articleUrl)
    soup = BeautifulSoup(html, "lxml")

    topic_list = []

    for topic in soup.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in topic.attrs:
            topic_list.append(topic.attrs['href'])
            
    return topic_list
            
topics = getLinks("/wiki/Kevin_Bacon")
random.seed(datetime.datetime.now())

#try to random walk 20 topics
i = 1
while len(topics) > 0 and i<20:
    new_topic = topics[random.randint(0,len(topics)-1)]
    print(str(i)+ " : " + new_topic)
    topics = getLinks(new_topic)
    i = i+1
