from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy

from apps.reviews.models import RestaurantReview, DishesReview
from apps.reviews import forms 
from apps.restaurants.models import Restaurant
from apps.dishes.models import Dish

class RestReviewListView(generic.ListView):
    model = RestaurantReview
    template_name = 'review/restreviewindex.html'
    context_object_name = 'restreviews'


class RestReviewCreateView(generic.CreateView):
    model = RestaurantReview
    form_class = forms.RestaurantReviewCreateForm
    template_name = 'review/restreviewcreate.html'

    def form_valid(self, form):
        form.instance.restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('rest_detail', kwargs={'pk': self.kwargs['pk']})


class RestReviewUpdateView(generic.UpdateView):
    model = RestaurantReview
    form_class = forms.RestaurantReviewUpdateForm
    template_name = 'review/restreviewupdate.html'
    success_url = reverse_lazy('/')


class RestReviewDeleteView(generic.DeleteView):
    model = RestaurantReview
    template_name = 'review/restreviewdelete.html'
    success_url = reverse_lazy('/')




class DishReviewListView(generic.ListView):
    model = DishesReview
    template_name = 'review/dishreviewindex.html'
    context_object_name = 'restreviews'


class DishReviewCreateView(generic.CreateView):
    model = DishesReview
    form_class = forms.DishesReviewCreateForm
    template_name = 'review/dishreviewcreate.html'

    def form_valid(self, form):
        form.instance.dish = get_object_or_404(Dish, pk=self.kwargs['pk'])
        form.instance.users = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dish_detail', kwargs={'pk': self.kwargs['pk']})


class DishReviewDetailView(generic.DetailView):
    model = DishesReview
    template_name = 'review/dishreviewdetail.html'
    context_object_name = 'restreview'


class DishReviewUpdateView(generic.UpdateView):
    model = DishesReview
    form_class = forms.DishesReviewUpdateForm
    template_name = 'review/dishreviewupdate.html'
    success_url = reverse_lazy('/')


class DishReviewDeleteView(generic.DeleteView):
    model = DishesReview
    template_name = 'review/dishreviewdelete.html'
    success_url = reverse_lazy('/')
