from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Car, Booking
from .forms import BookingCreateForm
import datetime
from datetime import timedelta

def index(request):
    if request.user.is_authenticated:
        context = {'button': 'Manage your car bookings', 'url': '/create/'}
    else:
        context = {'button': 'Please login to rent a car', 'url': '/login/'}

    template = 'index.html'
    return render(request, template, context)


@login_required(login_url='/')
def create(request):
    if request.method == "POST":
        form = BookingCreateForm(request.POST)
        if form.is_valid():
            user = request.user
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            car = form.cleaned_data.get('car')

            # Check if start_date is less then end_date
            if start_date < end_date:
                q_start_date = start_date - timedelta(hours=2)
                q_end_date = end_date + timedelta(hours=2)
                bookings = Booking.objects.all().filter(Q(car=car) & Q(start_date__range=[q_start_date, q_end_date]) | Q(end_date__range=[q_start_date, q_end_date])).count()
                if bookings == 0:
                    Booking.objects.create(user=user, car=car, start_date=start_date, end_date=end_date)
                    return HttpResponseRedirect('/create/')

                else:
                    return HttpResponse("The slot is already booked")

            else:
                return HttpResponseRedirect('/create/')

    if request.method == "GET":
        cars = Car.objects.all()
        bookings = Booking.objects.all().filter(user=request.user)
        template = 'create.html'
        context = {'bookings': bookings, 'cars': cars}
        return render(request, template, context)