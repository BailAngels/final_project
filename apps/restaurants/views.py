from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from apps.restaurants.models import Restaurant
from apps.restaurants.forms import RestaurantForm, RestaurantImageFormSet
from apps.reviews.forms import RestaurantReviewCreateForm


class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name = 'restaurant/res_index.html'
    context_object_name = 'rests'


class RestaurantCreateView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        form = RestaurantForm()
        formset = RestaurantImageFormSet()
        return render(request, 'restaurant/res_create.html', {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
            form = RestaurantForm(request.POST)
            formset = RestaurantImageFormSet(request.POST, request.FILES)
            if form.is_valid() and formset.is_valid():
                restaurant = form.save()
                formset.instance = restaurant  # Связываем formset с рестораном
                formset.save()
                return redirect(reverse_lazy('rest_list'))
            return render(request, 'restaurant/res_create.html', {'form': form, 'formset': formset})


class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant/res_detail.html'
    context_object_name = 'rest'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.restaurant_reviews.all()
        context['review_form'] = RestaurantReviewCreateForm()
        return context


class RestaurantUpdateView(generic.UpdateView):
    def get(self, request, pk, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        form = RestaurantForm(instance=restaurant)
        formset = RestaurantImageFormSet(instance=restaurant)  # Передаем instance ресторана
        return render(request, 'restaurant/res_update.html', {'form': form, 'formset': formset})

    def post(self, request, pk, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        form = RestaurantForm(request.POST, instance=restaurant)
        formset = RestaurantImageFormSet(request.POST, request.FILES, instance=restaurant)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse_lazy('rest_list'))
        return render(request, 'restaurant/res_update.html', {'form': form, 'formset': formset})

class RestaurantDeleteView(generic.DeleteView):
    model = Restaurant
    template_name = 'restaurant/res_delete.html'
    success_url = reverse_lazy('rest_list')



def about_us(request):
    return render(request, 'about.html', locals())

    