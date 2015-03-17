import datetime
from django import forms
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey
from config.models import Project
from config.models import Property
from config.models import Client
from config.models import Sales
from config.models import Office


import logging
logger = logging.getLogger(__name__)
# Create your models here.
class Purchase(models.Model):
    project = models.ForeignKey(Project)
    project_lot = ChainedForeignKey(Property,chained_field="project",chained_model_field="project",  show_all=False, auto_choose=True)
   
    office = models.ForeignKey(Office)
    sales = ChainedForeignKey(Sales,chained_field="office",chained_model_field="office",  show_all=False, auto_choose=True)
    client = models.ForeignKey(Client, to_field ='full_name')
    deposit = models.IntegerField(default=0, null=True)
    solicitor = models.CharField(max_length=40,blank=True)
    date_of_EOI_sent = models.DateField( 'Date EOI Sent', blank=True, null = True)
    date_of_contract_received = models.DateField( blank=True, null = True)
    date_of_contract_signed = models.DateField( blank=True, null = True)
    date_of_contract_exchanged = models.DateField( blank=True, null = True)
    date_of_BOD_paid  = models.DateField( blank=True, null = True)
    date_of_contract_unconditional = models.DateField( blank=True, null = True)
    date_of_settlement = models.DateField( blank=True, null = True)
    commission_1 = models.IntegerField(default=0, null = True,blank=True)
    commission_1_date = models.DateField( blank=True, null = True)
    commission_2 = models.IntegerField(default=0,null = True,blank=True)
    commission_2_date = models.DateField( blank=True, null = True)
    def _get_commission_total(self):
        if self.commission_1 is None:
            self.commission_1 = 0
        if self.commission_2 is None:
            self.commission_2 = 0
        return (self.commission_1 + self.commission_2)
    commission_total = property(_get_commission_total)
    tyler_commission_1 = models.IntegerField(default=0,null = True,blank=True)
    tyler_commission_2 = models.IntegerField(default=0,null = True,blank=True)
    tyler_commission_1_date = models.DateField( blank=True, null = True)
    tyler_commission_2_date = models.DateField( blank=True, null = True)
    def _get_tyler_commission_total(self):
        if self.tyler_commission_1 is None:
            self.tyler_commission_1 = 0
        if self.tyler_commission_2 is None:
            self.tyler_commission_2 = 0    
        return (self.tyler_commission_1 + self.tyler_commission_2)
    tyler_commission_total = property(_get_tyler_commission_total)
    bonus = models.IntegerField(default=0,null = True,blank=True)
    def _get_client_email(self):
        return self.client.email 
    client_email = property(_get_client_email)
    note = models.CharField(max_length=100,blank=True)
    letter1 = models.CharField(max_length=40,blank=True)
    letter2 = models.CharField(max_length=40,blank=True)
    letter3 = models.CharField(max_length=40,blank=True)
    modified_date = models.DateTimeField(default =timezone.now(), blank=True)
    
    lot_price = models.IntegerField(default=0, null=True)
    def _get_lot_price(self):       
        return self.lot_price 
    price = property(_get_lot_price)
    class Meta:
        ordering = ["-modified_date"]
        verbose_name_plural  = 'Sale Records'
        verbose_name  = 'Sale'
        unique_together = (("project", "project_lot"),)
    def __unicode__(self):        
        return unicode(self.project) + ' '+ unicode(self.project_lot)

    def save(self):        
        self.modified_date = timezone.now()
        super(Purchase,self).save()
    
    def clean(self):       
        logger.debug('clean.office %s, self.sales = %s,', self.office.city, self.sales.full_name) 
        sales = Sales.objects.filter(office=self.office.city, full_name= self.sales.full_name)
       
        if not sales:
            raise forms.ValidationError('Office:\''+ self.office.city + '\' doesn\'t have the sales named by: '+ self.sales.full_name + '. Change office or sales selection please!')
        
        property = Property.objects.filter(project=self.project.name, lot= self.project_lot.lot)
        if not property:
            raise forms.ValidationError('Project:\''+self.project.name + '\' doesn\'t have the lot: '+ str(self.project_lot.lot) + '. Change project or lot selection please!')
        
        super(Purchase,self).clean() 
