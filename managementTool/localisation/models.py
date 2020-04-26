from django.db import models
DEFAULT_ID = 1

class Campus(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 500, default= "")
    coordinates =  models.CharField(max_length = 500, default= "")

    class Meta:
        db_table = 'Campus'

class Room(models.Model):
    name = models.CharField(max_length = 255)
    floor = models.IntegerField(default=0)
    activity = models.CharField(max_length = 255, default= "")
    id_building = models.ForeignKey('Building' ,on_delete=models.CASCADE, default=DEFAULT_ID)

    class Meta:
        db_table = 'Room'

class Building(models.Model):
    name = models.CharField(max_length = 255)
    main_activity = models.CharField(max_length = 255, default= "")
    address = models.CharField(max_length = 500, default= "")
    coordinates =  models.CharField(max_length = 500, default= "")
    id_campus = models.ForeignKey('Campus' ,on_delete=models.CASCADE, default=DEFAULT_ID)

    class Meta:
        db_table = 'Building'

class SynonymRoom(models.Model):
    id_room = models.ForeignKey('Room' ,on_delete=models.CASCADE)
    value = models.CharField(max_length = 255)

class SynonymBuilding(models.Model):
    id_building = models.ForeignKey('Building' ,on_delete=models.CASCADE)
    value = models.CharField(max_length = 255)

class SynonymCampus(models.Model):
    id_campus = models.ForeignKey('Campus' ,on_delete=models.CASCADE)
    value = models.CharField(max_length = 255)
