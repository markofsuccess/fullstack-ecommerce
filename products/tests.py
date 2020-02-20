from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Defining the tests that runs against the
    Product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')