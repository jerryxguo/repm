from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from import_export import fields

from sales.models import Purchase
from sales.models import Project
from sales.models import Property
from sales.models import Client
from sales.models import Sales
from sales.models import Office

import logging
logger = logging.getLogger(__name__)
#widget
class OneToManyForeignKeyWidget(widgets.Widget):
    def __init__(self, model, field='pk', *args, **kwargs):
        self.model = model
        self.field = field
        logger.debug('__init__: self.field =%s', self.field)
        super(OneToManyForeignKeyWidget, self).__init__(*args, **kwargs)

    def clean(self, value):
        
        if (value is None) or (not ',' in value):           
            return None
        values = value.split(',')
        
        dic  = dict(zip(self.field,values))    
            
        logger.debug('dic =%s', dic)
        return self.model.objects.get(**dic)
        
    def render(self, value):
    	if value is None:
            return ""
        # just let caller know the field exist
        return getattr(value, self.field[0])
        
        
#purchase# 
class PurchaseResource(resources.ModelResource):
    
   
    class Meta:
        model = Purchase
        #fields = ('id', 'project', 'office','client', 'sales')
        #exclude = ['tyler_commission1', 'tyler_commission2', 'commission1', 'commission2']
     
    project = fields.Field(column_name='project', attribute='project', widget=widgets.ForeignKeyWidget(Project,'name'))
    project_lot = fields.Field(column_name='project_lot', attribute='project_lot', widget=widgets.ForeignKeyWidget(Property,'lot'))
    office = fields.Field(column_name='office', attribute='office', widget=widgets.ForeignKeyWidget(Office,'city'))
    sales = fields.Field(column_name='sales', attribute='sales', widget=OneToManyForeignKeyWidget(Sales,['last_name','first_name']))
    client = fields.Field(column_name='client', attribute='client', widget=OneToManyForeignKeyWidget(Client,['last_name','first_name']))
   
    def dehydrate_project(self, Purchase):
        return unicode(Purchase.project) if Purchase.project else None
    def dehydrate_project_lot(self, Purchase):
        return unicode(Purchase.project_lot) if Purchase.project_lot else None
    def dehydrate_office(self, Purchase):
        return unicode(Purchase.office) if Purchase.office else None    
    def dehydrate_client(self, Purchase):
        return unicode(Purchase.client) if Purchase.client else None
    def dehydrate_sales(self, Purchase):
        return unicode(Purchase.sales) if Purchase.sales else None

class PurchaseAdmin(ImportExportModelAdmin):
    fieldsets = [
        ('Property Info',    {'fields': (('project','project_lot'),)}),       
        ('Sales Info',       {'fields': (('office','sales'),)}), 
        ('Purchasing Info',  {'fields': (('client','deposit','solicitor'), ('date_of_contract_received','date_of_contract_signed','date_of_contract_unconditional'),('date_of_EOI_sent','date_of_BOD_paid','date_of_settlement'),)}), 
        ('Commission Info',  {'fields': (('commission1','commission2'), ('tyler_commission1','tyler_commission2'),)}), 
        ('Others',      {'fields': (('email','note'),('letter1','letter2','letter3'),)}), 
        
    ]
    
    list_display = ('project', 'project_lot', 'office','sales', 'client', 'deposit','solicitor','date_of_contract_received','date_of_contract_signed','date_of_contract_unconditional','date_of_EOI_sent','date_of_BOD_paid','date_of_settlement','commission1','commission2', 'tyler_commission1','tyler_commission2','email','note','letter1','letter2','letter3')
    list_filter = ['project','office','sales','date_of_contract_received', 'date_of_contract_signed','date_of_contract_unconditional','date_of_settlement']
    search_fields = ['project','sales', 'client', 'office']
    
    resource_class = PurchaseResource
    
admin.site.register(Purchase,PurchaseAdmin)

#########################################
#sales#

class SalesInline(admin.TabularInline):
    model = Sales
    extra = 10
        

class OfficeAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Office',               {'fields': ['city']}),
    ]
    inlines = [SalesInline]
    
admin.site.register(Office,OfficeAdmin)

#########################################
#property#

class PropertyInline(admin.TabularInline):
    model = Property
    extra = 10
        

class ProjectAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Project',               {'fields': ['name']}),
    ]
    inlines = [PropertyInline]
    
admin.site.register(Project,ProjectAdmin)

#########################################
#client#       

class ClientAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Client Info',    {'fields': (('first_name','last_name','email','mobile'),)}),
       
    ]
    list_display = ('first_name','last_name','email','mobile')
    
admin.site.register(Client,ClientAdmin)