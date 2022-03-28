from django.contrib.auth.views import logout
from django.urls import path
from . import views


rlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('chat/verify/', views.verify, name='verify'),
    path('register/', views.register_view, name='register'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('register/', views.register_view, name='register'),
    path('send_email/', views.send_email, name='send_email'),
     
]    