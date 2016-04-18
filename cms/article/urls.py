from django.conf.urls import url, include
from article.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
