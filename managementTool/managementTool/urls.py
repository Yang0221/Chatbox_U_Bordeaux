from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('edit/<id>' , views.edit , name = 'edit'),
    path('edit/<id>/edit_building' , views.edit_building , name = 'edit_building'),
    path('edit/<id>/add_synonym' , views.add_synonym , name = 'add_synonym'),
    path('edit/<id>/add_room' , views.add_room , name = 'add_room'),
    path('' , views.index , name = 'index'),
    path('admin/', admin.site.urls)
]
