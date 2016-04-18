from django.conf.urls import url, include
from article.views import index, article, peginate

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^peginate/(?P<page>\d+)$', peginate, name='peginate'),
    url(r'^article/(?P<slug>[\w_-]+)/$', article, name='article')
]
