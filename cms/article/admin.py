from django.contrib import admin
from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title', )
    }
    list_display = ('title', 'is_published')
