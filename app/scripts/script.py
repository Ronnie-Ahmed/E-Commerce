from app.models import Item
def run():
    items=Item.objects.all()
    for item in items:
        print(item.id)
    
    