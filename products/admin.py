from django.contrib import admin
from .models import Product
from .models import product_image

# Register your models here.
admin.site.register(Product)
admin.site.register(product_image)