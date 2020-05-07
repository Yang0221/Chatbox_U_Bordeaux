from django.contrib import admin
from django.urls import path
from . import views

app_name = 'demoChatbot'

urlpatterns = [
    path('' , views.main , name = 'main'),
    path('new_message', views.new_message, name = 'new_message'),
]
