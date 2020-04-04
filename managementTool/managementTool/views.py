from django.shortcuts import render
from localisation.models import Building
from localisation.models import Room
from localisation.models import Campus
from localisation.models import SynonymBuilding
from localisation.models import SynonymRoom
from localisation.models import SynonymCampus
from django.http import HttpResponseRedirect
import csv
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    return render(request , 'index.html', {'buildings' : Building.objects.all()})


def edit(request,id):
    building = Building.objects.filter(id = id)
    rooms = Room.objects.filter(id_building = id)
    synonyms = SynonymBuilding.objects.filter(id_building = id)
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


def writeCSV(index, writer, list):
    type = ["campus", "batiment", "salle"]

    for l in list:
        line = [type[index], l.name]
        alias = []
        if index == 0:
            alias = SynonymCampus.objects.filter(id_campus = l.id)
        elif index == 1:
            alias = SynonymBuilding.objects.filter(id_building = l.id)
        elif index == 2:
            alias = SynonymRoom.objects.filter(id_room = l.id)
        for a in alias:
            line.append(a.value)
        writer.writerow(line)


def exportCSV(request):
    response = HttpResponse(content_type='text/csv')
    filename = timezone.localtime().strftime("%m-%d-%Y") + "-localisation-export"
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)
    campus = Campus.objects.all()
    buildings = Building.objects.all()
    rooms = Room.objects.all()
    writeCSV(0, writer, campus)
    writeCSV(1, writer, buildings)
    writeCSV(2, writer, rooms)

    return response


def error(request):
    return index(request)
