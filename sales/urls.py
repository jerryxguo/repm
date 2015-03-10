from django.conf.urls import patterns,url
from sales import views


urlpatterns = patterns('',
    url(r'^purchase/$',views.PurchaseView.as_view(), name='purchase'),
    url(r'^client/$',views.ClientView.as_view(), name='client'),
    url(r'^sales/$',views.SalesView.as_view(), name='sales'),
    
    
)


