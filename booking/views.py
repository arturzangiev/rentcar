from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Car, Booking
from .forms import BookingCreateForm


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
            # Check two hours
            # bookings = Booking.objects.all().filter(user=request.user)


            obj = Booking.objects.create(
                user=request.user,
                car=form.cleaned_data.get('car'),
                start_date=form.cleaned_data.get('start_date'),
                end_date=form.cleaned_data.get('end_date')
            )

            return HttpResponseRedirect('/create/')

    if request.method == "GET":
        cars = Car.objects.all()
        bookings = Booking.objects.all().filter(user=request.user)
        template = 'create.html'
        context = {'bookings': bookings, 'cars': cars}
        return render(request, template, context)