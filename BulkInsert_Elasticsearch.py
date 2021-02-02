import requests, json, os
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch([{'host': 'localhost.localdomain', 'port': 9200}])
r = requests.get('http://localhost.localdomain:9200')
with open("netflows.json") as json_file:
        body=json_file.readlines()
        helpers.bulk(es, actions=body, index='netflows', doc_type='docs')
