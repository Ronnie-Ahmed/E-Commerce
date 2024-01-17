from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .forms import  CreateUser,LoginForm,BuyerForm,CategoryForm,ItemForm,OrderForm
from .models import Buyer,Item,ItemImage,Order,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .utils import check_superuser
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    category=request.GET.get('category')
    categories=Category.objects.all()
    
    if category is not None:
        items=Item.objects.filter(category__name__iexact=category)
    else:
        items=Item.objects.all()
        
    if request.method=='POST' and request.user.is_authenticated:
        user=request.user
        if 'addtocart' in request.POST:
            item_id = request.POST.get('addtocart')
            item = Item.objects.get(id=item_id)
            buyer, created = Buyer.objects.get_or_create(user=request.user)
            buyer.cart.add(item)
            return redirect('home')
    else:
        None
    
    
  
    
    context={
            'user':request.user,
            'items':items,
            'categories':categories
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
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            Buyer.objects.create(name=username,email=email,user=current_user)
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
    buyer=Buyer.objects.get(user=request.user)
    if request.method=='POST':
        if "pic" in request.POST:
            imagefile=request.FILES.get('profile_pic')
            buyer.profile_pic=imagefile
            buyer.save()
        
    context={
        'buyer':buyer
    }
    
    return render(request,'app/userprofile.html',context)


@check_superuser
def superuser(request):
    if request.method=='POST':
        if 'item_submit' in request.POST:
            form_item=ItemForm(request.POST,request.FILES)
            images = request.FILES.getlist('image_url')
            if form_item.is_valid():  
                item=form_item.save()  
            for image in images:
                ItemImage.objects.create(item=item,image_url=image)
                
            return redirect('home')
        if 'category_submit' in request.POST:
            form_category=CategoryForm(request.POST)
            if form_category.is_valid():
                form_category.save()
                return redirect('home')
    else:
        formitem=ItemForm()
        formcategory=CategoryForm
        
    context={
        'formitem':formitem,
        'formcategory':formcategory
    }
    
    return render(request,'app/superuser.html',context)


def viewitem(request,pk):
    item=Item.objects.get(id=pk)
    images=ItemImage.objects.filter(item=item.id)
    context={
        'item':item,
        'images':images
    }
    return render(request,'app/viewitem.html',context)

