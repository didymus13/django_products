from django.contrib import admin
from models import *

class ProductCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
