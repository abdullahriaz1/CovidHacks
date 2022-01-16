from django.db import models
from django.forms import EmailField
import random, string

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length= 50, default= '')
    phoneNumber = models.BigIntegerField(default= 0)
    email = models.EmailField(default='example@example.com')
    vaccinationNum = models.BigIntegerField(default=0)
    recentTestNegative = models.BooleanField(default=True)
    eventID = models.CharField(max_length=15, default= '')
    class Meta:
        ordering = ['-name', '-phoneNumber', '-email', '-vaccinationNum', '-recentTestNegative', '-eventID']    
    
class Event(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.CharField(default='', max_length=50)
    date = models.CharField(max_length= 50, default='')
    address = models.CharField(max_length=50, default='')
    county = models.CharField(max_length= 50, default='')
    state  = models.CharField(max_length= 50, default='')
    numVaccinesRequired = models.BigIntegerField(default='0')
    recentTestRequired = models.BooleanField(default=True)  
    hostName = models.CharField(max_length= 50, default='')
    hostPhoneNumber = models.BigIntegerField(default=0)
    hostEmail = models.EmailField(default='example@example.com')
    eventCode = models.CharField(max_length=20, default='')

    class Meta:
        ordering = ['-name', '-description', '-date', '-address', '-county', '-state', '-numVaccinesRequired', '-recentTestRequired','-hostName','-hostEmail','-hostPhoneNumber','-eventCode']

class EventFinder(models.Model):
    code = models.CharField(default='',max_length=20)
    
    class Meta:
        ordering = ['-code']