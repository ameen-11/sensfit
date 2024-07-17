from django import forms
from .models import SensorData


class SensorDataForm(forms.ModelForm):
    class Meta:
        model = SensorData
        exclude = ['timestamp']
        fields = [
            'timestamp', 'ax', 'ay', 'az', 'pitch', 'roll', 'azimuth',
            'avx', 'avy', 'avz', 'mfx', 'mfy', 'mfz', 'latitude',
            'longitude', 'altitude', 'hacc',
        ]
