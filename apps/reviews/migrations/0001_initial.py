# Generated by Django 5.0.4 on 2024-05-16 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'Рецензия ресторанов',
                'verbose_name_plural': 'Рецензии ресторанов',
            },
        ),
        migrations.CreateModel(
            name='DishesReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_reviews', to='dishes.dish', verbose_name='блюдо')),
            ],
            options={
                'verbose_name': 'Рецензия блюд',
                'verbose_name_plural': 'Рецензии блюд',
            },
        ),
    ]
