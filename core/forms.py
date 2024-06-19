from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import Item,Comment


class ItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your Product Name',
        'class' : 'py-2 px-6 rounded-xl mb-4 mt-6 shadow-xl'
    }))
    discription = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'Your Product discription',
        'class' : 'py-1 px-3 rounded-xl mb-4 mt-3 shadow-xl'
    }))
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['author',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields  = '__all__'
        exclude = ['item',]

class LoginForm(AuthenticationForm):
    class Meta:
        widget = {
            'username':forms.TextInput(attrs={
                'class':'py-2 px-6 rounded-xl mb-4 mt-6 shadow-xl'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'py-2 px-6 rounded-xl mb-4 mt-6 shadow-xl'
            })
        }