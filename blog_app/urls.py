from django.urls import path, include
from .views import DeletePost, UpdatePost, CreatePost, detail, home

urlpatterns = [
    path("detail/<int:pk>/delete", DeletePost.as_view(), name="delete"),
    path("detail/<int:pk>/edit", UpdatePost.as_view(), name="edit"),
    path("new_post", CreatePost.as_view(), name="new_post"),
    path('detail/<int:pk>/', detail, name='detail'),
    path('', home, name='home'),
]
