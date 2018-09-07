from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Car(models.Model):
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_registration = models.CharField(max_length=50)
    car_vin = models.CharField(max_length=50)

    def __str__(self):
        return self.car_registration


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.user.username