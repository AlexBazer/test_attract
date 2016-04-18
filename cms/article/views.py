from django.shortcuts import render
from django.views.decorators.http import require_GET

from article.models import Article

@require_GET
def index(request):
    """View for main page"""

    articles = Article.objects.all()[0:5]
    return render(
        request,
        'article/index.html',
        {'articles': articles}
    )
