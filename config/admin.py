from django.contrib import admin

from config.models import Project
from config.models import Property
from config.models import Client
from config.models import Sales
from config.models import Office
from config.models import Bonus

# Register your models here.
#########################################
#sales#

class SalesInline(admin.TabularInline):
    fieldsets = [
        ('Sales Info',    {'fields': (('full_name','email','mobile','start_date', 'total_sales','accumulated_bonus','bonus_paid','date_of_paid','bonus_unpaid','leader','director','on_board','referrer'),)}),       
    ]
    readonly_fields = ('total_sales','accumulated_bonus','bonus_unpaid',)
    model = Sales
    extra = 3
        

class OfficeAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Office', {'fields': (('city','independent',),('address','country'),('phone'),)}),
    ]
    list_display = ('city', 'independent', 'phone')
    inlines = [SalesInline]
    
admin.site.register(Office,OfficeAdmin)
###############################
class SalesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Sales Info',    {'fields': (('office','full_name'),('email','mobile',),)}),       
    ]
    
   
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    
admin.site.register(Sales,SalesAdmin)
#########################################
#########################################
#property#

class PropertyInline(admin.TabularInline):
    fieldsets = [
        ('Property Info',    {'fields': (('project','lot','price','sales','client','status','status_date'),)}),       
    ]
    model = Property
    extra = 3
    readonly_fields = ('status_date','sales','client')    

class ProjectAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Project', {'fields': (('name','address','city','state'),)}),
    ]
    list_display = ('name','address','city','state')
    inlines = [PropertyInline]
    
admin.site.register(Project,ProjectAdmin)
###############################
class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Property Info',    {'fields': (('project','lot','price',),)}),       
    ]
    
    
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    
admin.site.register(Property,PropertyAdmin)
#########################################
#client#       

class ClientAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Client Info',    {'fields': (('full_name','email','mobile'),)}),
        ('Property Info',   {'fields': (('number_of_properties',),)}),
    ]
    readonly_fields = ('number_of_properties',)
    list_display = ('full_name','email','mobile','number_of_properties')
    
admin.site.register(Client,ClientAdmin)


class BonusAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Bonus Plan',    {'fields': (('number_of_sales','bonus'),)}),
       
    ]
    list_display = ('number_of_sales','bonus')
    
admin.site.register(Bonus,BonusAdmin)