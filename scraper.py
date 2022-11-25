import requests
import json
import pymongo as pymo
from bs4 import BeautifulSoup
import lxml

response = requests.get('https://www.hpra.ie/img/uploaded/swedocuments/latestVMlist.xml')
print("download done")
data = response.content

# Create a BeautifulSoup object
soup = BeautifulSoup(data, 'xml')

# filter out all productnames into list of dictionaries
parent = soup.find('Products')
products = []
for n, product in enumerate(parent.find_all('Product')):
    if product.find('Species').text.strip() == 'Horses':
        dict = {"name" : product.find('ProductName').text.strip()}
        products.append(dict)
# for item in products:
#     print(item)

json_data = json.dumps(products, indent = 2)
print(json_data)

