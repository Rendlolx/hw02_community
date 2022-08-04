from .models import Post_create
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post_create
        fields = (
            'text',
            'group'
        )
        