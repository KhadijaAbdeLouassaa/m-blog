from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import CreatePostForm
from .models import Post,Category,Comment
from accounts.models import UserProfile
from django.views.generic import ListView,CreateView, DeleteView 
# Create your views here.

# - section of post   
class PostListView(ListView):
    model = Post
    template_name = "posts\post.html"
        
def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    related_posts = Post.objects.filter(category=post.category)
    return render(request,"posts\post_detail.html",{'post':post,'related_posts':related_posts})
    
class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = "posts\create_post.html"
    success_url = "/"
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)   
  
class DeletePostView(DeleteView):
    model = Post
    template_name = "posts\post_confirm_delete.html"
    success_url = "/"
 
 
# - section of search
class PostSearchView(ListView):
    model = Post
    template_name = 'posts/post_search.html' 
    context_object_name = 'posts'

    def get_queryset(self):       
        query = self.request.GET.get('query')
        if query:
            return Post.objects.filter(Q(title__icontains=query)|
                                        Q(body__icontains=query)|
                                        Q(author__username__icontains=query)
                                        ) 


# - section of categories
def categories(request,name):
    category = Category.objects.get(name= name)
    posts = Post.objects.filter(category=category)
    return render(request,"posts\categories.html",{'posts':posts})
  
  
# - section of posts saved  
@login_required  
def save_post(request,slug):
    post = Post.objects.get(slug=slug)
    user = UserProfile.objects.get(user=request.user)
    user.posts_saved.add(post)
    return redirect("/")

def posts_saved(request):
    user = UserProfile.objects.get(user=request.user)
    posts = user.posts_saved.all()
    return render(request,"posts\posts_saved.html",{'posts':posts})
    
def delete_post_saved(request,slug):
    post = Post.objects.get(slug=slug)
    user = UserProfile.objects.get(user = request.user)
    user.posts_saved.remove(post)  
    return redirect("posts:posts-saved")
 
 
# - section of comments
@login_required
def add_comment(request,slug):
    post =  Post.objects.get(slug=slug)
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment :
            Comment.objects.create(commenter=request.user, comment=comment,post=post)
    return redirect('posts:post-detail', slug=post.slug)     
   
def delete_comment(request,pk):
    comment = Comment.objects.get(commenter=request.user,pk=pk)
    comment_pk = comment.post.slug
    comment.delete()
    return redirect("posts:post-detail",slug=comment_pk)
    
