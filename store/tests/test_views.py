# from django.test import TestCase
from unittest import skip
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product
from store.views import product_all

@skip("demonstarting skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        """
        Test category response status
        """
        response= self.c.get(
            reverse('store:category_list', args=['django'])
        )
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse('store:product_detail', args=['the-road-to-react'])
        )
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startsWith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """
        Example: Using request factory
        """
        request= self.factory.get('/the-temple-of-django-database-performance')
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>BookStore </title>', html)
        self.assertTrue(html.startsWith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)