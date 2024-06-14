from django.urls import path
from .views import data,home

urlpatterns=[
    path('', home, name='home'),
    path('data/',data,name='data'),
]