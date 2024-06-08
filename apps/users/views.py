from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from apps.users.models import User
from apps.users.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView


class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user/register.html'

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})


class UserDetailView(DetailView):
    model = User   
    template_name = 'user/detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('user_detail')  

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('homepage')