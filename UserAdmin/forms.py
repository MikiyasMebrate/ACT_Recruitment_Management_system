from django import forms
from django.contrib.auth.forms import UserCreationForm
from Account.models import CustomUser


class SuperUserCreationForm(UserCreationForm):
    class Meta: 
        model: CustomUser
        fields = ('first_name','last_name', 'username', 'email','password1', 'password2')

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form=control'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'password1' : forms.PasswordInput(attrs={
                'class':'form-control'
            }),
            'password2' : forms.PasswordInput(attrs={
                'class' : 'form-control'
            })
        }
