from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import json

from .forms import SensorDataForm
from .models import SensorData


@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            sensor_data = form.save(commit=False)
            sensor_data.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sensor_data.save()
            # Redirect to a success page or another view
            return redirect('success')
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
            # Redirect to a success page or another view
            return redirect('success')
    else:
        form = SensorDataForm()

    return render(request, 'pages/sensor_data.html', {'form': form})


@csrf_exempt
def sendData(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Assuming 'timestamp' is a required field
            userID = data.get('userid')
            if userID is None:
                return JsonResponse({
                    'error': 'userID field is required'
                }, status=400)

            print(data)
            # Create a new SensorData object
            sensor_data = SensorData(
                timestamp=data.get('timestamp'),
                userid=data.get('userid'),
                ax=data.get('ax'),
                ay=data.get('ay'),
                az=data.get('az'),
                pitch=data.get('pitch'),
                roll=data.get('roll'),
                azimuth=data.get('azimuth'),
                avx=data.get('avx'),
                avy=data.get('avy'),
                avz=data.get('avz'),
                mfx=data.get('mfx'),
                mfy=data.get('mfy'),
                mfz=data.get('mfz'),
                latitude=data.get('latitude'),
                longitude=data.get('longitude'), altitude=data.get('altitude'),
                hacc=data.get('hacc')
            )

            # Save the object to the database
            sensor_data.save()

            return JsonResponse({
                'message': 'Data stored successfully'
            }, status=201)

        except json.JSONDecodeError as e:
            return JsonResponse({
                'error': 'Invalid JSON format ' + str(e)
            }, status=400)

    else:
        return JsonResponse({
            'error': 'Only POST requests are allowed'
        }, status=405)
