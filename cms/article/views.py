from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    """View for main page"""
    return render(request, 'article/index.html')
