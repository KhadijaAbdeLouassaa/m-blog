from .models import UserProfile

# add your context processor here
  
    
def user_profile_image(request):
    if request.user.is_authenticated :
        get_user,created = UserProfile.objects.get_or_create(user=request.user)
    
        return {'image':get_user}
        
    return {}
    