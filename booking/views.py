from django.shortcuts import render
from .models import Car


def index(request):
    cars = Car.objects.all()
    template = 'login.html'
    context = {'cars': cars}
    return render(request, template, context)