import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey
from django.conf import settings
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
    start_date = models.DateField(default =timezone.now(), blank=True, null = True)
    
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
        verbose_name_plural  = 'Consultants'
        verbose_name  = 'Consultant:'
        unique_together = (("office", "full_name"),)

'''   
    def save(self, *args, **kwargs):
        if self.leader is True:
            try:
                temp = Sales.objects.get(leader=True)
                if self != temp:
                    temp.leader = False
                    temp.save()
            except Sales.DoesNotExist:
                pass
        super(Sales, self).save(*args, **kwargs)        
'''            
class Client(models.Model):
    full_name = models.CharField(primary_key = True, max_length=30, unique = True)
    number = models.IntegerField(default=0)
    
    email = models.EmailField(max_length=50, blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True)
   
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
        
    status = models.CharField(max_length=20,default ='----')
    def _get_property_status(self):        
        return self.status
    property_status = property(_get_property_status)    
    modification_date = models.DateField( blank=True, null = True)    
    def _get_date(self):        
        return self.modification_date
        
    status_date = property(_get_date)
    def __unicode__(self):
        return str(self.lot)
    class Meta:
        verbose_name_plural  = 'Properties'
        unique_together = (("project", "lot"),)


        
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
        verbose_name_plural  = 'Bonus Plan'
        verbose_name  = 'Bonus Plan'
        
    def __unicode__(self):
        return 'Bonus Plan'

class Notification(models.Model):
    NOTIFY_TYPE_CHOICES = (
        ('NS', 'NOTIFY_CONSULTANT'),     
        ('NA', 'NOTIFY_ADMIN'),
        ('N1', 'NOTIFY_CLIENT_LETTER_1'),
        ('N2', 'NOTIFY_CLIENT_LETTER_2'),
        ('N3', 'NOTIFY_CLIENT_LETTER_3'),
    )
    notify_type = models.CharField(max_length=2, choices=NOTIFY_TYPE_CHOICES, default ='NS') 
    subject = models.CharField(max_length=100, blank=True, null = True)
    sender = models.CharField(max_length=100, blank=True, null = True)
    cc_list = models.CharField(max_length=500, blank=True, null = True) 
    bcc_list  = models.CharField(max_length=500, blank=True, null = True) 
    receiver = models.CharField(max_length=100, blank=True, null = True)
    template = models.FilePathField(path=settings.TEMPLATE_DIRS[1])
    
    class Meta:
        verbose_name_plural  = 'Notify'
        verbose_name  = 'Notify'
        
    def __unicode__(self):
        return 'Notify' 