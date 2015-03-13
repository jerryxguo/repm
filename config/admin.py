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
    
    readonly_fields = ('bonus_unpaid',)
    model = Sales
    extra = 3
        

class OfficeAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Office',               {'fields': (('city'),('address','state','country'),('phone'),)}),
    ]
    inlines = [SalesInline]
    
admin.site.register(Office,OfficeAdmin)

#########################################
#property#

class PropertyInline(admin.TabularInline):
    model = Property
    extra = 3
    readonly_fields = ('date',)    

class ProjectAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Project',               {'fields': (('name','address','city','state'),)}),
    ]
    list_display = ('name','address','city','state')
    inlines = [PropertyInline]
    
admin.site.register(Project,ProjectAdmin)

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