from django.contrib import admin
from . import models

admin.site.register(models.Room)
admin.site.register(models.Building)
admin.site.register(models.Synonym)


