from django.urls import path

from apps.cities import views


urlpatterns = [
    path('', views.CityListView.as_view(), name='homepage'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='detail'),
]
