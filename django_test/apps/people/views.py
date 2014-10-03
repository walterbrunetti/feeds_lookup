from django.shortcuts import render

from datetime import datetime
from elasticsearch import Elasticsearch

def test_elasticsearch():
	es = Elasticsearch()

	doc = {
	    'author': 'kimchy',
	    'text': 'Elasticsearch: cool. bonsai cool.',
	    'timestamp': datetime(2010, 10, 10, 10, 10, 10)
	}
	res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
	print(res['created'])

	res = es.get(index="test-index", doc_type='tweet', id=1)
	print(res['_source'])

	es.indices.refresh(index="test-index")

	res = es.search(index="test-index", body={"query": {"match_all": {}}})
	print("Got %d Hits:" % res['hits']['total'])
	for hit in res['hits']['hits']:
	    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
