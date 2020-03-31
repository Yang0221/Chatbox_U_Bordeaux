from django.shortcuts import render
from tool.models import Building
from tool.models import Room
from tool.models import Synonym

def index(request):
    return render(request , 'index.html', {'buildings' : Building.objects.all()})

def edit(request,id):
    building = Building.objects.filter(id = id)
    rooms = Room.objects.filter(id_building = id)
    synonyms = Synonym.objects.filter(id_building = id)
    return render(request , 'edit.html', {'building' : building[0], 'rooms' : rooms, 'synonyms' : synonyms})

def error(request):
    return index(request)
