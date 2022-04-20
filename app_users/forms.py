from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(required=True, help_text='Город проживания')
    date_of_birth = forms.DateField(required=False, help_text='Дата рождения')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')