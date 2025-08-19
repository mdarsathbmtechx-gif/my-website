from django.db import models

# Create your models here.
from mongoengine import Document, StringField, IntField

class RideBooking(Document):
    customer_name = StringField(required=True)
    pickup_location = StringField(required=True)
    drop_location = StringField(required=True)
    passengers = IntField(required=True)
    phone_number = StringField(required=True)  # new field
