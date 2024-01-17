from django.test import TestCase,Client
from .models import Buyer,Category,Item,Order
from django.contrib.auth.models import User
# Create your tests here.

class TestModel(TestCase):
    def test_1(self):
        try:
            # emails=input('Enter your email: ')
            user=User.objects.create_user(username='ronnie',password='ronnie')
            buyer=Buyer.objects.create(name='Ronnie',email='rksraisul@gmail.com',user=user)
            self.assertEqual(str(buyer),'Ronnie')
            self.assertEqual(buyer.email,"rksraisul@gmail.com")
            self.assertTrue(isinstance(buyer,User))
        except Exception as e:
            self.fail(e)

