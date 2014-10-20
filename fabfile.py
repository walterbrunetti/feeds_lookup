from datetime import datetime
from fabric.api import local
from elasticsearch import Elasticsearch


def prepare_deployment(branch_name):
    local('python manage.py test django_project')
    local('git add -p && git commit')


def import_feeds():
    print "Importing Feeds"


def index_feeds():
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
    
