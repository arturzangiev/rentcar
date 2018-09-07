from django.contrib import admin
from . import models


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_make', 'car_model', 'car_registration', 'car_vin')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'start_date', 'end_date', 'user')


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Booking, BookingAdmin)