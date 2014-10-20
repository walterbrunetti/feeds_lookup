from django.conf.urls import url, include
from rest_framework import routers
from django_test.apps.feeds import views


router = routers.DefaultRouter()
router.register(r'feeds', views.FeedViewSet)
router.register(r'articles', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
