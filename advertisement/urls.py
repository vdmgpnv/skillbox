from django.urls import path
from .views import index, About, AdvertisementListView, AdvertisementDetailView, AdvertisementCreateView


urlpatterns = [
    path('', index, name='advertisement_list'),
    path('about', About.as_view()),
    path('  ', AdvertisementListView.as_view(), name='advertisements'),
    path('advertisement/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('advertisement/create', AdvertisementCreateView.as_view())
]
