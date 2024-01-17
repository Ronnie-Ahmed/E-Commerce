from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        



class Buyer(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    profile_pic=models.ImageField(upload_to='images/',null=True,blank=True)
    descriptions=models.TextField(max_length=500,blank=True,null=True)
    dateJoined=models.DateField(blank=True,null=True)
    cart = models.ManyToManyField('Item', through='CartItem')

    
    def save(self,*args,**kwargs):
        if not self.dateJoined:
            self.dateJoined=timezone.now() + timezone.timedelta(hours=6)
        super().save(*args,**kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Buyers'
        
  

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Items'
     
    
class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.item.name
    
    class Meta:
        verbose_name_plural = 'Item Images'
    
      
class Order(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    odered_at=models.DateField(blank=True,null=True)
    delivery_date=models.DateField(null=True)
    howmany=models.IntegerField(null=True)
    totalcolst=models.FloatField(blank=True,null=True)
    
    
    def calculateprice(self):
        return self.item.price * self.howmany
    
    def save(self,*args,**kwargs):
        if not self.odered_at:
            self.odered_at=timezone.now() + timezone.timedelta(hours=6)
        
        self.totalcolst=self.calculateprice()   
        super().save(*args,**kwargs)
        
    def __str__(self):
        return f"Item= {self.item.name}  By= {self.buyer}"
    
    class Meta:
        verbose_name_plural='Order'
    
    
class CartItem(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.buyer} - {self.item} - Quantity: {self.quantity}"