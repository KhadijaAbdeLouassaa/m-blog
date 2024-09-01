from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta :
        model = UserProfile
        fields = ('bio', 'user_image')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'user_image':  forms.FileInput(attrs={'class': 'form-control-file'}),
        
       }
       
       

