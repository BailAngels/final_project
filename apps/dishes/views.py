from django.urls import reverse_lazy, reverse
from django.views import generic


from apps.dishes.models import Dish, DishImage
from apps.dishes.forms import DishForm
from apps.restaurants.models import Restaurant
from apps.reviews import forms

class DishListView(generic.ListView):
    model = Dish
    template_name = 'dish/list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(restaurants_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurant'] = Restaurant.objects.get(pk=self.kwargs['pk'])
        return context


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = 'dish/detail.html'
    context_object_name = 'dish'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.dish_reviews.all()
        context['review_form'] = forms.DishesReviewCreateForm()
        return context



class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish/create.html'

    def get_success_url(self):
        return reverse_lazy('restaurant_menu', kwargs={'pk': self.object.restaurants.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        images = self.request.FILES.getlist('images')  # Получаем список изображений из формы
        for image in images:
            DishImage.objects.create(image=image, dish=self.object)
        return super().form_valid(form)
    

class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish/update.html'

    def get_success_url(self):
        return reverse('dish_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist('images')  # Получаем список изображений из формы
        for image in images:
            DishImage.objects.create(image=image, dish=self.object)
        return super().form_valid(form)

class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = 'dish/delete.html'
    success_url = reverse_lazy('dish_list')

    def get_success_url(self):
        # Получаем объект ресторана, связанного с удаляемым блюдом
        restaurant_pk = self.get_object().restaurants.pk
        # Формируем URL для страницы с меню блюд ресторана
        return reverse_lazy('restaurant_menu', kwargs={'pk': restaurant_pk})
    