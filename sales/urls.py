from django.conf.urls import patterns,url
from sales import views


urlpatterns = patterns('',
    url(r'^$',views.IndexView.as_view(), name='index'),
    #url(r'^$', views.index, name='index'),    
)


