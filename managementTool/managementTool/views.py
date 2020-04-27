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



def index(request):
    hide = ""
    campus =  Campus.objects.all();
    if campus.count() > 0 :
        hide = "building"
        for c in campus :
            c.number = Building.objects.filter(id_campus = c.id).count()

    buildings = Building.objects.all();
    if buildings.count() > 0 :
        hide = "room"
        for b in buildings :
            b.number = Room.objects.filter(id_building = b.id).count()

    rooms = Room.objects.all();

    return render(request , 'index.html', {'buildings' : buildings, 'campus' : campus, 'rooms' : rooms, 'hide' : hide})

def edit_building(request,id):
    building = Building.objects.get(id = id)
    rooms = Room.objects.filter(id_building = id)
    synonyms = SynonymBuilding.objects.filter(id_building = id)
    campus = Campus.objects.all()
    for c in campus:
        if c.id == building.id_campus.id:
            c.selected = "selected"
        else :
            c.selected = ""
    return render(request , 'edit.html', {'type':'building', 'building' : building, 'rooms' : rooms, 'synonyms' : synonyms, 'campus' : campus})

def edit_room(request,id):
    room = Room.objects.get(id = id)
    buildings = Building.objects.all()
    for b in buildings:
        if b.id == room.id_building.id :
            b.selected = "selected"
        else :
            b.selected = ""
    synonyms = SynonymRoom.objects.filter(id_room = id)
    return render(request , 'edit.html', {'type':'room', 'room' : room, 'buildings' : buildings, 'synonyms' : synonyms})

def edit_campus(request,id):
    campus = Campus.objects.get(id = id)
    buildings = Building.objects.filter(id_campus = id)
    synonyms = SynonymCampus.objects.filter(id_campus = id)
    return render(request , 'edit.html', {'type':'campus', 'campus' : campus, 'buildings' : buildings, 'synonyms' : synonyms})

def edit_building_informations(request,id):
    if request.POST:
        building = Building.objects.get(id = id)
        if request.POST.get('name') != "":
            building.name = request.POST.get('name')
        if request.POST.get('mainActivity') != "":
            building.main_activity = request.POST.get('mainActivity')
        if request.POST.get('address') != "":
            building.address = request.POST.get('address')
        if request.POST.get('coordinatesGPS') != "":
            building.coordinates = request.POST.get('coordinatesGPS')
        if request.POST.get('campus_id') != "":
            building.id_campus = Campus.objects.get(id = request.POST.get('campus_id'))
        building.save()
    return HttpResponseRedirect("/edit/building/" + id)

def edit_room_informations(request,id):
    if request.POST:
        room = Room.objects.get(id = id)
        if request.POST.get('name') != "":
            room.name = request.POST.get('name')
        if request.POST.get('mainActivity') != "":
            room.activity = request.POST.get('mainActivity')
        if request.POST.get('stage') != "":
            room.floor = request.POST.get('stage')
        if request.POST.get('building_id') != "":
            room.id_building = Building.objects.get(id = request.POST.get('building_id'))
        room.save()
    return HttpResponseRedirect("/edit/room/" + id)

def edit_campus_informations(request,id):
    if request.POST:
        campus = Campus.objects.get(id = id)
        if request.POST.get('name') != "":
            campus.name = request.POST.get('name')
        if request.POST.get('address') != "":
            campus.address = request.POST.get('address')
        if request.POST.get('coordinatesGPS') != "":
            campus.coordinates = request.POST.get('coordinatesGPS')
        campus.save()
    return HttpResponseRedirect("/edit/campus/" + id)

def add_synonym_building(request,id):
    if request.POST:
        building = Building.objects.get(id = id)
        new_synomym = SynonymBuilding(id_building = building , value = request.POST.get('alias'))
        new_synomym.save()
    return HttpResponseRedirect("/edit/building/" + id)

def add_synonym_room(request,id):
    if request.POST:
        if request.POST.get('alias') != "":
            room = Room.objects.get(id = id)
            new_synomym = SynonymRoom(id_room = room , value = request.POST.get('alias'))
            new_synomym.save()
    return HttpResponseRedirect("/edit/room/" + id)

