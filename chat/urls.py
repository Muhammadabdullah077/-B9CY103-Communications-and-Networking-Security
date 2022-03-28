from django.contrib.auth.views import logout
rlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chats'),
]    