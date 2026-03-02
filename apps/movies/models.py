from django.db import models
from apps.cinemas.models import Cinema
from apps.users.models import User

# Create your models here.


class Movie(models.Model):
    """
    Movie model to define the structure of the movie schema
    """
    name = models.CharField(max_length=100, unique=True)
    """Name of the movie"""
    poster = models.ImageField(upload_to='movies/images/')
    """Poster of the movie"""
    language = models.CharField(max_length=50)
    """Language of the movie"""
    genre = models.CharField(max_length=50)
    """Genre of the movie"""
    description = models.TextField()
    """Description of the movie"""
    duration = models.DurationField()
    """Duration of the movie"""

    class Meta:
        """
        Meta configuration for the movie model
        """
        db_table = 'movies_movie'
        """Explicitly defines the name of the table"""

    def __str__(self):
        """Returns human readable string representation"""
        return self.name


class Slot(models.Model):
    """
    Represent movie show timing in a cinema
    """
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    """Cinema where movie will be played"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    """Movie that will be played in the slot"""
    date_time = models.DateTimeField()
    """Date and timing of the movie"""
    price = models.DecimalField(max_digits=6, decimal_places=2)
    """Price of the ticket"""

    class Meta:
        """"
        Meta configuration for the slot model
        """
        db_table = 'slots_slot'
        """Explicitly defines the name of the table"""

    def __str__(self):
        """Returns human readable string representation"""
        return self.movie.name


class Booking(models.Model):
    """
    Represent the booking of the movie in particular slot
    """
    BOOKING_STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('BOOKED', 'Booked'),
        ('UNAVAILABLE', 'Unavailable')
    ]
    """Options of the booking status"""

    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    """Slot in which movie is played"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """User who booked ticket"""
    row = models.CharField(max_length=2)
    """Row number of the user"""
    seat = models.PositiveIntegerField()
    """Seat of the user"""
    status = models.CharField(
        max_length=20, choices=BOOKING_STATUS_CHOICES, default='AVAILABLE')
    """Status of the booking"""

    def __str__(self):
        """Returns human readable string representation"""
        return self.slot.movie.name
