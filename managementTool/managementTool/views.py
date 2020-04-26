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
import json
from django.core import serializers


def displayInformations():
    buildings = Building.objects.all();
    for b in buildings :
        b.number = Room.objects.filter(id_building = b.id).count()

    campus =  Campus.objects.all();
    for c in campus :
        c.number = Building.objects.filter(id_campus = c.id).count()

    rooms = Room.objects.all();
    return {'buildings' : buildings, 'campus' : campus, 'rooms' : rooms}


def index(request):
    return render(request , 'index.html', displayInformations())

def edit_building(request,id):
    building = Building.objects.get(id = id)
    rooms = Room.objects.filter(id_building = id)
    synonyms = SynonymBuilding.objects.filter(id_building = id)
    return render(request , 'edit.html', {'type':'building', 'building' : building, 'rooms' : rooms, 'synonyms' : synonyms})


def edit_building_informations(request,id):
    if request.POST:
        building = Building.objects.get(id = id)
        building.name = request.POST.get('name')
        building.main_activity = request.POST.get('mainActivity')
        building.address = request.POST.get('address')
        building.coordinates = request.POST.get('coordinatesGPS')
        building.save()
    return HttpResponseRedirect("/edit/building/" + id)


def add_synonym_building(request,id):
    if request.POST:
        building = Building.objects.get(id = id)
        new_synomym = SynonymBuilding(id_building = building , value = request.POST.get('alias'))
        new_synomym.save()
    return HttpResponseRedirect("/edit/building/" + id)


def add_room_building(request,id):
    if request.POST:
        building = Building.objects.get(id = id)
        new_room = Room(id_building = building , name = request.POST.get('roomName'), floor = request.POST.get('stage'), activity = request.POST.get('activity'))
        new_room.save()
    return HttpResponseRedirect("/edit/building/" + id)


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

def deleteBuilding(request):
    if request.POST and request.is_ajax:
        Building.objects.get(id = request.POST.get('id')).delete()
    return HttpResponse(json.dumps("ok"), content_type="application/json")

def addItem(request):
    if request.POST and request.is_ajax:
        if request.POST.get('type') == 'building':
            new_item = Building(name = request.POST.get('new_name'))
        elif request.POST.get('type') == 'campus':
            new_item = Campus(name = request.POST.get('new_name'))
        if request.POST.get('type') == 'room':
            new_item = Room(name = request.POST.get('new_name'))
        new_item.save()
    return HttpResponse(json.dumps(new_item.id), content_type="application/json")

# def displayTable(request):
#     informations = displayInformations()
#     buildings = informations['buildings']
#     campus = informations['campus']
#     rooms = informations['rooms']
#     data = {
#         'campus' : serializers.serialize('json', campus),
#         'buildings' : serializers.serialize('json', buildings),
#         'rooms' : serializers.serialize('json', rooms)
#     }
#
#     return HttpResponse(json.dumps(data), content_type='application/json')



def error(request):
    return index(request)
