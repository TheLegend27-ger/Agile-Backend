import datetime
import logging
import azure.functions as func
import requests
import json
import pymongo 
from bs4 import BeautifulSoup

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()


    #Create connection String
    client = pymongo.MongoClient("mongodb+srv://Cluster2User:gPId3Gm4a0I9icN5@agile2cluster.bxvcw4l.mongodb.net/?retryWrites=true&w=majority",tls=True, tlsAllowInvalidCertificates=True)
    
    #Create DataBase if not already there
    mydb = client["Test"]
    #Create collection
    mycol = mydb["CollectionTest"]
    #Delete all entries in Collection
    mycol.drop()

    #Get HTML/XML page from web
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
    mycol.insert_many(products)


    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
