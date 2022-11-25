import requests
import json
import pymongo 
from bs4 import BeautifulSoup
import lxml

import certifi
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Cluster2User:gPId3Gm4a0I9icN5@agile2cluster.bxvcw4l.mongodb.net/?retryWrites=true&w=majority",tls=True, tlsAllowInvalidCertificates=True)
db = client.test
mydb = client["Test"]
mycol = mydb["CollectionTest"]
mycol.drop()


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

json_data = json.dumps(products, indent = 2)
print(mycol.insert_many(products))





