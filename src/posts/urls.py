from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [

    # - section of post 
    path('',views.PostListView.as_view(), name = 'post-list' ),
    path('post-detail/<slug>/',views.post_detail, name = 'post-detail' ),
    path('create/',views.CreatePostView.as_view(), name = 'create-post' ),
    path('delete/<slug>/',views.DeletePostView.as_view(), name = 'delete-post' ),
   
    # - section of posts saved
    path('save-post/<slug>/',views.save_post, name = 'save-post' ),
    path('posts-saved',views.posts_saved, name = 'posts-saved' ),
    path('delete-post-saved/<slug>/',views.delete_post_saved, name = 'dalete-post-saved' ),
    
    # - section of search & categories
    path('search/',views.PostSearchView.as_view(), name = 'post-search' ),
    path('categories/<str:name>/',views.categories, name = 'categories' ),
    
    # - section of comment 
    path('add-comment/<slug>/',views.add_comment, name = 'add-comment' ),
    path('delete-comment/<int:pk>/',views.delete_comment, name = 'delete-comment' ),
]
