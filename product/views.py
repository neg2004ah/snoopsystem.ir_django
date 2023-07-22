from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from home.models import *

def product(request, cat=None):
    products = Product.objects.all()
    questions = Question.objects.all()
    
    if cat:
        products = Product.objects.filter(category__name=cat)
        category = Category.objects.all()
        
        context = {
        'products': products,
        'category' : category,
        'questions' : questions,
                 }

        return render(request,'home/index.html',context=context)



def products_details(request,pid):
      
    products = Product.objects.get(id=pid)
    products.save()

    context = {
        'products': products,
        }
    
    return render(request, 'product/portfolio-details.html', context=context)

