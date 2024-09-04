from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=15)
        
    def __str__(self):
        return self.name
                
 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    body = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to = "post_images", null=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(null= True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args,**kwargs)
        
    
    def __str__(self):
        return self.title
    
    
    
    
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.commenter.username
     
    
    
