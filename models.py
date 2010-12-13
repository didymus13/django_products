from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length = 128)
    prefix = models.CharField(max_length = 3)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'product categories'

class Product(models.Model):
    name = models.CharField(max_length = 128)
    suffix = models.CharField(max_length = 5)
    category = models.ForeignKey(ProductCategory)
    cost = models.DecimalField(decimal_places = 2, max_digits=10)
    price = models.DecimalField(decimal_places = 2, max_digits=10)
    isTaxable = models.BooleanField()

    def _makeProductCode(self):
        return "%s%s" % (self.category.prefix, self.suffix)
    productCode = property(_makeProductCode)

    def __unicode__(self):
        return self.name

