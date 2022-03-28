from django.contrib.auth.views import logout
from django.urls import path

rlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chats'),
    path('register/', views.register_view, name='register'),
]    