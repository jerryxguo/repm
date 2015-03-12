
from django.db import models
from django.core.exceptions import ValidationError
from config.models import Sales
from config.models import Bonus
from sales.models import Purchase
from django.core.mail import send_mail

import logging
logger = logging.getLogger(__name__)

       
def send_email(sender, instance, created, **kwargs):
    logger.debug('DO send_email %s', instance.full_name)
    bonus_plan = Bonus.objects.all().order_by('number_of_sales')
    bonus = 0
    
    for plan in bonus_plan:
        if(instance.number_of_sales>=plan.number_of_sales):
            bonus = bonus + plan.bonus
    if instance.accumulation_bonus!= bonus:
        instance.accumulation_bonus = bonus
        instance.save()
        #send_mail('Subject here', 'Here is the message.', 'xguo10@tpg.com.au',['xguo10@tpg.com.au'], fail_silently=False)

def update_sales(instance):
    purchases = Purchase.objects.filter(sales=instance.sales)
    sales = Sales.objects.get(full_name=instance.sales)
    if purchases and sales:
        if len(purchases) != sales.number_of_sales:
            sales.number_of_sales = len(purchases)
            sales.save()
        
def add_sales(sender, instance, created, **kwargs):
    logger.debug('DO add_sales %s', instance.sales)     
    update_sales(instance)

def delete_sales(sender, instance, using, **kwargs):
    logger.debug('DO delete_sales %s', instance.sales)     
    update_sales(instance)

            
           
        
models.signals.post_save.connect(send_email, sender=Sales) 
models.signals.post_save.connect(add_sales, sender=Purchase)
models.signals.post_delete.connect(delete_sales, sender=Purchase)