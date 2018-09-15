from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField()

class HouseRoom(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    temperature_reading = models.CharField(max_length=100)
    humidity_reading = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name



