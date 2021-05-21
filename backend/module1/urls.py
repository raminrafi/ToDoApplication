from django.urls import path
from django.urls import path
from .views import registration_list

urlpatterns = [
    path ('registration/',registration_list),

]