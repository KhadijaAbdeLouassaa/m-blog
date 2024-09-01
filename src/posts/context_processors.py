from .models import Category

# add your context processor here

def category(request):
    
    categories = Category.objects.all()
    return {'categories':categories}
    
    
    
