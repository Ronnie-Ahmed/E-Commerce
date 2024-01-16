from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .forms import CreateUser,LoginForm,BuyerForm
from .models import Buyer,Item,ItemImage,Order,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .utils import check_superuser

# Create your views here.

def home(request):
    
    if request.user.is_authenticated:
        user=request.user
    else:
        user=None
    
    context={
            'user':user
        }
    
   
        
    return render(request,'app/index.html',context)


def Login(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
    context={
        'form':form
    }
    return render(request,'app/login.html',context)

def SignUp(request):
    if request.method=='POST':
        form=CreateUser(request.POST)
        
        if form.is_valid():
            current_user=form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form=CreateUser()
        
    context={
        'form':form
    }
    return render(request,'app/signup.html',context)
    

def Log_out(request):
    logout(request)
    return redirect('home')


def UserProfile(request):
    return render(request,'app/userprofile.html')


@check_superuser
def superuser(request):
    return HttpResponse("Valid")