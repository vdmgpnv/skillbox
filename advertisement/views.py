
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Advertisement 

def index(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement_list.html', {'advs' : advertisements})



class About(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления'
        context['text'] = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium, molestias.'
        return context