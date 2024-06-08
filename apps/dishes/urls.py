from django.urls import path
from apps.dishes import views

urlpatterns = [
    path('restaurant/<int:pk>/menu/', views.DishListView.as_view(), name='restaurant_menu'),
    path('dish/create/', views.DishCreateView.as_view(), name='dish_create'),
    path('dish/detail/<int:pk>/', views.DishDetailView.as_view(), name='dish_detail'),
    path('dish/update/<int:pk>/', views.DishUpdateView.as_view(), name='dish_update'),
    path('dish/delete/<int:pk>/', views.DishDeleteView.as_view(), name='dish_delete'),
]
