from django.core.validators import MinValueValidator
from django.db import models


class Location(models.Model):
    """
    Represent the geographical location.
    """

    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["country", "state", "city", "area"], name="unique_location"
            )
        ]

    def __str__(self):
        return f"{self.area}, {self.city}" if self.area else self.city


class Cinema(models.Model):
    """
    Represent where movie is played.
    """

    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    seats_per_row = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="cinemas")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "location"], name="unique_cinema_per_location")
        ]

    def __str__(self):
        return f"{self.name} - {self.location}"


class Seat(models.Model):
    """
    Represent seats in the cinema.
    """

    SEAT_STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("BOOKED", "Booked"),
        ("UNAVAILABLE", "Unavailable"),
    ]

    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="seats")
    row_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    seat_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=SEAT_STATUS_CHOICES, default="AVAILABLE")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cinema", "row_number", "seat_number"], name="unique_seat_per_cinema"
            )
        ]

    def __str__(self):
        return f"{self.cinema.name} - {self.row_number}{self.seat_number}"
