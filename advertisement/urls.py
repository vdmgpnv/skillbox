from operator import index
from django import views
from django.urls import path
from .views import index, About


urlpatterns = [
    path('', index, name='advertisement_list'),
    path('about/', About.as_view())
]
