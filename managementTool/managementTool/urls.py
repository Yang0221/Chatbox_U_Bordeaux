from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('edit/<id>' , views.edit , name = 'edit'),
    path('' , views.index , name = 'index'),
    path('admin/', admin.site.urls)
]
