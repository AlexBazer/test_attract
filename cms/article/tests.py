from django.test import TestCase
from django.core.urlresolvers import reverse


class ArticleTest(TestCase):
    fixures = ['fixures.json']

    def test_index(self):
        response = self.client.get(reverse('article:index'))
        # Is page reachable
        self.assertEqual(response.status_code, 200)
        # Is page context contains articles list with 5 elements
        self.assertEqual(len(response.context.get('articles', [])), 5)
