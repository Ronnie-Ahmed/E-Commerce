from django.test import TestCase,Client
from .models import Buyer,Category,Item,Order,ItemImage,CartItem
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.hashers import make_password,mask_hash
from django.urls import reverse
# Create your tests here.

class TestModel(TestCase):
    def setUp(self):
        try:
            self.user = User.objects.create_user(username='ronnie', password='ronnie')
            self.buyer = Buyer.objects.create(name='Ronnie', email='rksraisul@gmail.com', user=self.user)
            self.category = Category.objects.create(name="Anime", slug="Anime", description="This is the anime Category")
            self.item = Item.objects.create(name="Item1", price=2.2, description="This is Item1", category=self.category)
            self.item_image = ItemImage.objects.create(item=self.item, image_url='images/40718.jpg')
            self.order = Order.objects.create(buyer=self.buyer, item=self.item,  delivery_date=timezone.now(), howmany=2)
            self.cart_item = CartItem.objects.create(buyer=self.buyer, item=self.item, quantity=3)
            # self.order = Order.objects.create(buyer=self.buyer, item=self.item)

        except Exception as e:
            self.fail(e)

    def test_instances(self):
        try:
            self.assertTrue(isinstance(self.user,User))
            self.assertTrue(isinstance(self.buyer,Buyer))
            self.assertTrue(isinstance(self.category,Category))
            self.assertTrue(isinstance(self.item,Item))
            self.assertTrue(isinstance(self.item_image,ItemImage))
            self.assertTrue(isinstance(self.order,Order))
            self.assertTrue(isinstance(self.cart_item,CartItem))
            self.assertTrue(str(self.buyer),"Ronnie")
            self.assertTrue(str(self.category),"Anime")
            self.assertTrue(str(self.item),"Item1")
            self.assertTrue(str(self.order),f"Item= {self.item.name}  By= {self.buyer}")
            self.assertTrue(str(self.item_image),self.item.name)
            self.assertTrue(str(self.cart_item),f"{self.buyer} - {self.item} - Quantity: {self.cart_item.quantity}")
        except Exception as e:
            self.fail(e)
    def test_user(self):
        try:
            self.assertEqual(self.user.username,"ronnie")
            self.assertTrue(self.user.check_password("ronnie"))
            # self.assertEqual(self.user.password,make_password("ronnie"))
            # print(make_password("ronnie"))
        except Exception as e:
            self.fail(e)
            
    def test_buyer(self):
        try:
            self.assertEqual(self.buyer.name,"Ronnie")
            self.assertEqual(self.buyer.email,"rksraisul@gmail.com")
            self.assertEqual(self.buyer.user,self.user)
        except Exception as e:
            self.fail(e)
    def test_order(self):
        try:
            self.assertEqual(self.order.buyer,self.buyer)
            self.assertEqual(self.order.item,self.item)
            # self.assertEqual(self.order.delivery_date,timezone.now())
            self.assertEqual(self.order.howmany,2)
        except Exception as e:
            self.fail(e)
            
class TestViews(TestCase):
    def setUp(self):
        try:
            
            self.client=Client()
            self.index_url=reverse("home")
            self.login_url=reverse("Login")
            self.signup_url=reverse("SignUp")
            self.user = User.objects.create_user(username='rony', password='rony')            
            self.superuser=User.objects.create_superuser(username="ronnie",password="ronnie")
            self.buyer = Buyer.objects.create(name='rony', email='rksraisul@gmail.com', user=self.user)
            self.userprofile=reverse("UserProfile")
            self.superuser_url=reverse("superuser")
            # item=Item.objects.first()
            # self.viewitem_pk=item.id
            # self.viewitem_url=reverse("viewitem",args=[self.viewitem_pk])
        except Exception as e:
            self.fail(e)
        
        
    def test_home(self):
        response=self.client.get(self.index_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"app/index.html")
        
    def test_login(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"app/login.html")
        
    def test_viewitem(self):
        # response=self.client.get(self.viewitem_url)
        # print(response)
        pass
        
    def test_userprofile(self):
        try: 
            self.client.login(username="rony",password="rony")
            response=self.client.get(self.userprofile)
            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response,"app/userprofile.html")
        except Exception as e:
            self.fail(e)
    def test_not_userprofile(self):
        try:
            self.client.login(username="rony",password="rony")
            self.client.logout()
            response=self.client.get(self.userprofile)
            self.assertNotEqual(response.status_code,200)
            self.assertTemplateNotUsed(response,"app/userprofile.html")
        except Exception as e:
            self.fail(e)
    
    def test_super_user(self):
        try: 
            self.client.login(username="ronnie",password="ronnie")
            response=self.client.get(self.superuser_url)
            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response,"app/superuser.html")
        except Exception as e:
            self.fail(e)
    def test_Not_super_user(self):
        try: 
            self.client.login(username="ronnie",password="ronnie")
            self.client.logout()
            response=self.client.get(self.superuser_url)
            self.assertNotEqual(response.status_code,200)
            self.assertTemplateNotUsed(response,"app/superuser.html")
        except Exception as e:
            self.fail(e)
            
class TestHomeView(TestCase):
    def setUp(self):
        self.client=Client()
        self.index_url=reverse("home")
        self.user=User.objects.create_user(username="ronnie",password="ronnie")
        self.category = Category.objects.create(name="Anime", slug="Anime", description="This is the anime Category")
        self.category2 = Category.objects.create(name="Tech", slug="Tech", description="This is the anime Category")
        self.buyer = Buyer.objects.create(name='Ronnie', email='rksraisul@gmail.com', user=self.user)
        self.item1 = Item.objects.create(name="Item1", price=2.2, description="This is Item1", category=self.category)
        self.item2 = Item.objects.create(name="Item2", price=2.2, description="This is Item1", category=self.category)
        self.item3 = Item.objects.create(name="Item3", price=2.2, description="This is Item1", category=self.category)
        self.item4 = Item.objects.create(name="Item4", price=2.2, description="This is Item1", category=self.category2)
        self.item_image1 = ItemImage.objects.create(item=self.item1, image_url='images/40718.jpg')
        self.item_image2= ItemImage.objects.create(item=self.item2, image_url='images/40718.jpg')
        self.item_image3 = ItemImage.objects.create(item=self.item3, image_url='images/40718.jpg')
        self.item_image4 = ItemImage.objects.create(item=self.item4, image_url='images/40718.jpg')


    def test1(self):
        self.client.login(username="ronnie",password="ronnie")
        self.assertEqual(self.item1.name,"Item1")
        response=self.client.post(self.index_url,data={'addtocart':self.item1.id})
        self.assertEqual(response.status_code,302)
    
    def test_category(self):
        try: 
            self.client.login(username="ronnie",password="ronnie")
            response=self.client.get(self.index_url)
        except Exception as e:
            self.fail(e)
        # self.assertEqual(response.status_code,200)
        # items=response.context['items']
        # self.assertIn(self.item1,items)
        