from django.views import generic
from django.urls import reverse_lazy

from apps.cities.models import City
from apps.cities.forms import CityForm


class CityListView(generic.ListView):
    model = City
    template_name = 'city/index.html'
    context_object_name = 'cities'


class CityDetailView(generic.DetailView):
    model = City
    template_name = 'city/detail.html'
    context_object_name = 'city'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurants'] = self.object.restaurants.all()
        return context