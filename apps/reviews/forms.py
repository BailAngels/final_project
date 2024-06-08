from django import forms

from apps.reviews.models import RestaurantReview, DishesReview


class RestaurantReviewCreateForm(forms.ModelForm):

    class Meta:
        model = RestaurantReview
        fields = ['text',]


class RestaurantReviewUpdateForm(forms.ModelForm):

    class Meta:
        model = RestaurantReview
        fields = ['text']


class DishesReviewCreateForm(forms.ModelForm):

    class Meta:
        model = DishesReview
        fields = ['text']


class DishesReviewUpdateForm(forms.ModelForm):

    class Meta:
        model = DishesReview
        fields = ['text']
