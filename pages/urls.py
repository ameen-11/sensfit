from django.urls import path
from .views import data, home, sensor_data, success, display, sendData,getMaxData,getMinData,charts,maps,login_view,login

urlpatterns = [
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('data/', data, name='data'),
    path('sensor_data/', sensor_data, name='sensor_data'),
    path('success/', success, name='success'),
    path('display/', display, name='display'),
    path('send_data/', sendData, name='sendData'),
    path('get-max-data/',getMaxData,name='getMaxData'),
    path('get-min-data/',getMinData,name='getMinData'),
    path('charts/',charts,name='charts'),
    path('maps/',maps,name='maps'),
]
