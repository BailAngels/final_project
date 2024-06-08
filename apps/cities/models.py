from django.db import models


class City(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='навзание',
    )
    description = models.TextField(
        max_length=500,
        verbose_name='описание',
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='изображение'
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'