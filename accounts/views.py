from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm,CaptchaForm
from .models import CustomUser

def Login(request) :
    if request.user.is_authenticated:
        return redirect('/')
    
    elif request.method == 'GET':
        form = AuthenticationForm()
        captcha = CaptchaForm()
        return render(request, 'registration/login.html', {'form': form, 'captcha': captcha})

    elif request.method == 'POST':
        captcha = CaptchaForm(request.POST)
        
        if captcha.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if '@' in username:
                try:
                    user = CustomUser.objects.get(email=username)
                    username = user.username

                except CustomUser.DoesNotExist:
                    messages.add_message(request, messages.ERROR , "کاربری با این ایمیل / نام کاربری یافت نشد")
                    return redirect('accounts:login')
                
                
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            
            else :
                messages.add_message(request, messages.ERROR , 'رمز عبور یا نام کاربری اشتباه می باشد')
                return redirect('accounts:login')
        else : 
            messages.add_message(request, messages.ERROR , 'تصویر مقابل به نادرستی وارد شده .')
            return redirect('accounts:login')
    else:
        messages.add_message(request, messages.ERROR , 'حسابی وجود ندارد.ابتدا ثبت نام کنید .')
        return redirect('accounts:login')

@login_required
def Logout(request) :
    logout(request)
    return redirect('/')



def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    elif request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else :
            messages.add_message(request, messages.ERROR , 'مقادیر وارد شده نادرست است.')
            return redirect('accounts:signup')
    
    