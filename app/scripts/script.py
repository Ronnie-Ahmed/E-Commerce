from app.models import Item,Category
import requests
from django.db import connection
from django.core.files import File
from django.conf import settings
import random
import os
def run():
    # url='https://dummyjson.com/products/1'
    # response=requests.get(url)
    # data=response.json()
    # for index,image in enumerate(data['images']):
    #     print(f"index: {index} value: {image}")
    
    # items=Item.objects.filter(price__gt=1).select_related('category')
    # print(items.query)
    
    
    # print(connection.queries)
    categories = Category.objects.all()

# Get a list of image file names from your media folder
    image_files = os.listdir(os.path.join(settings.MEDIA_ROOT, 'images'))

    for i in range(1, 30):
        # Select a random image file from the list
        random_category = random.choice(categories)
        random_image = random.choice(image_files)

        # Create a new Item with the selected image
        new_item = Item.objects.create(
            name="item" + str(i),
            price=10 + i,
            description="item" + str(i),
            category=random_category,
            image=random_image  # Assign the selected image file name
        )

        # You may want to open the image file and save it to the Item's image field
        with open(os.path.join(settings.MEDIA_ROOT, 'images', random_image), 'rb') as f:
            new_item.image.save(random_image, File(f))
        
    
    