from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignInForm(UserCreationForm):
    email = forms.EmailField()
    # firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    #     'class' : 'pt-4'
    # }))
    # lastname = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']