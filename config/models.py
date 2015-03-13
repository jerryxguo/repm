import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey

import logging
logger = logging.getLogger(__name__)

# Create your models here.


class Office(models.Model):
    city = models.CharField(max_length=20, primary_key = True)
    exclude = models.BooleanField(default=False)
    address = models.CharField(max_length=40, blank=True, null=True)   
    state = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField('Contact Phone Number', max_length=10, blank=True, null=True)
    def __unicode__(self):
        return self.city
    class Meta:
        verbose_name_plural  = 'Office'
        

class Sales(models.Model):
    full_name = models.CharField(max_length=30, unique=True, primary_key = True)
    
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
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
    is_director =  models.BooleanField(default=False)
    on_board = models.BooleanField(default=True)   
    
    referrer = models.CharField('Referer', max_length=30, blank=True, null=True)
    def __unicode__(self):
        return self.full_name
    class Meta:        
        verbose_name_plural  = 'Sales'
 
            
            
class Client(models.Model):
    full_name = models.CharField(max_length=30)
    
    
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=10,blank=True)
   
    def _get_number_of_properties(self):
        
        return 0
        
    number_of_properties = property(_get_number_of_properties)

    class Meta:
        verbose_name_plural  = 'Client'
    
    def __unicode__(self):
        return self.full_name

class Project(models.Model):
    name = models.CharField(max_length=20, primary_key = True, unique = True)
    address = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural  = 'project'
        
class Property(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    lot = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    sales = models.ForeignKey(Sales, blank=True, null=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    
    STATUS_CHOICES = (
        ('--', '------'),
        ('CR', 'Contract Received'),
        ('CS', 'Contract Signed'),
        ('CE', 'Contract Exchanged'),
        ('CU', 'Contract Unconditional'),
        ('PS', 'Property Settled'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default ='--')    
    date = models.DateField( blank=True, null = True)    
    def _get_date(self):
        if self.status=='--':
            return None
        return timezone.now()
        
    date = property(_get_date)
    def __unicode__(self):
        return str(self.lot)
    class Meta:
        verbose_name_plural  = 'Properties'
        
        
class Bonus(models.Model):
    
    number_of_sales = models.IntegerField('Number of Sales', default=0)    
    bonus = models.IntegerField('Bonus(AUS)', default=0)
    
    class Meta:
        verbose_name_plural  = 'Bonue Plan'
        verbose_name  = 'Bonue Plan'
        
    def __unicode__(self):
        return 'Bonus Plan'
