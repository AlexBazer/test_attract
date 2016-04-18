from django.test import TestCase
from django.core.urlresolvers import reverse


class ArticleTest(TestCase):
    fixures = ['fixures.json']

    def test_index(self):
        response = self.client.get(reverse('article:index'))
        self.assertEqual(response.status_code, 200)
