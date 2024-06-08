from django.db import models
from django.contrib.auth.models import AbstractUser
import os


class User(AbstractUser):
    display_name = models.CharField(
        max_length=150,
        verbose_name="Никнейм"
    )
    bio = models.TextField(
        verbose_name="о себе",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="user_avatar/",
        verbose_name="фотография",
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.avatar.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
