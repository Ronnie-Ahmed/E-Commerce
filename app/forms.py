from django import forms
from .models import Buyer,Order,Category,Item,ItemImage
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms.widgets import PasswordInput,TextInput

class BuyerForm(forms.ModelForm):
    class Meta:
        model=Buyer
        fields='__all__'
        exclude=['user','dateJoined']
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model=Order
#         fields='__all__'
#         exclude=['user','dateOrdered']
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model=Category
#         fields='__all__'
#         exclude=['slug']
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model=Item
#         fields='__all__'
# class ItemImageForm(forms.ModelForm):


class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput)
    password=forms.CharField(widget=PasswordInput)