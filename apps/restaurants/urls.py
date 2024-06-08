from django.urls import path

from apps.restaurants import views

urlpatterns = [
    path('restaurant/', views.RestaurantListView.as_view(), name='rest_list'),
    path('restaurant/create/', views.RestaurantCreateView.as_view(), name='rest_create'),
    path('restaurant/detail/<int:pk>/', views.RestaurantDetailView.as_view(), name='rest_detail'),
    path('restaurant/update/<int:pk>/', views.RestaurantUpdateView.as_view(), name='rest_update'),
    path('restaurant/delete/<int:pk>/', views.RestaurantDeleteView.as_view(), name='rest_delete'),
    path('about/', views.about_us, name='about'),
]
