from django.db import models


class Location(models.Model):
    """
    Represent the geographical location
    """
    country = models.CharField(max_length=100)
    """Country name"""
    state = models.CharField(max_length=100)
    """State name"""
    city = models.CharField(max_length=100)
    """City name"""
    area = models.CharField(max_length=100, blank=True)
    """Area of the location"""

    class Meta:
        """
        Meta configuration for the movie model
        """
        db_table = "location_location"
        """Explicitly defines the name of the table"""

    def __str__(self):
        """Returns human readable string representation"""
        return f"{self.area}, {self.city}"


class Cinema(models.Model):
    """
    Represent cinema where movie is played
    """
    name = models.CharField(max_length=100, unique=True)
    """Name of the cinema"""
    rows = models.PositiveIntegerField()
    """Number of seat rows"""
    seats_per_row = models.PositiveIntegerField()
    """Number of seat per rows"""
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    """Geographic location of the cinema"""

    class Meta:
        """
        Meta configuration for the movie model
        """
        db_table = "cinemas_cinema"
        """Explicitly defines the name of the table"""

    def __str__(self):
        """Returns human readable string representation"""
        return self.name
