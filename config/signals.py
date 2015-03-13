
from django.db import models
from django.core.exceptions import ValidationError
from config.models import Sales
from config.models import Bonus
from config.models import Property
from sales.models import Purchase
from sales.models import Client
from django.core.mail import send_mail

import logging
logger = logging.getLogger(__name__)

   
# update sales's achievement
def update_sales(instance):    
    purchases = Purchase.objects.filter(sales=instance.sales)
    sales = Sales.objects.get(full_name=instance.sales)
    
    if purchases and sales:
        if len(purchases) != sales.number_of_sales:
            sales.number_of_sales = len(purchases)
            bonus_plan = Bonus.objects.all().order_by('number_of_sales')
            bonus = 0
            
            for plan in bonus_plan:
                if(sales.number_of_sales>=plan.number_of_sales):
                    bonus = bonus + plan.bonus
            if sales.accumulation_bonus!= bonus:
                sales.accumulation_bonus = bonus
                #send_mail('Subject here', 'Here is the message.', 'xguo10@tpg.com.au',['xguo10@tpg.com.au'], fail_silently=False)
            sales.save()
            
# update client's holdings           
def update_client(instance):
    purchases = Purchase.objects.filter(client=instance.client)
    client = Client.objects.get(full_name=instance.client)
    if purchases and client:
        if len(purchases) != client.number:
            client.number = len(purchases)
            client.save()
            
# update property           
def update_property(instance):
    
    logger.debug('update_project %s propertys = %s type = %s, ', instance.project.name, instance.project_lot, type(instance.project_lot.lot))  
    property = Property.objects.get(project=instance.project.name, lot= instance.project_lot.lot)
    property.lot_sales = instance.sales
    property.lot_client = instance.client
    property.save()
    
def save_sales(sender, instance, created, raw, using, update_fields, **kwargs):
    logger.debug('DO add_sales %s, raw = %s, update_fields = %s', instance.sales, raw, update_fields)     
    
    if created:
        update_sales(instance)
        update_client(instance)
        update_property(instance)
    else:       
        if 'sales' in update_fields:
            update_sales(instance)
        if 'client' in update_fields:
            update_client(instance)    
        if 'project_lot' in update_fields or 'project' in update_fields:
            update_property(instance)
        
def delete_sales(sender, instance, using, **kwargs):
    logger.debug('DO delete_sales %s, client = %s, lot = %s', instance.sales, instance.client, instance.project_lot)
    update_sales(instance)
    update_client(instance)
    update_property(instance)        
           

models.signals.post_save.connect(save_sales, sender=Purchase)
models.signals.post_delete.connect(delete_sales, sender=Purchase)


