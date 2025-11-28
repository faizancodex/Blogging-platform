from django import forms
from HOME.models import Post
from tinymce.widgets import TinyMCE
from .models import CustomUser


# Post form (for blog or post creation)
class PostForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Post
        fields = ['post_category', 'post_title', 'description', 'image']


# User profile update form
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'bio', 'location', 'profile_picture']
