from django import forms
from django.forms import inlineformset_factory

from apps.restaurants.models import Restaurant, RestaurantImage


class RestaurantImageForm(forms.ModelForm):
    class Meta:
        model = RestaurantImage
        fields = ('image', )
        widgets = {'image': forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })}


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'description', 'address', 'phone', 'city']

RestaurantImageFormSet = inlineformset_factory(
    Restaurant,
    RestaurantImage,
    form=RestaurantImageForm,
    extra=3,  # количество пустых форм для новых изображений
    can_delete=True
)
