from django.urls import path

from apps.users import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('user/detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
]
