# aptanimelistweb/urls.py
from re import search
from django.urls import path
from .views import register, user_login, user_logout, home,populer
from .views import search
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('', user_login, name='login'),
    path('search/', search, name='search'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('populer/',populer, name='populer'),
]
