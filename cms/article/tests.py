from django.test import TestCase
from django.core.urlresolvers import reverse

from article.models import Article


class ArticleTest(TestCase):
    fixtures = ['all.json']

    def test_index(self):
        response = self.client.get(reverse('article:index'))
        # Is page reachable
        self.assertEqual(response.status_code, 200)
        # Is page context contains articles list with 5 elements
        self.assertEqual(len(response.context.get('articles', [])), 5)

        first_article = Article.objects.order_by('-id').first()
        # Test order
        first_article.is_published = True
        first_article.save()
        response = self.client.get(reverse('article:index'))
        self.assertIn(first_article, response.context.get('articles', []))

        # Test is_published
        first_article.is_published = False
        first_article.save()
        response = self.client.get(reverse('article:index'))
        self.assertNotIn(first_article, response.context.get('articles', []))
