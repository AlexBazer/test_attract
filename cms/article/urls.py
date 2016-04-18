from django.conf.urls import url, include
from article.views import index, article

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/(?P<slug>[\w_-]+)/$', article, name='article')
]
