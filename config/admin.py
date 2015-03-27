from django.contrib import admin



from config.models import Project
from config.models import Property
from config.models import Client
from config.models import Sales
from config.models import Office
from config.models import Plan
from config.models import Notification
# Register your models here.
#########################################
#sales#

class SalesInline(admin.StackedInline):
    fieldsets = [
        ('Personal Info',    {'fields': (('full_name','email','mobile'),('start_date', 'referrer','leader','director','on_board',),)}), 
        ('Bonus Info',    {'fields': (('annual_sales','annual_bonus','total_sales','accumulated_bonus','bonus_paid','date_of_paid','accum_bonus_unpaid'),),'classes': ['grp-collapse grp-open']}),       
    ]
    readonly_fields = ('annual_sales','total_sales','accumulated_bonus','accum_bonus_unpaid','annual_bonus')
    model = Sales
    extra = 0
        

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
        ('Sales Info',    {'fields': (('office','full_name'),('email','mobile',),('start_date','referrer'),('leader','director'))}),       
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
        ('Property Info',    {'fields': (('project','lot','price','sales','client','property_status','status_date'),)}),       
    ]
    model = Property
    extra = 0
    readonly_fields = ('property_status','status_date','sales','client')    

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


class PlanAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Bonus Plan',    {'fields': (('plan_type', 'year', 'number_of_sales', 'bonus'),)}),
       
    ]
    list_display = ('plan_type', 'year', 'number_of_sales','bonus')
    
admin.site.register(Plan,PlanAdmin)

class NotificationAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Notification Configuration',    {'fields': (('notify_type', 'subject', 'sender', 'receiver', 'cc_list', 'bcc_list', 'template'),)}),
       
    ]
    list_display = ('notify_type', 'subject', 'sender', 'receiver','cc_list', 'bcc_list', 'template')
    
admin.site.register(Notification,NotificationAdmin)