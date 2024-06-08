from django.contrib import admin

from apps.restaurants.models import Restaurant, RestaurantImage


class RestaurantInLine(admin.TabularInline):
    model = RestaurantImage
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [RestaurantInLine]


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ['image']
