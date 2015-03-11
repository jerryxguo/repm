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
    
    def __unicode__(self):
        return self.full_name 

        
class Purchase(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    project_lot = ChainedForeignKey(Property,chained_field="project",chained_model_field="project",  show_all=False, auto_choose=True, blank=True, null=True)
    office = models.ForeignKey(Office, blank=True, null=True)
    sales = ChainedForeignKey(Sales,chained_field="office",chained_model_field="office",  show_all=False, auto_choose=True, blank=True, null=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    deposit = models.IntegerField(default=0, null=True)
    solicitor = models.CharField(max_length=40,blank=True)
    date_of_EOI_sent = models.DateField( 'Date EOI Sent', blank=True, null = True)
    date_of_contract_received = models.DateField( blank=True, null = True)
    date_of_contract_signed = models.DateField( blank=True, null = True)
    date_of_contract_exchanged = models.DateField( blank=True, null = True)
    date_of_BOD_paid  = models.DateField( blank=True, null = True)
    date_of_contract_unconditional = models.DateField( blank=True, null = True)
    date_of_settlement = models.DateField( blank=True, null = True)
    commission_1 = models.IntegerField(default=0, null = True)
    commission_1_date = models.DateField( blank=True, null = True)
    commission_2 = models.IntegerField(default=0,null = True)
    commission_2_date = models.DateField( blank=True, null = True)
    def _get_commission_total(self):
        if self.commission_1 is None:
            self.commission_1 = 0
        if self.commission_2 is None:
            self.commission_2 = 0
        return (self.commission_1 + self.commission_2)
    commission_total = property(_get_commission_total)
    tyler_commission_1 = models.IntegerField(default=0,null = True)
    tyler_commission_2 = models.IntegerField(default=0,null = True)
    tyler_commission_1_date = models.DateField( blank=True, null = True)
    tyler_commission_2_date = models.DateField( blank=True, null = True)
    def _get_tyler_commission_total(self):
        if self.tyler_commission_1 is None:
            self.tyler_commission_1 = 0
        if self.tyler_commission_2 is None:
            self.tyler_commission_2 = 0    
        return (self.tyler_commission_1 + self.tyler_commission_2)
    tyler_commission_total = property(_get_tyler_commission_total)
    bonus = models.IntegerField(default=0,null = True)
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