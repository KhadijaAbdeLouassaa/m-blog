from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta :
        model = UserProfile
        fields = ('bio', 'user_image')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'user_image':  forms.FileInput(attrs={'class': 'form-control-file'}),
        
       }
       
       

