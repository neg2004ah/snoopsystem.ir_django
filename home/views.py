from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from product.models import *
from django.contrib import  messages
from django.utils import timezone





def home(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        products = Product.objects.all()
        category = Category.objects.all()
    
    
        context = {
            "questions": questions,
            'products' : products,
            'category' : category,
        }
        
        return render(request,"home/index.html",context=context)
    
    elif request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'The Email is not valid !')
            
            

def contact(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')
    
    elif request.method == 'POST':
        form_contact = ContactUsForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect('/')




