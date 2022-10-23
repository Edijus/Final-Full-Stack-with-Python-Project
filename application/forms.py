from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Categories, Notes


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditUserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'image']


class EditCategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'user']


class EditNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['name', 'user', 'text']

