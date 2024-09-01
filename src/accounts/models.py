from django.db import models
from django.utils.text import slugify
from posts.models import Post
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    user_image = models.ImageField(upload_to = "user_image", default="user_profile_images\default_image.png")
    posts_saved = models.ManyToManyField(Post, blank=True)
    slug = models.SlugField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super(UserProfile, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username
    
    
    
def create_profile(sender,**kargs):
    if kargs['created'] :
        UserProfile.objects.create(user=kargs['instance'])
        
        
post_save.connect(create_profile,sender=User)