from django.conf.urls import url, include
from .views import all_products
from .views import details

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^details/([0-9]+)', details, name='details')
]