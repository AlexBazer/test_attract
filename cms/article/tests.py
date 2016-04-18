from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from article.models import Article


class ArticleTest(TestCase):
    fixtures = ['all.json']

    def test_index(self):
        response = self.client.get(reverse('article:index'))
        # Is page reachable
        self.assertEqual(response.status_code, 200)
        # Is page context contains articles list with 5 elements
        articles_count = Article.objects.filter(is_published=True).count()
        self.assertEqual(len(response.context['articles']), articles_count)

        first_article = Article.objects.order_by('-id').first()
        # Test order
        first_article.is_published = True
        first_article.save()
        response = self.client.get(reverse('article:index'))
        self.assertIn(first_article, response.context['articles'])

        # Test is_published
        first_article.is_published = False
        first_article.save()
        response = self.client.get(reverse('article:index'))
        self.assertNotIn(first_article, response.context['articles'])

    def test_article_pagination(self):
        page = 1
        # Get next 5 articles
        response = self.client.get(reverse('article:paginate', kwargs={'page': page}))

        # Is page reachable
        self.assertEqual(response.status_code, 200)

        # Is next 5 elements can be getted
        offset = settings.ARTICLES_PER_PAGE * page
        to = offset + settings.ARTICLES_PER_PAGE
        articles = Article.objects\
            .filter(is_published=True)\
            .order_by('-id')[offset: to]
        [self.assertIn(article, response.context['articles']) for article in articles]

    def test_article(self):
        first_article = Article.objects.order_by('-id').first()
        first_article.is_published = True
        first_article.save()

        # Article page reachable
        response = self.client.get(
            reverse('article:article', kwargs={'slug': first_article.slug})
        )
        self.assertEqual(response.status_code, 200)

        # Article page have correct article object
        self.assertEqual(response.context['article'], first_article)

        # Article with is_published=False has to git 404 page
        first_article.is_published = False
        first_article.save()
        response = self.client.get(
            reverse('article:article', kwargs={'slug': first_article.slug})
        )
        self.assertEqual(response.status_code, 404)
