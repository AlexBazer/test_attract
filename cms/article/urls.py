from django.conf.urls import url, include
from article.views import index, article, paginate

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^paginate/(?P<page>\d+)$', paginate, name='paginate'),
    url(r'^article/(?P<slug>[\w_-]+)/$', article, name='article')
]
