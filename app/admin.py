from django.contrib import admin
from .models import Category, Item, ItemImage,Buyer,Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Buyer)
admin.site.register(Order)
