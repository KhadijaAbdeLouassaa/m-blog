from django import forms
from .models import Post,Comment

# create your forms here


class CreatePostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ('category','title', 'body', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        
        

