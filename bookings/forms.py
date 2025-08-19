from django import forms
from .models import RideBooking  # your MongoEngine document

class RideBookingForm(forms.Form):
    customer_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    pickup_location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pickup location'})
    )
    drop_location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Drop location'})
    )
    passengers = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of passengers'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'})
    )

    def save(self):
        # Save to MongoDB using MongoEngine document
        booking = RideBooking(
            customer_name=self.cleaned_data['customer_name'],
            pickup_location=self.cleaned_data['pickup_location'],
            drop_location=self.cleaned_data['drop_location'],
            passengers=self.cleaned_data['passengers'],
            phone_number=self.cleaned_data['phone_number']
        )
        booking.save()
        return booking
