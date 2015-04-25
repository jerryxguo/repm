from django import forms
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from import_export import fields
from daterange_filter.filter import DateRangeFilter
from sales.models import Purchase

from config.models import Project
from config.models import Property
from config.models import Client
from config.models import Sales
from config.models import Office

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
        widgets = {
                'date_of_EOI_sent': {'format': '%d/%m/%Y'},
                'date_of_contract_received': {'format': '%d/%m/%Y'},
                'date_of_contract_signed': {'format': '%d/%m/%Y'},
                'date_of_contract_exchanged': {'format': '%d/%m/%Y'},
                'date_of_contract_unconditional': {'format': '%d/%m/%Y'},
                'date_of_BOD_paid': {'format': '%d/%m/%Y'},
                'date_of_settlement': {'format': '%d/%m/%Y'},
                'commission_1_date': {'format': '%d/%m/%Y'},
                'commission_2_date': {'format': '%d/%m/%Y'},
                'tyler_commission_1_date': {'format': '%d/%m/%Y'},
                'tyler_commission_2_date': {'format': '%d/%m/%Y'},
                }
        export_order = ('id','office','sales', 'project','project_lot','lot_price','client','deposit','solicitor', \
        'date_of_EOI_sent','date_of_contract_received','date_of_contract_signed','date_of_contract_exchanged','date_of_BOD_paid','date_of_contract_unconditional',\
        'date_of_settlement','commission_1','commission_1_date', 'commission_2',\
        'commission_2_date','tyler_commission_1','tyler_commission_1_date','tyler_commission_2','tyler_commission_2_date','bonus',\
        'note','letter1','letter1_date','letter2','letter2_date','letter3', 'letter3_date')
        #fields = ('id', 'project', 'office','client', 'sales')
        #exclude = ['tyler_commission_1', 'tyler_commission_2', 'commission_1', 'commission_2']
     
    project = fields.Field(column_name='project', attribute='project', widget=widgets.ForeignKeyWidget(Project,'name')) 
    project_lot = fields.Field(column_name='project_lot', attribute='project_lot', widget=widgets.ForeignKeyWidget(Property,'lot'))
    
    office = fields.Field(column_name='office', attribute='office', widget=widgets.ForeignKeyWidget(Office,'city'))
    sales = fields.Field(column_name='sales', attribute='sales', widget=widgets.ForeignKeyWidget(Sales,'full_name'))
    client = fields.Field(column_name='client', attribute='client', widget=widgets.ForeignKeyWidget(Client,'full_name'))
    
       
'''
    def dehydrate_project(self, Purchase):
        return unicode(Purchase.project) if Purchase.project else None
    def dehydrate_office(self, Purchase):
        logger.debug('Purchase.office = %s',unicode(Purchase.office))
        return unicode(Purchase.office) if Purchase.office else None    
    def dehydrate_client(self, Purchase):
        return unicode(Purchase.client) if Purchase.client else None
    def dehydrate_sales(self, Purchase):
        return unicode(Purchase.sales) if Purchase.sales else None
    def dehydrate_project_lot(self, Purchase):
        return unicode(Purchase.project_lot) if Purchase.project_lot else None
'''
'''        
class PurchaseAdminForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        exclude = ['client_email']
    def clean(self):       
        sales = Sales.objects.get(office=self.cleaned_data['office'], full_name= self.cleaned_data['sales'])
        logger.debug('clean.status %s, self.__original_status = %s,', self.cleaned_data['office'], self.cleaned_data['sales'])  
        if not sales:
            raise forms.ValidationError(self.cleaned_data['office'].city + ' doesn\'t have sales named by'+ self.cleaned_data['sales'].full_name + '. Change office or sales selection please!')
        else:
            logger.debug('self.status %s, self.__original_status = %s,', self.cleaned_data['office'], self.cleaned_data['sales'])  
        property = Property.objects.get(project=self.cleaned_data['project'], lot= self.cleaned_data['project_lot'].lot)
        if not property:
            raise forms.ValidationError(self.cleaned_data['project'].name + ' doesn\'t have the lot:'+ self.cleaned_data['project_lot'].lot + '. Change project or lot selection please!')
        return self.cleaned_data
'''

class PurchaseAdmin(ImportExportModelAdmin):
    fieldsets = [
        ('Sales Info',       {'fields': (('office','sales'),)}), 
        ('Property Info',    {'fields': (('project','project_lot',),)}),
        ('Purchasing Info',  {'fields': (('client','client_email','deposit'),('solicitor'), ('date_of_EOI_sent','date_of_contract_received','date_of_contract_signed','date_of_contract_exchanged',),('date_of_BOD_paid','date_of_contract_unconditional','date_of_settlement'),)}), 
        ('Commission Info',  {'fields': (('commission_1','commission_1_date'), ('commission_2','commission_2_date'),('tyler_commission_1','tyler_commission_1_date'),('tyler_commission_2','tyler_commission_2_date'),('bonus',))}), 
        ('Others',      {'fields': (('note'),('letter1','letter1_date'),('letter2','letter2_date'),('letter3', 'letter3_date'))}), 
        
    ]
    readonly_fields = ('client_email',)
    list_display = ('project', 'project_lot', 'price', 'office','sales', 'client', 'client_email','deposit','solicitor','date_of_EOI_sent','date_of_BOD_paid','date_of_contract_unconditional','date_of_settlement','note','letter1','letter2','letter3')
    list_filter = ['project','office','sales',('date_of_contract_received',DateRangeFilter), ('date_of_contract_signed', DateRangeFilter),('date_of_contract_exchanged', DateRangeFilter),('date_of_contract_unconditional', DateRangeFilter),('date_of_settlement', DateRangeFilter),('date_of_EOI_sent', DateRangeFilter)]
    search_fields = ['project__name','sales__full_name', 'client__full_name', 'office__city']
    
    resource_class = PurchaseResource
#    form = PurchaseAdminForm
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "office":
            kwargs["queryset"] = Office.objects.order_by('city')
        if db_field.name == "project":
            kwargs["queryset"] = Project.objects.order_by('name')
        if db_field.name == "client":
            kwargs["queryset"] = Client.objects.order_by('full_name')        
        return super(PurchaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
     
admin.site.register(Purchase,PurchaseAdmin)

