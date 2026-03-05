from decimal import Decimal

from cloudinary.models import CloudinaryField
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from apps.cinemas.models import Cinema, Seat


class Movie(models.Model):
    """
    Represent the movie which is played in cinema.
    """

    name = models.CharField(max_length=100, unique=True)
    poster = CloudinaryField("poster", folder="movies/images/")
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Slot(models.Model):
    """
    Represent slot for the movie in specific cinema.
    """

    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="slots")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="slots")
    date_time = models.DateTimeField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Price per ticket in INR",
    )

    def __str__(self):
        return f"{self.cinema.name} - {self.movie.name} at {self.date_time}"


class Booking(models.Model):
    """
    Represent Booking for the movie in the specific slot.
    """

    BOOKING_STATUS_CHOICES = [("BOOKED", "Booked"), ("CANCELLED", "Cancelled")]

    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings"
    )
    seats = models.ManyToManyField(Seat, related_name="bookings")
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default="BOOKED")

    def __str__(self):
        return f"Booking {self.id} - {self.user.email} ({self.slot})"
