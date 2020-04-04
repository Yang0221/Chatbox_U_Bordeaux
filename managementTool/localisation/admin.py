from django.contrib import admin
from . import models

admin.site.register(models.Room)
admin.site.register(models.Building)
admin.site.register(models.Campus)
admin.site.register(models.SynonymRoom)
admin.site.register(models.SynonymBuilding)
admin.site.register(models.SynonymCampus)
