from django import forms

from .models import ChangePasswordAfterReset

from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm
)
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 
            'last_name',
            'username',
            'email'
        )


class PasswordChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'password',
            'password',
            'password'
        )
