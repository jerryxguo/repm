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

    def __unicode__(self):
        return self.city

class Sales(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    office = models.ForeignKey(Office, blank=True, null=True)
    def __unicode__(self):
        return self.last_name + ','+ self.first_name
    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=20,blank=True)
    
    def __unicode__(self):
        return self.last_name + ','+ self.first_name    

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)
        
class Purchase(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    project_lot = ChainedForeignKey(Property,chained_field="project",chained_model_field="project",  show_all=False, auto_choose=True, blank=True, null=True)
    office = models.ForeignKey(Office, blank=True, null=True)
    sales = ChainedForeignKey(Sales,chained_field="office",chained_model_field="office",  show_all=False, auto_choose=True, blank=True, null=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    deposit = models.IntegerField(default=0)
    solicitor = models.CharField(max_length=40,blank=True)
    date_of_EOI_sent = models.DateField( blank=True, null = True)
    date_of_contract_received = models.DateField( blank=True, null = True)
    date_of_contract_signed = models.DateField( blank=True, null = True)
    date_of_BOD_paid  = models.DateField( blank=True, null = True)
    date_of_contract_unconditional = models.DateField( blank=True, null = True)
    date_of_settlement = models.DateField( blank=True, null = True)
    commission1 = models.IntegerField(default=0)
    commission2 = models.IntegerField(default=0)
    tyler_commission1 = models.IntegerField(default=0)
    tyler_commission2 = models.IntegerField(default=0)
    email = models.EmailField(blank=True)
    note = models.CharField(max_length=100,blank=True)
    letter1 = models.CharField(max_length=40,blank=True)
    letter2 = models.CharField(max_length=40,blank=True)
    letter3 = models.CharField(max_length=40,blank=True)
    modified_date = models.DateTimeField(default =timezone.now(), blank=True)
    class Meta:
        ordering = ["-modified_date"]
        
    def __unicode__(self):        
        return unicode(self.project) + ' '+ unicode(self.project_lot)

    def save(self):        
        self.modified_date = timezone.now()       
        super(Purchase,self).save()