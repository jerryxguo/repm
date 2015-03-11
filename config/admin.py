from django.contrib import admin

from config.models import Project
from config.models import Property
from config.models import Client
from config.models import Sales
from config.models import Office
# Register your models here.
#########################################
#sales#

class SalesInline(admin.TabularInline):
    model = Sales
    extra = 5
        

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
    extra = 5
        

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
        ('Client Info',    {'fields': (('full_name','email','mobile'),)}),
       
    ]
    list_display = ('full_name','email','mobile')
    
admin.site.register(Client,ClientAdmin)