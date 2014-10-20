from django.shortcuts import render

from models import Feed, Article
from rest_framework import viewsets
from django_test.apps.feeds.serializers import FeedSerializer, ArticleSerializer


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
