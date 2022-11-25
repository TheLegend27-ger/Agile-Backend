import requests
import json

from bs4 import BeautifulSoup

url = "https://5f5e3147-f7a0-4ef3-a058-afe7524160d7.mock.pstmn.io/"
headers = {'Authorization' : 'Bearer 48a3eac8c7842e3eaf9dfba48631a4b38df1aa24589841abde4740c1d0e5c890fe6cd551a0ff0be17a2ef8b6ee6dc3efd12bd8c004b47ad1fc59e8a971738057a0509655d1933f99c5ce92726b754639a0a564806c9b4bbba6cda4abc41b46a525a62300c63e50975ae80550d918eb44fb2886b699f526023b2df01dd5a32c06', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

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

r = requests.post(url, data=json_data, headers=headers)
print(r)