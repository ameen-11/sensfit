# Generated by Django 4.2.5 on 2024-07-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=255)),
                ('ax', models.FloatField(blank=True, null=True)),
                ('ay', models.FloatField(blank=True, null=True)),
                ('az', models.FloatField(blank=True, null=True)),
                ('pitch', models.FloatField(blank=True, null=True)),
                ('roll', models.FloatField(blank=True, null=True)),
                ('azimuth', models.FloatField(blank=True, null=True)),
                ('avx', models.FloatField(blank=True, null=True)),
                ('avy', models.FloatField(blank=True, null=True)),
                ('avz', models.FloatField(blank=True, null=True)),
                ('mfx', models.FloatField(blank=True, null=True)),
                ('mfy', models.FloatField(blank=True, null=True)),
                ('mfz', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('hacc', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]