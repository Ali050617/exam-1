from django.shortcuts import render

from .models import Taxi

def taxi_list(requests):
    taxi_name = requests.GET.get('taxi_name')
    license_plate = requests.GET.get('license_plate')
    driver_name = requests.GET.get('driver_name')
    passenger_capacity = requests.GET.get('passenger_capacity')
    car_model = requests.GET.get('car_model')
    status = requests.GET.get('status')
    if (taxi_name and
            license_plate and
            driver_name and
            passenger_capacity and
            car_model and
            status):
        Taxi.objects.create(
            taxi_name=taxi_name,
            license_plate=license_plate,
            driver_name=driver_name,
            passenger_capacity=passenger_capacity,
            car_model=car_model,
            status=status
        )
    taxi =Taxi.objects.all()
    ctx = {'taxi': taxi}
    return render(requests, 'taxi/taxi-list.html', ctx)