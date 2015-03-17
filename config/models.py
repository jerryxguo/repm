import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey

import logging
logger = logging.getLogger(__name__)

# Create your models here.


class Office(models.Model):
    city = models.CharField(max_length=20, unique=True, primary_key = True)
    independent = models.BooleanField(default=False)
    address = models.CharField(max_length=40, blank=True, null=True)   
    
    country = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField('Contact Phone', max_length=10, blank=True, null=True)
    def __unicode__(self):
        return self.city
    class Meta:
        verbose_name_plural  = 'Office'

        

class Sales(models.Model):
    full_name = models.CharField(max_length=30, unique=True, primary_key = True)
    
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    office = models.ForeignKey(Office)
    start_date = models.DateField( blank=True, null = True)
    
    number_of_year_sales  = models.IntegerField(default=0, blank=True, null=True)
    def _get_annual_sales(self):        
        return self.number_of_year_sales 
    annual_sales = property(_get_annual_sales)
    
    year_bonus = models.IntegerField(default=0, blank=True,  null=True)  
    def _get_annual_bonus(self):        
        return self.year_bonus 
    annual_bonus = property(_get_annual_bonus)
    
    number_of_sales = models.IntegerField(default=0, blank=True, null=True)
    def _get_total_sales(self):        
        return self.number_of_sales 
    total_sales = property(_get_total_sales)
    
    accumulation_bonus = models.IntegerField(default=0, blank=True,  null=True)  
    def _get_accumulated_bonus(self):        
        return self.accumulation_bonus 
    accumulated_bonus = property(_get_accumulated_bonus)
    bonus_paid = models.IntegerField('Accum bonus paid',default=0, blank=True, null=True)
    date_of_paid = models.DateField( blank=True, null = True)

    def _get_accum_bonus_unpaid(self):
        if self.accumulation_bonus is None:
            self.accumulation_bonus = 0
        if self.bonus_paid is None:
            self.bonus_paid = 0    
        return (self.accumulation_bonus - self.bonus_paid)
    accum_bonus_unpaid = property(_get_accum_bonus_unpaid)
    
    leader = models.BooleanField(default=False)
    director =  models.BooleanField(default=False)
    on_board = models.BooleanField(default=True)   
    
    referrer = models.CharField('Referer', max_length=30, blank=True, null=True)
    def __unicode__(self):
        return self.full_name
    class Meta:        
        verbose_name_plural  = 'Sales'
        unique_together = (("office", "full_name"),)
            
            
class Client(models.Model):
    full_name = models.CharField(max_length=30, unique = True)
    number = models.IntegerField(default=0)
    
    email = models.EmailField(blank=True, unique = True)
    mobile = models.CharField(max_length=10,blank=True)
   
    def _get_number_of_properties(self):        
        return self.number
        
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
    project = models.ForeignKey(Project)
    lot = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    lot_sales = models.ForeignKey(Sales, blank=True, null=True)
    lot_client = models.ForeignKey(Client, blank=True, null=True)
    def _get_sales(self):
        return self.lot_sales        
    sales = property(_get_sales)
    def _get_client(self):
        return self.lot_client        
    client = property(_get_client)
    
    STATUS_CHOICES = (
        ('--', '------'),
        ('CR', 'Contract Received'),
        ('CS', 'Contract Signed'),
        ('CE', 'Contract Exchanged'),
        ('CU', 'Contract Unconditional'),
        ('PS', 'Property Settled'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default ='--')    
    modification_date = models.DateField( blank=True, null = True)    
    def _get_date(self):        
        return self.modification_date
        
    status_date = property(_get_date)
    def __unicode__(self):
        return str(self.lot)
    class Meta:
        verbose_name_plural  = 'Properties'
        unique_together = (("project", "lot"),)
    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self.__original_status = self.status
    def save(self):
        logger.debug('self.status %s, self.__original_status = %s,', self.status, self.__original_status)   
        if self.status != self.__original_status:
            #logger.debug(' name changed - do something here')
            self.modification_date = timezone.now()            
            self.__original_status = self.status
        super(Property, self).save()
        
class Plan(models.Model):
    BONUS_TYPE_CHOICES = (
        ('LB', 'LOYALTY BONUS'),     
        ('AB', 'ACCUMULATION BONUS'),
    )
    plan_type = models.CharField(max_length=2, choices=BONUS_TYPE_CHOICES, default ='LB') 
    YEAR_CHOICES = []
    for r in range(datetime.datetime.now().year, (datetime.datetime.now().year+2)):
        YEAR_CHOICES.append((r,r))

    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=None , blank=True, null = True )

    number_of_sales = models.IntegerField('Least Number of Sales', default=0)    
    bonus = models.IntegerField('Bonus(AUS)', default=0)
    
    class Meta:
        verbose_name_plural  = 'Bonue Plan'
        verbose_name  = 'Bonue Plan'
        
    def __unicode__(self):
        return 'Bonus Plan'
