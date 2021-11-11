import requests, re
from bs4 import BeautifulSoup
 
data = requests.get("https://www.rawgear.com/collections/sale/products/rawgear-women-tie-dye-crop-t-shirt-rg3003").content
soup = BeautifulSoup(data, 'html.parser')
div = soup.find("h1", {"class":"ProductMeta__Title Heading u-h2"})
title = div.text
div = soup.find("span", {"class":"ProductMeta__Price Price Price--highlight Text--subdued u-h4"})
price = div.text
print("Item %s has price %s" % (title, price)) 
