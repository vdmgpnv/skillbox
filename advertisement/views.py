
from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import CreateView, TemplateView, ListView

from .models import Advertisement
from .forms import AdvertisementForm


def index(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement_list.html', {'advs': advertisements})


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления'
        context['text'] = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium, molestias.'
        return context


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisements_list.html'
    context_object_name = 'adv_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisement_detail.html'


class AdvertisementCreateView(View):
    
    
    def get(self, request):
        adv_form = AdvertisementForm()
        return render(request, 'create_advertisement.html', {'form' : adv_form})
    
    def post(self, request):
        adv_form = AdvertisementForm(request.POST)
        
        if adv_form.is_valid():
            Advertisement.objects.create(**adv_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'create_advertisement.html', {'form' : adv_form})