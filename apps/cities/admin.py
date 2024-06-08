from django.contrib import admin

from apps.cities.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']

