from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete_view, name='post_delete'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
