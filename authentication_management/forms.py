from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from django import forms


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',
                  'password1', 'password2']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100)
    new_password1 = forms.CharField(max_length=100)
    new_password2 = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
