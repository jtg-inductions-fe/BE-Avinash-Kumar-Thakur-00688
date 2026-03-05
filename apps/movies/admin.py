from django.contrib import admin

from apps.movies import models as movies_models

admin.site.register(movies_models.Movie)
admin.site.register(movies_models.Slot)
admin.site.register(movies_models.Booking)
