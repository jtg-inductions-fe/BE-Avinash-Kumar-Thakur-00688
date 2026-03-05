from django.contrib import admin

from apps.users import models as users_models

admin.site.register(users_models.User)
