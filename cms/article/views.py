from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from article.models import Article


@require_GET
def index(request):
    """View for main page"""

    articles = Article.objects\
        .filter(is_published=True).order_by('-id')[0:settings.ARTICLES_PER_PAGE]
    return render(
        request,
        'article/index.html',
        {'articles': articles}
    )


@require_GET
def paginate(request, page):
    offset = settings.ARTICLES_PER_PAGE * int(page)
    to = offset + settings.ARTICLES_PER_PAGE
    articles = Article.objects\
        .filter(is_published=True)\
        .order_by('-id')[offset:to]

    return render(request, 'article/articles_list.html', {
        'articles': articles
    })


@require_GET
def article(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'article/article.html', {
        'article': article
    })
