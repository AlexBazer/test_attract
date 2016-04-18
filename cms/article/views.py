from django.shortcuts import render
from django.views.decorators.http import require_GET

from article.models import Article


@require_GET
def index(request):
    """View for main page"""

    articles = Article.objects.filter(is_published=True).order_by('-id')[0:5]
    return render(
        request,
        'article/index.html',
        {'articles': articles}
    )


@require_GET
def article(request, slug):
    return render(request, 'article/article.html')
