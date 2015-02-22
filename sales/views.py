
import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from sales.models import Purchase
# Create your views here.
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'sales/result.html'
    context_object_name = 'latest_sales_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Purchase.objects.order_by('project')