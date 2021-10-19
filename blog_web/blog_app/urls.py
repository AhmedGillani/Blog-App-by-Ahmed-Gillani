from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('post/', post, name='post'),
    path('feedback/', feedback, name='feedback'),
    path('detail/<int:id>/', detail, name='detail'),
    path('logout/', user_logout, name='logout'),
]
