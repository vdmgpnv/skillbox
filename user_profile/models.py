from django.db import models



class User(models.Model):
    username = models.CharField(
        max_length=20, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    last_name = models.CharField(max_length=20, verbose_name='Отчество')
    email = models.EmailField(verbose_name='Электронная почта')
    birthday = models.DateField(verbose_name='Дата рождения')
    
    
    
