from django.contrib import admin

from apps.cinemas import models as cinemas_models

admin.site.register(cinemas_models.Location)
admin.site.register(cinemas_models.Cinema)
admin.site.register(cinemas_models.Seat)
