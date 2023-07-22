from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length= 255) 
    client = models.CharField(max_length= 255)
    published_date = models.DateField()
    content = models.TextField()
    image1 = models.ImageField(upload_to='product',default='default.jpg')
    image2 = models.ImageField(upload_to='product',default='default.jpg')
    image3 = models.ImageField(upload_to='product',default='default.jpg')
    category = models.ManyToManyField(Category)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created_date',)
