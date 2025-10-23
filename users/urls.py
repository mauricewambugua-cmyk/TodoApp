from django.urls import path
from .views import registerview
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',registerview.as_view(), name='register'),
]