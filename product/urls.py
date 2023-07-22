from django.urls import *
from .views import *

app_name = 'product'


urlpatterns = [

    path('<int:pid>', products_details , name='products_details'),
    path('category/<str:cat>', product , name= 'product_with_category'),
]