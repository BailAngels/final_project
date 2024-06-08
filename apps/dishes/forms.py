from django import forms

from apps.dishes.models import Dish, DishImage


class DishImageForm(forms.ModelForm):
    class Meta:
        model = DishImage
        fields = ('image', )
        widgets = {'image': forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })}


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'description', 'restaurants']

