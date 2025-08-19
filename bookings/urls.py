from django.urls import path
from . import views

urlpatterns = [
    path('', views.header, name='header'),            # landing page
    path('home/', views.home, name='home'),          # booking form page
    path('book/', views.book_ride, name='book_ride'),# form submission
    path('thank-you/', views.thank_you, name='thank_you'),
    path('bookings/', views.list_bookings, name='list_bookings'),
]
