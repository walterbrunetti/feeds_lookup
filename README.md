django_test
===========

##This project is an experimentation using django, elasticsearch and backbone.



http://pixabay.com/en/blog/posts/django-search-with-elasticsearch-47/

http://elasticsearch-py.readthedocs.org/en/master/

http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/

```
import json, requests
from my_project.blog.models import BlogPost

data = ''
for p in BlogPost.objects.all():
    data += '{"index": {"_id": "%s"}}\n' % p.pk
    data += json.dumps({
        "title": p.title,
        "description": p.description,
        "content": p.content
    })+'\n'
response = requests.put('http://127.0.0.1:9200/my_index/blog/_bulk', data=data)
print response.text
```

```
data = {
    "query": {
        "query_string": { "query": "hello world" }
    }
}
response = requests.post('http://127.0.0.1:9200/my_index/blog/_search', data=json.dumps(data))
print response.json()

```
