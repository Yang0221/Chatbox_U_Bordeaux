from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('edit/building/0' , views.index , name = 'index'),
    path('edit/building/<id>' , views.edit_building , name = 'edit_building'),
    path('edit/building/<id>/edit_informations' , views.edit_building_informations , name = 'edit_building_informations'),
    path('edit/building/<id>/add_synonym' , views.add_synonym_building , name = 'add_synonym_building'),
    path('edit/building/<id>/add_room' , views.add_room_building , name = 'add_room_building'),
    path('edit/building/<id>/edit_synonym/<alias>' , views.edit_alias_building , name = 'edit_alias_building'),
    path('edit/building/<id>/delete_synonym/<alias>' , views.delete_alias_building , name = 'delete_alias_building'),
    path('edit/building/<parent>/delete/<id>' , views.delete_room , name = 'delete_room'),
    path('edit/building/<id>/delete' , views.delete_building , name = 'delete_building'),


    path('edit/campus/0' , views.index , name = 'index'),
    path('edit/campus/<id>' , views.edit_campus , name = 'edit_campus'),
    path('edit/campus/<id>/edit_informations' , views.edit_campus_informations , name = 'edit_campus_informations'),
    path('edit/campus/<id>/add_synonym' , views.add_synonym_campus , name = 'add_synonym_campus'),
    path('edit/campus/<id>/add_building' , views.add_building_campus , name = 'add_building_campus'),
    path('edit/campus/<id>/edit_synonym/<alias>' , views.edit_alias_campus , name = 'edit_alias_campus'),
    path('edit/campus/<id>/delete_synonym/<alias>' , views.delete_alias_campus , name = 'delete_alias_campus'),
    path('edit/campus/<parent>/delete/<id>' , views.delete_building , name = 'delete_building'),
    path('edit/campus/<id>/delete' , views.delete_campus , name = 'delete_campus'),

    path('edit/room/<id>' , views.edit_room , name = 'edit_room'),
    path('edit/room/<id>/edit_informations' , views.edit_room_informations , name = 'edit_room_informations'),
    path('edit/room/<id>/add_synonym' , views.add_synonym_room , name = 'add_synonym_room'),
    path('edit/room/<id>/edit_synonym/<alias>' , views.edit_alias_room , name = 'edit_alias_room'),
    path('edit/room/<id>/delete_synonym/<alias>' , views.delete_alias_room , name = 'delete_alias_room'),
    path('edit/room/<id>/delete' , views.delete_room , name = 'delete_room'),

    path('addItem' , views.addItem , name = 'addItem'),
    path('exportCSV' , views.exportCSV , name = 'exportCSV'),
    path('' , views.index , name = 'index'),
    path('admin/', admin.site.urls)
]
