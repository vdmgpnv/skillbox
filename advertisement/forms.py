from django.forms import ModelForm
from .models import Advertisement

class AdvertisementForm(ModelForm):
    
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'price', 'type', 'region')