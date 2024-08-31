from django.urls import path
from .views import data, home, sensor_data, success, display, sendData, getData

urlpatterns = [
    path('', home, name='home'),
    path('data/', data, name='data'),
    path('sensor_data/', sensor_data, name='sensor_data'),
    path('success/', success, name='success'),
    path('display/', display, name='display'),
    path('send_data/', sendData, name='sendData'),
    path('get_data/', getData, name='getData'),
]
