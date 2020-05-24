from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user, name='user'),
    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('accounts/', include('django.contrib.auth.urls')),
]