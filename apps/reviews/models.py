from django.db import models
from django.contrib.auth import get_user_model

from apps.dishes.models import Dish
from apps.restaurants.models import Restaurant


User = get_user_model()


class DishesReview(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации'
    )
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dish_reviews',
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='dish_reviews',
        verbose_name='блюдо'
    )

    def __str__(self):
        return f'{self.pub_date}'

    
    class Meta:
        verbose_name = 'Рецензия блюд'
        verbose_name_plural = 'Рецензии блюд'


class RestaurantReview(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rustaurant_reviews',
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_reviews',
        verbose_name='ресторан'
    )

    def __str__(self):
        return f'{self.pub_date}'


    class Meta:
        verbose_name = 'Рецензия ресторанов'
        verbose_name_plural = 'Рецензии ресторанов'