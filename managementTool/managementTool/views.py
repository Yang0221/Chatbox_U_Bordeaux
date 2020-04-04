from django.shortcuts import render
from localisation.models import Building
from localisation.models import Room
from localisation.models import SynonymBuilding
from django.http import HttpResponseRedirect

def index(request):
    return render(request , 'index.html', {'buildings' : Building.objects.all()})

def edit(request,id):
    building = Building.objects.filter(id = id)
    rooms = Room.objects.filter(id_building = id)
    synonyms = Synonym.objects.filter(id_building = id)
    return render(request , 'edit.html', {'building' : building[0], 'rooms' : rooms, 'synonyms' : synonyms})

def edit_building(request,id):
    if request.POST:
        building = Building.objects.filter(id = id)
        building = building[0]
        building.name = request.POST.get('name')
        building.main_activity = request.POST.get('mainActivity')
        building.address = request.POST.get('address')
        building.coordinates = request.POST.get('coordinatesGPS')
        building.save()
    return HttpResponseRedirect("/edit/" + id)

def add_synonym(request,id):
    if request.POST:
        building = Building.objects.filter(id = id)
        new_synomym = SynonymBuildings(id_building = building[0] , value = request.POST.get('alias'))
        new_synomym.save()
    return HttpResponseRedirect("/edit/" + id)

def add_room(request,id):
    if request.POST:
        building = Building.objects.filter(id = id)
        new_room = Room(id_building = building[0] , name = request.POST.get('roomName'), floor = request.POST.get('stage'), activity = request.POST.get('activity'))
        new_room.save()
    return HttpResponseRedirect("/edit/" + id)

def error(request):
    return index(request)
