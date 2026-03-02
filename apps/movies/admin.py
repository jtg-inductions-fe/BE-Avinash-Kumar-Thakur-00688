from django.contrib import admin
from .models import Movie, Slot, Booking

admin.site.register(Movie)
admin.site.register(Slot)
admin.site.register(Booking)
