from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import select_template
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from feeds_lookup.apps.feeds.serializers import FeedSerializer, ArticleSerializer
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


class ArticleApiSearch(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Article.objects.filter(title__icontains=title)


class ArticleSearch(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        articles = [article.title for article in Article.objects.all()]
        return Response(articles)

