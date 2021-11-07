import requests, re
from bs4 import BeautifulSoup 
data = requests.get("https://www.reebok.com/us/national-geographic-club-c-mens-shoes/GY1200.html").content
soup = BeautifulSoup(data, 'html.parser')
span=soup.find("h1", {"class":"gl-heading gl-heading--regular gl-heading--italic name___1EbZs"})
title = span.text
span=soup.find("div",{"class":"product-price___gJhOl gl-vspace"})
price = span.text
print("Item is %s has price %s" % (title, price))