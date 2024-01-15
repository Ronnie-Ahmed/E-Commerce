from django import forms
from .models import Buyer,Order,Category,Item,ItemImage
from django.contrib.auth.models import User

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