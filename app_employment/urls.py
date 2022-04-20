from django.urls import path

from .views import vacancy_list


urlpatterns = [
    path('', vacancy_list, name='vacancy_list')
]
