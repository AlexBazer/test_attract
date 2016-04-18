from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage

from article.models import Article


def peginate_articles(page):
    """Paginate through articles"""
    articles = Article.objects\
        .filter(is_published=True)\
        .order_by('-id')

    paginator = Paginator(articles, settings.ARTICLES_PER_PAGE)
    try:
        articles = paginator.page(int(page))
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return articles


@require_GET
def index(request):
    """View for main page"""
    articles = peginate_articles(1)

    return render(
        request,
        'article/index.html',
        {'articles': articles}
    )


@require_GET
def paginate(request, page):
    """Paginate views"""
    articles = peginate_articles(page)
    return render(request, 'article/articles_list.html', {
        'articles': articles
    })


@require_GET
def article(request, slug):
    """Article view"""
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'article/article.html', {
        'article': article
    })
