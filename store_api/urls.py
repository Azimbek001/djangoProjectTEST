from django.urls import path
from .views import post_list_create, post_detail, review_list_create, review_detail

urlpatterns = [
    path('posts/', post_list_create, name='post-list-create'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/<int:post_id>/reviews/', review_list_create, name='review-list-create'),
    path('posts/<int:post_id>/reviews/<int:pk>/', review_detail, name='review-detail'),
]
