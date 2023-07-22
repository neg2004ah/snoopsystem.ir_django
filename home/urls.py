from django.urls import *
from .views import *

app_name = 'home'


urlpatterns = [
    path('',home,name = 'home'),
    path('contact',contact,name = 'contact'),
]