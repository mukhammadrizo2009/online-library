from django.urls import path
from .views import register_view, login_view, user_logout, home

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path("", home, name="home"),
]
