from django.conf.urls import url, include
from rest_framework import routers
from feeds_lookup.apps.feeds import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'feeds', views.FeedViewSet)
router.register(r'articles', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('^api/articles/api-search/(?P<title>.+)$', views.ArticleApiSearch.as_view()),  # had to remove the trailing_slash
    url(r'^api/articles/search/$', views.ArticleSearch.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

