from django import views
from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    description = models.CharField(max_length=1000, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisements')
    region = models.ForeignKey('AdvertisementRegion', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')
    
    def __str__(self) -> str:
        return self.title

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)
    
class AdvertisementType(models.Model):
    name = models.CharField(max_length=1000)
    
class AdvertisementRegion(models.Model):
    region = models.CharField(max_length=1000)