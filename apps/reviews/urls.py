from django.urls import path

from apps.reviews import views


urlpatterns = [
    path('review/', views.RestReviewListView.as_view(), name='restreview_list'),
    path('restaurant/<int:pk>/review/', views.RestReviewCreateView.as_view(), name='rest_review_create'),
    path('review/<int:pk>/update/', views.RestReviewUpdateView.as_view(), name='rest_review_update'),
    path('review/<int:pk>/delete/', views.RestReviewDeleteView.as_view(), name='rest_review_delete'),

    path('dish/<int:pk>/review/create/', views.DishReviewCreateView.as_view(), name='dish_review_create'),
    path('dish/review/update/<int:pk>/', views.DishReviewUpdateView.as_view(), name='dish_review_update'),
    path('dish/review/delete/<int:pk>/', views.DishReviewDeleteView.as_view(), name='dish_review_delete'),
]
