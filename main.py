# coding: utf-8
import requests
from bs4 import BeautifulSoup
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

url = 'http://www.yenom.nl/slijterijaanbiedingen/search/111/absolut'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
prices = soup.select('.hikashop_product_price_with_discount')
for elem in prices:
    m = re.match(u'€ (\d+),\d+', elem.string)
    euro_price = int(m.group(1))
    if euro_price < 16:
        print elem.string, url
