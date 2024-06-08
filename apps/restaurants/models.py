from django.db import models
import os

from apps.cities.models import City


class Restaurant(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Адрес"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='restaurants',
        verbose_name='город'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class RestaurantImage(models.Model):
    image = models.ImageField(
        upload_to='restaurant_images/'
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='r_images',
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Изображение Ресторана"
        verbose_name_plural = "Изображения Ресторанов"