from django.contrib import admin
from . import models


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_make', 'car_model', 'car_registration', 'car_vin')
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Car, CarAdmin)