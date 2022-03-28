from django.contrib.auth.views import logout
from django.urls import path
from . import views


rlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chats'),
    path('register/', views.register_view, name='register'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('register/', sender.register_view, name='register'),
    path('send_email/', sender.send_email, name='send_email'),
     
]    