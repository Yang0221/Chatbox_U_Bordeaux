from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 500)
    coordinates =  models.CharField(max_length = 500)

class Room(models.Model):
    name = models.CharField(max_length = 255)
    floor = models.IntegerField()
    activity = models.CharField(max_length = 255)
    id_building = models.ForeignKey('Building' ,on_delete=models.CASCADE)

class Building(models.Model):
    name = models.CharField(max_length = 255)
    main_activity = models.CharField(max_length = 255)
    address = models.CharField(max_length = 500)
    coordinates =  models.CharField(max_length = 500)
    id_campus = models.ForeignKey('Campus' ,on_delete=models.CASCADE)

class SynonymRoom(models.Model):
    id_room = models.ForeignKey('Room' ,on_delete=models.CASCADE)
    value = models.CharField(max_length = 255)

class SynonymBuilding(models.Model):
    id_building = models.ForeignKey('Building' ,on_delete=models.CASCADE)
    value = models.CharField(max_length = 255)

class SynonymCampus(models.Model):
    id_campus = models.ForeignKey('Campus' ,on_delete=models.CASCADE)
    value = models.CharField(max_length = 255)
