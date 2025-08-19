from django.shortcuts import render, redirect
from .forms import RideBookingForm
from .models import RideBooking

def header(request):
    return render(request, 'bookings/header.html')

def home(request):
    form = RideBookingForm()
    last_bookings = RideBooking.objects.order_by('-id')[:5]
    top_routes = [f"{b.pickup_location} → {b.drop_location}" for b in last_bookings]
    return render(request, 'bookings/home.html', {'form': form, 'top_routes': top_routes})

def book_ride(request):
    if request.method == 'POST':
        form = RideBookingForm(request.POST)
        if form.is_valid():
            form.save()  # saves to MongoDB
            return redirect('thank_you')  # redirect after successful booking
    else:
        form = RideBookingForm()

    # Last 5 bookings from MongoDB
    last_bookings = RideBooking.objects.order_by('-id')[:5]
    top_routes = [f"{b.pickup_location} → {b.drop_location}" for b in last_bookings]

    return render(request, 'bookings/home.html', {'form': form, 'top_routes': top_routes})
def thank_you(request):
    return render(request, 'bookings/thank_you.html')
def list_bookings(request):
    bookings = RideBooking.objects.all()
    return render(request, 'bookings/bookings_list.html', {'bookings': bookings})
