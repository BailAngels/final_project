from django.db import models
import os

from apps.restaurants.models import Restaurant


class Dish(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    restaurants = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="r_dish",
        verbose_name="Ресторан",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class DishImage(models.Model):
    image = models.ImageField(
        upload_to="dish_images/",
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name="d_images",
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Изображение Блюда"
        verbose_name_plural = "Изображение Блюд"