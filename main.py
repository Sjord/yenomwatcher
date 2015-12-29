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
prices = soup.select('.hikashop_product_price_0')
for elem in prices:
    m = re.match(u'€ (\d+),\d+', elem.string)
    euro_price = int(m.group(1))
    if euro_price < 16:
        text = elem.find_parent('tr').select_one('.hikashop_product_name_row em').string
        print elem.string, text
