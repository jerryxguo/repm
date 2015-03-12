import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from smart_selects.db_fields import ChainedForeignKey
#from sales.models import Purchase
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
    full_name = models.CharField(max_length=40, unique=True, primary_key = True)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    office = models.ForeignKey(Office, blank=True, null=True)
    number_of_sales = models.IntegerField(default=0, blank=True, null=True)
    accumulation_bonus = models.IntegerField(default=0, blank=True,  null=True)    
    bonus_paid = models.IntegerField(default=0, blank=True, null=True)
    date_of_paid = models.DateField( blank=True, null = True)

    def _get_bonus_unpaid(self):
        if self.accumulation_bonus is None:
            self.accumulation_bonus = 0
        if self.bonus_paid is None:
            self.bonus_paid = 0    
        return (self.accumulation_bonus - self.bonus_paid)
    bonus_unpaid = property(_get_bonus_unpaid)
    
    leader = models.BooleanField(default=False)
    on_board = models.BooleanField(default=True)
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

class Bonus(models.Model):
    
    number_of_sales = models.IntegerField('Number of Sales', default=0)    
    bonus = models.IntegerField('Bonus(AUS)', default=0)
    
    class Meta:
        verbose_name_plural  = 'Bonue Plan'
        verbose_name  = 'Bonue Plan'
        
    def __unicode__(self):
        return 'Bonus Plan'
