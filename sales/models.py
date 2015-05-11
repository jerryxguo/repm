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
from django.dispatch import Signal
letter_1 = Signal(providing_args=[ 'uId', 'date'])
letter_2 = Signal(providing_args=[ 'uId', 'date'])
letter_3 = Signal(providing_args=[ 'uId', 'date'])

import logging
logger = logging.getLogger(__name__)
# Create your models here.
class Purchase(models.Model):
    project = models.ForeignKey(Project)
    project_lot = ChainedForeignKey(Property,chained_field="project",chained_model_field="project",  show_all=False, auto_choose=True)
   
    office = models.ForeignKey(Office)
    sales = ChainedForeignKey(Sales,chained_field="office",chained_model_field="office",  show_all=False, auto_choose=True)
    client = models.ForeignKey(Client)
    deposit = models.IntegerField(null=True,blank=True)
    solicitor = models.CharField(max_length=40,blank=True)
    date_of_EOI_sent = models.DateField( 'Date Of EOI Sent', blank=True, null = True)
    date_of_contract_received = models.DateField( blank=True, null = True)
    date_of_contract_signed = models.DateField( blank=True, null = True)
    date_of_contract_exchanged = models.DateField( blank=True, null = True)
    date_of_BOD_paid  = models.DateField( blank=True, null = True)
    date_of_contract_unconditional = models.DateField( blank=True, null = True)
    date_of_settlement = models.DateField( blank=True, null = True)
    commission_1 = models.IntegerField( null = True,blank=True)
    comm_1_invoice_date = models.DateField( blank=True, null = True)
    commission_2 = models.IntegerField(null = True,blank=True)
    comm_2_invoice_date = models.DateField( blank=True, null = True)
    def _get_commission_total(self):
        if self.commission_1 is None:
            self.commission_1 = 0
        if self.commission_2 is None:
            self.commission_2 = 0
        return (self.commission_1 + self.commission_2)
    commission_total = property(_get_commission_total)
    tyler_commission_1 = models.IntegerField(null = True,blank=True)
    tyler_commission_2 = models.IntegerField(null = True,blank=True)
    tyler_comm_1_invoice_date = models.DateField( blank=True, null = True)
    tyler_comm_2_invoice_date = models.DateField( blank=True, null = True)
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
    letter1 = models.BooleanField(default=False)
    letter1_date = models.DateField('Sent Date', blank=True, null = True)
    letter2 = models.BooleanField(default=False)
    letter2_date = models.DateField('Sent Date',  blank=True, null = True)
    letter3 = models.BooleanField(default=False)
    letter3_date = models.DateField('Sent Date',  blank=True, null = True)
    withdrawal = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default =timezone.now(), blank=True)
    
    lot_price = models.IntegerField(default=0, null=True)
    def _get_lot_price(self):       
        return self.lot_price 
    price = property(_get_lot_price)
    class Meta:
        ordering = ["-modified_date"]
        verbose_name_plural  = 'Sale Records'
        verbose_name  = 'Sale'
        unique_together = (("project", "project_lot","client"),)
    def __unicode__(self):        
        return 'purchase'

    def save(self):        
        self.modified_date = timezone.now()
        self.lot_price = self.project_lot.price
        super(Purchase,self).save()
        if (self.__original_letter_1 is False or self.date_of_EOI_sent!=self.__original_EOI_date) and self.letter1 is True and self.date_of_EOI_sent is not None:
            letter_1.send(sender=letter_1, uId=self.id,  date = self.date_of_EOI_sent)
        if (self.__original_letter_2 is False or self.date_of_contract_exchanged!=self.__original_exchange_date) and self.letter2 is True and self.date_of_contract_exchanged is not None:
            logger.debug('send %s', 'letter_2')   
            letter_2.send(sender=letter_2, uId=self.id,  date = self.date_of_contract_exchanged)
        if (self.__original_letter_3 is False or self.date_of_settlement!=self.__original_settlement_date) and self.letter3 is True and self.date_of_settlement is not None:
            logger.debug('send %s', 'letter_3')   
            letter_3.send(sender=letter_3, uId=self.id,  date = self.date_of_settlement)
        
        self.__original_letter_1 = self.letter1
        self.__original_letter_2 = self.letter2    
        self.__original_letter_3 = self.letter3
        
    def clean(self):       
        logger.debug('clean.office %s, self.sales = %s,', self.office.city, self.sales.full_name) 
        sales = Sales.objects.filter(office=self.office, full_name= self.sales.full_name)
       
        if not sales:
            raise forms.ValidationError('Office:\''+ self.office.city + '\' doesn\'t have the sales named by: '+ self.sales.full_name + '. Change office or sales selection please!')
        
        property = Property.objects.filter(project=self.project, lot= self.project_lot.lot)
        if not property:
            raise forms.ValidationError('Project:\''+self.project.name + '\' doesn\'t have the lot: '+ str(self.project_lot.lot) + '. Change project or lot selection please!')
        
        super(Purchase,self).clean() 

    def __init__(self, *args, **kwargs):
        super(Purchase, self).__init__(*args, **kwargs)    
        self.__original_letter_1 = self.letter1
        self.__original_letter_2 = self.letter2
        self.__original_letter_3 = self.letter3
        self.__original_EOI_date = self.date_of_EOI_sent
        self.__original_exchange_date = self.date_of_contract_exchanged
        self.__original_settlement_date = self.date_of_settlement