from app.models import Item
import requests
from django.db import connection

def run():
    # url='https://dummyjson.com/products/1'
    # response=requests.get(url)
    # data=response.json()
    # for index,image in enumerate(data['images']):
    #     print(f"index: {index} value: {image}")
    
    items=Item.objects.filter(price__gt=1).select_related('category')
    print(items.query)
    
    # print(connection.queries)
        
    
    
    