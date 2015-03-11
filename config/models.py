import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey
import logging
logger = logging.getLogger(__name__)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Property(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    lot = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    def __unicode__(self):
        return str(self.lot)


class Office(models.Model):
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)   
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    def __unicode__(self):
        return self.city


class Sales(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    office = models.ForeignKey(Office, blank=True, null=True)
    number_of_sales = models.IntegerField(default=0, null=True)
    accumulation_bonus = models.IntegerField(default=0, null=True)    
    bonus_paid = models.IntegerField(default=0, null=True)
    date_of_paid = models.DateField( blank=True, null = True)
    bonus_unpaid = models.IntegerField(default=0, null=True)
    
    
    leader = models.BooleanField(default=False)
    def __unicode__(self):
        return self.full_name
   

class Client(models.Model):
    full_name = models.CharField(max_length=40)
    
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=20,blank=True)
    class Meta:
        verbose_name_plural  = 'Clients'
    
    def __unicode__(self):
        return self.full_name 