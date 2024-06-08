from django.contrib import admin

from apps.dishes.models import Dish, DishImage


class DishInLine(admin.TabularInline):
    model = DishImage
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [DishInLine]


@admin.register(DishImage)
class DishImageAdmin(admin.ModelAdmin):
    list_display = ['image']


