from django.db import models


class Car(models.Model):
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_registration = models.CharField(max_length=50)
    car_vin = models.CharField(max_length=50)

    def __str__(self):
        return self.car_registration


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.first_name