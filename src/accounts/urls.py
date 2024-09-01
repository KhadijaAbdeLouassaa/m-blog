from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'


urlpatterns = [
    # - section of profile
    path('profile/', views.user_profile, name='user-profile'),
    path('edit-profile/', views.edit_user_profile, name='edit-user-profile'),
    path('author/<slug>',views.author_profile, name = 'author-profile' ),
    
    
    # - secion of authentication
    path('sign-up/', views.sign_up, name='sign-up'),    
    path('log-in/', views.log_in, name='log-in'),  
    path('log-out/', auth_views.LogoutView.as_view(), name='log-out'),
    
    
    # - section of reset password
    path('reset-password/', views.reset_password, name='reset-password'),
    path('password-reset-sent/', views.password_reset_sent, name='password-reset-sent'),   
    path('password-reset-confirm/<token>/', views.password_reset_confirm, name='password-reset-confirm'),    
    path('password-reset-done/', views.password_reset_done, name='password-reset-done'),
    
    
]

