from django.contrib import admin
from django.urls import path, include  # include added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),  # include all URLs from the bookings app
]
