from django.urls import path
from .views import data,home,sensor_data,success,display

urlpatterns=[
    path('', home, name='home'),
    path('data/', data, name='data'),
    path('sensor_data/', sensor_data, name='sensor_data'),
    path('success/', success, name='success'),
    path('display/', display, name='display'),
]