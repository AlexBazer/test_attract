from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    """Article model"""
    title = models.CharField(_('Article title'), max_length=250)
    slug = models.SlugField(_('Article slug'), max_length=250)
    image = models.ImageField(_('Article image'), upload_to='article')
    content = models.TextField(_('Article content text'))
    is_published = models.BooleanField(_('Article is published'), default=False)
