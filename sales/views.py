
import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from sales.models import Purchase
from config.models import Client
from config.models import Sales
# Create your views here.
# Create your views here.
class PurchaseView(generic.ListView):
    template_name = 'sales/purchase.html'
    context_object_name = 'latest_purchase_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Purchase.objects.order_by('project')

class ClientView(generic.ListView):
    template_name = 'sales/client.html'
    context_object_name = 'latest_client_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Client.objects.all()

class SalesView(generic.ListView):
    template_name = 'sales/sales.html'
    context_object_name = 'latest_sales_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Sales.objects.order_by('office')