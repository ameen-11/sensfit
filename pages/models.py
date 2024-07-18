from django.db import models
from datetime import datetime


class SensorData(models.Model):
    # Assuming timestamp as a string
    timestamp = models.CharField(max_length=255,
                                 default=datetime.now().isoformat())
    userid = models.CharField(max_length=255)
    ax = models.FloatField(null=True, blank=True)
    ay = models.FloatField(null=True, blank=True)
    az = models.FloatField(null=True, blank=True)
    pitch = models.FloatField(null=True, blank=True)
    roll = models.FloatField(null=True, blank=True)
    azimuth = models.FloatField(null=True, blank=True)
    avx = models.FloatField(null=True, blank=True)
    avy = models.FloatField(null=True, blank=True)
    avz = models.FloatField(null=True, blank=True)
    mfx = models.FloatField(null=True, blank=True)
    mfy = models.FloatField(null=True, blank=True)
    mfz = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    hacc = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"SensorData at {self.timestamp}"
