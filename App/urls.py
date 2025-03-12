from django.urls import path
from .views import file_list

urlpatterns = [
    path('', file_list, name='file_list'),
]