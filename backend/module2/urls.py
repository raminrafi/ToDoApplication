from django.urls import path
from django.urls import path
from .views import task_list

urlpatterns = [
    path ('task/',task_list),

]