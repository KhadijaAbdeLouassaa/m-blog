from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required 
from .models import UserProfile
from .forms import UserProfileForm
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .email_fct import send_email_fct

# Create your views here.

# - section of authentication 

def sign_up(request):
    if request.method == "POST" :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username and email and password1 and password2 :
            if User.objects.filter(username= username).exists():
                messages.add_message(request,messages.ERROR, "this username already token")
            else :
                if User.objects.filter(email= email).exists():
                    messages.add_message(request,messages.ERROR, "this email already token")
                else :               
                    if password1 == password2 :                   
                        if len(password2) >= 8: 
                            user = User.objects.create_user(username = username, password = password2, email = email)
                            user.save()
                            messages.add_message(request,messages.ERROR, f"welcome {user.username}, your account has been seccessfly created")
                            backend = 'django.contrib.auth.backends.ModelBackend'
                            login(request,user,backend=backend)
                            return redirect("/")
                        else :
                            messages.add_message(request,messages.ERROR, "Your password must contain at least 8 characters")
                    else :
                        messages.add_message(request,messages.ERROR, "passwords must be same")
                
        else :
            messages.add_message(request,messages.ERROR, "please fill all")
            
   
    return render(request, "accounts/registration/signup.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username and password :
            user = authenticate(username = username, password = password)
            if user is not None:                
                backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user,backend=backend)
                messages.add_message(request,messages.ERROR, f"welcome back {user.username}")
                return redirect("/")
            else :                
                messages.add_message(request,messages.ERROR, "password or username does not correct")
        else :
            messages.add_message(request,messages.ERROR, "please fill all")
      
    return render(request,"accounts/registration/login.html")

def reset_password(request):
    if request.method == "POST":
        email = request.POST['email']
        if email :
            if User.objects.filter(email=email).exists() :
                token = str(uuid.uuid4())
                send_email_fct(email,token)
                return redirect("accounts:password-reset-sent")
            
            else :
                messages.add_message(request,messages.ERROR, "this email does not exist")
        
        
        else :
            messages.add_message(request,messages.ERROR, "please enter your email")
    
    return render(request, "accounts/registration/reset_password.html")

def password_reset_sent(request):
    return render(request,"accounts/registration/password_reset_sent.html")

def password_reset_confirm(request,token):
    if request.method == "POST" :
        username = request.POST['username']
        new_password = request.POST['new_password']
        new_password_confirm = request.POST['new_password_confirm']
        
        if username and new_password and new_password_confirm :
            if new_password == new_password_confirm :
                if len(new_password_confirm) >= 8: 
                    user = User.objects.get(username = username)            
                    user.set_password(new_password)
                    user.save()
                    return redirect("accounts:password-reset-done")
                else :
                    messages.add_message(request,messages.ERROR, "Your password must contain at least 8 characters")
                
            else :               
                messages.add_message(request,messages.ERROR, "passwords are not the same")
           
        else :            
            messages.add_message(request,messages.ERROR, "please fell all")
   
    return render(request,"accounts/registration/password_reset_confirm.html")

def password_reset_done(request):
    return render(request,"accounts/registration/password_reset_done.html")



# - section of user profile
@login_required
def user_profile(request):
    user = UserProfile.objects.filter(user=request.user)
    user_posts = Post.objects.filter(author=request.user)
        
    return render(request,"accounts/profile.html",{'user':user,'user_posts':user_posts})
   
def edit_user_profile(request):
    if request.method == 'POST' :
        user_form = UserProfileForm(request.POST, request.FILES,instance=request.user.userprofile)
        if user_form.is_valid():
            user_form.save()
            return redirect("accounts:user-profile")
            
    else :
        user_form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request,"accounts/edit_user_profile.html",{'form':user_form})   
    
  
  
# - section of author profile
def author_profile(request,slug):
    
    author = UserProfile.objects.get(slug=slug)
    author_posts = Post.objects.filter(author=author.user)
  
    return render(request,"accounts/author.html",{'author':author,'author_posts':author_posts,})

