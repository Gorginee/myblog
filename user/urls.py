from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('is_registered/', is_registered, name='is_registered'),
]
