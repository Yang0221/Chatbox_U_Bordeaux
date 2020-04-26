from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('edit/building/<id>' , views.edit_building , name = 'edit_building'),
    path('edit/building/<id>/edit_informations' , views.edit_building_informations , name = 'edit_building_informations'),
    path('edit/building/<id>/add_synonym' , views.add_synonym_building , name = 'add_synonym_building'),
    path('edit/building/<id>/add_room' , views.add_room_building , name = 'add_room_building'),





    path('deleteBuilding' , views.deleteBuilding , name = 'deleteBuilding'),
    path('addItem' , views.addItem , name = 'addItem'),
    path('exportCSV' , views.exportCSV , name = 'exportCSV'),
    #path('displayTable' , views.displayTable , name = 'displayTable'),
    path('' , views.index , name = 'index'),
    path('admin/', admin.site.urls)
]
