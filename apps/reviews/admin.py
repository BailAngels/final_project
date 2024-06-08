from django.contrib import admin

from apps.reviews.models import DishesReview, RestaurantReview


@admin.register(DishesReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pub_date']
    list_filter = ['pub_date']
    search_fields = ['pub_date']


@admin.register(RestaurantReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pub_date']
    list_filter = ['pub_date']
    search_fields = ['pub_date']
