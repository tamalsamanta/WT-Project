from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # birth_date = forms.DateField(help_text='Enter in yyyy-mm-dd format')
    contact = forms.CharField(max_length=10, help_text='Don\'t enter Country Code ')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','contact','password1', 'password2', )