def add_synonym_campus(request,id):
    if request.POST:
        if request.POST.get('alias') != "":
            campus = Campus.objects.get(id = id)
            new_synomym = SynonymCampus(id_campus = campus , value = request.POST.get('alias'))
            new_synomym.save()
    return HttpResponseRedirect("/edit/campus/" + id)

def add_room_building(request,id):
    if request.POST and request.POST.get('roomName') != "":
        building = Building.objects.get(id = id)
        new_room = Room(id_building = building , name = request.POST.get('roomName'), floor = request.POST.get('roomStage'), activity = request.POST.get('activity'))
        new_room.save()
    return HttpResponseRedirect("/edit/building/" + id)


def add_building_campus(request,id):
    if request.POST and request.POST.get('buildingName') != "":
        campus = Campus.objects.get(id = id)
        new_building = Building(id_campus = campus , name = request.POST.get('buildingName'), address = request.POST.get('roomAddress'), main_activity = request.POST.get('activity'))
        new_building.save()
    return HttpResponseRedirect("/edit/campus/" + id)


def delete_alias_campus(request,id,alias):
    SynonymCampus.objects.get(id = alias).delete()
    return HttpResponseRedirect("/edit/campus/" + id)

def delete_alias_building(request,id,alias):
    SynonymBuilding.objects.get(id = alias).delete()
    return HttpResponseRedirect("/edit/building/" + id)

def delete_alias_room(request,id,alias):
    SynonymRoom.objects.get(id = alias).delete()
    return HttpResponseRedirect("/edit/room/" + id)

def delete_alias_campus(request,id,alias):
    SynonymCampus.objects.get(id = alias).delete()
    return HttpResponseRedirect("/edit/campus/" + id)

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

def delete_campus(request,id, parent = 0):
    Campus.objects.get(id = id).delete()
    return HttpResponseRedirect("/edit/campus/" + str(parent))

def delete_building(request,id, parent = 0):
    Building.objects.get(id = id).delete()
    return HttpResponseRedirect("/edit/campus/" + str(parent))


def delete_room(request,id, parent = 0):
    Room.objects.get(id = id).delete()
    return HttpResponseRedirect("/edit/building/" + str(parent))

def addItem(request):
    if request.POST and request.is_ajax:
        if request.POST.get('type') == 'building':
            campus = Campus.objects.all()
            new_item = Building(name = request.POST.get('new_name'), id_campus = campus[0])
            new_item.save()
            return HttpResponseRedirect("edit/building/" + str(new_item.id))
        elif request.POST.get('type') == 'campus':
            new_item = Campus(name = request.POST.get('new_name'))
            new_item.save()
            return HttpResponseRedirect("edit/campus/" + str(new_item.id))
        if request.POST.get('type') == 'room':
            building = Building.objects.all()
            new_item = Room(name = request.POST.get('new_name'), id_building = building[0])
            new_item.save()
            return HttpResponseRedirect("edit/room/" + str(new_item.id))

def edit_alias_campus(request, id, alias):
    if request.POST.get('edit_alias') != "":
        synonyms = SynonymCampus.objects.get(id = alias)
        synonym.value = request.POST.get('edit_alias')
        synonym.save()
        return HttpResponse(json.dumps("ok"), content_type='application/json')

def edit_alias_building(request, id, alias):
    if request.POST.get('edit_alias') != "":
        synonyms = SynonymBuilding.objects.get(id = alias)
        synonym.value = request.POST.get('edit_alias')
        synonym.save()
        return HttpResponse(json.dumps("ok"), content_type='application/json')

def edit_alias_room(request, id, alias):
    if request.POST.get('edit_alias') != "":
        synonyms = SynonymRoom.objects.get(id = alias)
        synonym.value = request.POST.get('edit_alias')
        synonym.save()
        return HttpResponse(json.dumps("ok"), content_type='application/json')
