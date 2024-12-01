from django.db import models

class Taxi(models.Model):
    taxi_name = models.CharField(max_length=50)
    license_plate = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=50)
    passenger_capacity = models.PositiveIntegerField()
    car_model = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
