from django.urls import path
from .views import login, register,logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout')
]