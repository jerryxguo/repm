import datetime
from django.db import models
from django.core.exceptions import ValidationError
from config.models import Sales
from config.models import Plan
from config.models import Property
from sales.models import Purchase
from sales.models import Client
from sales.models import Office
from django.core.mail import send_mail

import logging
logger = logging.getLogger(__name__)

   
# update sales's achievement
def update_sales(instance):       
    sales = Sales.objects.get(full_name=instance.sales)
    #send_mail('Subject here', 'Here is the message.', 'xguo10@tpg.com.au',['xguo10@tpg.com.au'], fail_silently=False)
    if sales:
        purchases = Purchase.objects.filter(sales=instance.sales)
        if purchases:
            if len(purchases) != sales.number_of_sales:
                #send_mail('Subject here', 'Here is the message.', 'xguo10@tpg.com.au',['xguo10@tpg.com.au'], fail_silently=False)
                print 'send email'
                
            sales.number_of_sales = len(purchases)
            
            bonus_plan = Plan.objects.all().order_by('number_of_sales')
            accum_bonus = 0
            annual_bonus = 0
            
            for plan in bonus_plan:
                if plan.plan_type=='AB':
                    if sales.number_of_sales>=plan.number_of_sales:
                        accum_bonus = accum_bonus + plan.bonus
                else:
                    delta  = datetime.date.today() - sales.start_date
                    #logger.debug('delta.days =  %s ',  str(delta.days))
                    if delta.days >=365:
                        #logger.debug('plan.year =  %s ',  plan.year)
                        if plan.year:
                            p = Purchase.objects.filter(sales=instance.sales, date_of_EOI_sent__year=plan.year)                        
                            sales.number_of_year_sales = len(p)
                            #logger.debug('sales.number_of_year_sales =  %s ',  str(sales.number_of_year_sales))
                            if sales.number_of_year_sales>=plan.number_of_sales and sales.on_board is True:
                                annual_bonus = annual_bonus + plan.bonus*plan.number_of_sales
                
            sales.year_bonus = annual_bonus
            sales.accumulation_bonus = accum_bonus            
        else:
            sales.accumulation_bonus = 0
            sales.year_bonus = 0
            sales.number_of_sales = 0
            sales.number_of_year_sales = 0
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
    
def save_purchase(sender, instance, created, raw, using, update_fields, **kwargs):
    logger.debug('DO add_sales %s, raw = %s, update_fields = %s', instance.sales, raw, update_fields)     
    if instance.office.independent is False:
        update_sales(instance)
    update_client(instance)
    update_property(instance)
   
    
def delete_purchase(sender, instance, using, **kwargs):
    logger.debug('DO delete_sales %s, client = %s, lot = %s', instance.sales, instance.client, instance.project_lot)
    if instance.office.independent is False:
        update_sales(instance)
    update_client(instance)
    update_property(instance)        
           

models.signals.post_save.connect(save_purchase, sender=Purchase)
models.signals.post_delete.connect(delete_purchase, sender=Purchase)


