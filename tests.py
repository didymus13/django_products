"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

class ProductCategoryTest(TestCase):
    
    def testProductCategoryProperties(self):
        pc = ProductCategory()
        pc.name = 'test category'
        pc.prefix = 'TST'
        pc.save()

        pc2 = ProductCategory.objects.get(pk=pc.id)
        self.assertEquals(pc.name, pc2.name)
        self.assertEquals(pc.prefix, pc2.prefix)

class ProductTest (TestCase):
    def testProductProperties(self):
        pc = ProductCategory()
        pc.name = 'test category'
        pc.prefix = 'TST'
        pc.save()

        p = Product()
        p.category = pc
        p.suffix = '0010'
        p.name = 'test product'
        p.cost = 20
        p.price = 40
        p.isTaxable = True
        p.save()

        p2 = Product.objects.get(pk=p.id)
        self.assertEquals(p.suffix, p2.suffix)
        self.assertEquals(p.name, p2.name)
        self.assertEquals(p.cost, p2.cost)
        self.assertEquals(p.price, p2.price)
        self.assertEquals(p.isTaxable, p2.isTaxable)
        self.assertEquals(p.category, p.category)
        self.assertEquals("%s%s" % (pc.prefix, p.suffix), p2.productCode)

        self.assertEquals(1, pc.product_set.count())
        for product in pc.product_set.all():
            self.assertEquals(p.name, product.name)
