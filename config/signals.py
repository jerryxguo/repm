import datetime
from django.db import models
from django.core.exceptions import ValidationError
from config.models import Sales
from config.models import Plan
from config.models import Property
from sales.models import Purchase
from sales.models import Client
from sales.models import Office
from config.models import Notification
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

if "asyn_mail" in settings.INSTALLED_APPS:
    from asyn_mail import send_mail
else:
    from django.core.mail import send_mail
        
import logging
logger = logging.getLogger(__name__)

def notify_sales_by_email(instance):
    notify = Notification.objects.all()
    logger.debug('notify_sales_by_email ')
    for n in notify:
        if n.notify_type=='NS':
            receiver = n.receiver if n.receiver else instance.sales.email
            if n.template and receiver:
                
                start = n.template.find('template')
                plaintext = get_template(n.template[start+10:])
                
                d = Context({ 'salesname': instance.sales.full_name,'project': instance.project,'lot': instance.project_lot })
                text_content = plaintext.render(d)
                
                if ';' in n.bcc_list:
                    b = ';'               
                elif ',' in n.bcc_list:
                    b = ','
                else:
                    b = ' '
                bcc_list = tuple(n.bcc_list.split(b)) if n.bcc_list else None
                cc_list = tuple(n.cc_list.split(b)) if n.cc_list else None
                logger.debug('bcc = %s cc_list %s', bcc_list,cc_list)
                
                send_mail(n.subject, text_content, n.sender,[receiver], fail_silently=False, bcc=bcc_list, cc=cc_list, html=None)
  
# update sales's achievement
def update_sales(instance):       
   
    sales = Sales.objects.get(full_name=instance.sales)
    if sales:
        purchases = Purchase.objects.filter(sales=instance.sales)
        if purchases:
            #logger.debug('sales.number_of_sales =%s, purhcases = %s ', str(sales.number_of_sales), str(len(purchases)))
            if len(purchases) != sales.number_of_sales:
                #send_mail('Subject here', 'Here is the message.', 'xguo10@tpg.com.au',['xguo10@tpg.com.au'], fail_silently=False)
                notify_sales_by_email(instance)
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
    
    #logger.debug('update_project %s propertys = %s type = %s, ', instance.project.name, instance.project_lot, type(instance.project_lot.lot))  
    property = Property.objects.get(project=instance.project.name, lot= instance.project_lot.lot)
    property.lot_sales = instance.sales
    property.lot_client = instance.client
    if instance.date_of_settlement:
        property.modification_date = instance.date_of_settlement
        property.status ='Property Settled'
    elif instance.date_of_contract_unconditional:
        property.modification_date = instance.date_of_contract_unconditional
        property.status ='Contract Unconditional'
    elif instance.date_of_contract_exchanged:
        property.modification_date = instance.date_of_contract_exchanged
        property.status ='Contract Exchanged'
    elif instance.date_of_contract_signed:
        property.modification_date = instance.date_of_contract_signed
        property.status ='Contract Signed'
    elif instance.date_of_contract_received:
        property.modification_date = instance.date_of_contract_received
        property.status ='Contract Received'  
    else:
        property.modification_date = None
        property.status ='----'  
    property.save()
    
def save_purchase(sender, instance, created, raw, using, update_fields, **kwargs):
    #logger.debug('DO add_sales %s, raw = %s, update_fields = %s', instance.sales, raw, update_fields)
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

#####################################################################################365
from sales.models import letter_1
from sales.models import letter_2
from sales.models import letter_3



def letter_handler(sender, **kwargs):
   
    notify = Notification.objects.all()
    email = kwargs['email']
    logger.debug('email = %s', email if email else 'None')
    if sender == letter_1:
        logger.debug('sender = %s', 'letter_1')
        for n in notify:
            
            if n.notify_type=='N1':
                receiver = n.receiver if n.receiver else email
                if n.template and receiver:
                    start = n.template.find('template')
                    plaintext = get_template(n.template[start+10:])
                    
                    d = Context({ 'client': kwargs['client'],'project': kwargs['project'], 'consultant': kwargs['consultant'],'phone': kwargs['phone'], 'deposit': kwargs['deposit'] })
                    text_content = plaintext.render(d)
                    
                    if ';' in n.bcc_list:
                        b = ';'               
                    elif ',' in n.bcc_list:
                        b = ','
                    else:
                        b = ' '
                    bcc_list = tuple(n.bcc_list.split(b)) if n.bcc_list else None
                    cc_list = tuple(n.cc_list.split(b)) if n.cc_list else None                   
                    send_mail(n.subject, text_content, n.sender,[receiver], fail_silently=False, bcc=bcc_list, cc=cc_list, html=None)
               
    elif sender == letter_2:
        logger.debug('sender = %s', 'letter_2')
        for n in notify:
            if n.notify_type=='N2':
                receiver = n.receiver if n.receiver else email
                if n.template and receiver:
                    start = n.template.find('template')
                    plaintext = get_template(n.template[start+10:])
                    
                    d = Context({ 'client': kwargs['client'],'project': kwargs['project'], 'exchange_date': kwargs['exchange_date'] })
                    text_content = plaintext.render(d)
                    
                    if ';' in n.bcc_list:
                        b = ';'               
                    elif ',' in n.bcc_list:
                        b = ','
                    else:
                        b = ' '
                    bcc_list = tuple(n.bcc_list.split(b)) if n.bcc_list else None
                    cc_list = tuple(n.cc_list.split(b)) if n.cc_list else None                   
                    send_mail(n.subject, text_content, n.sender,[receiver], fail_silently=False, bcc=bcc_list, cc=cc_list, html=None)
        
    elif sender == letter_3:
        logger.debug('sender = %s', 'letter_3')
        for n in notify:
            if n.notify_type=='N3':
                receiver = n.receiver if n.receiver else email
                if n.template and receiver:
                    start = n.template.find('template')
                    plaintext = get_template(n.template[start+10:])
                    
                    d = Context({ 'client': kwargs['client'],'project': kwargs['project']})
                    text_content = plaintext.render(d)
                    
                    if ';' in n.bcc_list:
                        b = ';'               
                    elif ',' in n.bcc_list:
                        b = ','
                    else:
                        b = ' '
                    bcc_list = tuple(n.bcc_list.split(b)) if n.bcc_list else None
                    cc_list = tuple(n.cc_list.split(b)) if n.cc_list else None                   
                    send_mail(n.subject, text_content, n.sender,[receiver], fail_silently=False, bcc=bcc_list, cc=cc_list, html=None)
 
letter_1.connect(letter_handler, sender =letter_1)
letter_2.connect(letter_handler, sender =letter_2)
letter_3.connect(letter_handler, sender =letter_3)