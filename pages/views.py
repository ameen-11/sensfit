from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import json

from .forms import SensorDataForm
from .models import SensorData
from django.db.models import Max,Min

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
    try:
        data = json.loads(request.body.decode('utf-8'))

        # Assuming 'timestamp' is a required field
        userID = data.get('userid')
        if userID is None:
            return JsonResponse({
                'error': 'userID field is required'
            }, status=400)

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
            longitude=data.get('longitude'),
            altitude=data.get('altitude'),
            hacc=data.get('hacc')
        )

        # Save the object to the database
        sensor_data.save()

        return JsonResponse({'status': 'success'}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def getMaxData(request):
    if request.method == 'GET':
        last_10_entries = SensorData.objects.order_by('-timestamp')[:10]
        max_values = last_10_entries.aggregate(
            max_ax=Max('ax'),
            max_ay=Max('ay'),
            max_az=Max('az'),
            max_pitch=Max('pitch'),
            max_roll=Max('roll'),
            max_azimuth=Max('azimuth'),
            max_avx=Max('avx'),
            max_avy=Max('avy'),
            max_avz=Max('avz'),
            max_mfx=Max('mfx'),
            max_mfy=Max('mfy'),
            max_mfz=Max('mfz'),
            max_latitude=Max('latitude'),
            max_longitude=Max('longitude'),
            max_altitude=Max('altitude'),
            max_hacc=Max('hacc')
        )
        return JsonResponse(max_values, status=200)
    else:
        return JsonResponse({
            'error': 'Only GET requests are allowed'
        }, status=405)
        
        
@csrf_exempt
def getMinData(request):
    if request.method == 'GET':
        last_10_entries = SensorData.objects.order_by('-timestamp')[:10]
        min_values = last_10_entries.aggregate(
            min_ax=Min('ax'),
            min_ay=Min('ay'),
            min_az=Min('az'),
            min_pitch=Min('pitch'),
            min_roll=Min('roll'),
            min_azimuth=Min('azimuth'),
            min_avx=Min('avx'),
            min_avy=Min('avy'),
            min_avz=Min('avz'),
            min_mfx=Min('mfx'),
            min_mfy=Min('mfy'),
            min_mfz=Min('mfz'),
            min_latitude=Min('latitude'),
            min_longitude=Min('longitude'),
            min_altitude=Min('altitude'),
            min_hacc=Min('hacc')
        )
        return JsonResponse(min_values, status=200)
    else:
        return JsonResponse({
            'error': 'Only GET requests are allowed'
        }, status=405)
