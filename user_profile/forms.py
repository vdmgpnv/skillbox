from django.forms import ValidationError
from django import forms
from .models import User
import datetime


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'second_name', 'last_name', 'email', 'birthday')

    def clean_birthday(self):
        '''Проверяет поле с датой'''
        data = self.cleaned_data['birthday']
        today = datetime.date.today()
        year_delta = (today - data).days / 365
        if year_delta < 18:
            raise ValidationError('До 18 нельзя')
        return data

    def clean(self):
        '''проверяет несколько полей на валидацию'''
        cleaned_data = super(UserForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == 'Вадим' and last_name == 'Сергеевич':
            msg = 'Нельзя Вадиму Сергеевичу Регистрироваться'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
