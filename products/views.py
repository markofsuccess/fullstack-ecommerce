from django.shortcuts import render
from .models import Product
from .models import product_details

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def details(request, id):
    details = product_details.objects.filter(product_id = id)
    product= Product.objects.get(id=id)
    return render(request, "product_details.html", {'details': details, 'product': product})