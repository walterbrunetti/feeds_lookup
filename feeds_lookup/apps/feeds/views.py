from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import select_template
from rest_framework import viewsets
from django_test.apps.feeds.serializers import FeedSerializer, ArticleSerializer
from models import Feed, Article




def index(request):
    context = {
        'app' : 'empty_for_now'
    }
    t = select_template(['index.html'])
    return HttpResponse(t.render(RequestContext(request, context)))


class FeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Feed to be viewed or edited.
    """
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Article to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
