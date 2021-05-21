from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login'),
]