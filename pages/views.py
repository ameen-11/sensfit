import os
from django.shortcuts import render
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .forms import SensorDataForm
from datetime import datetime
from .models import SensorData
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            sensor_data = form.save(commit=False)
            sensor_data.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sensor_data.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = SensorDataForm()

    return render(request, 'pages/sensor_data.html', {'form': form})


def home(request):
    return render(request, 'pages/home.html')

def data(request):
    return render(request, 'pages/data.html')


def display(request):
    sensor_data = SensorData.objects.all()
    return render(request, 'pages/display.html', {'sensor_data': sensor_data})

def success(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = SensorDataForm()
    
    return render(request, 'pages/sensor_data.html', {'form': form})
   
