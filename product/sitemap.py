from django.urls import reverse
from django.contrib import sitemaps
from .models import *




class DynamicSiteMaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Product.objects.all().order_by('created_date')
    
    def location(self, obj):
        return '/product/products_details/%s' %obj.id