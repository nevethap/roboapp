from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Quote

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'all_quotes'

    def get_queryset(self):
        return Quote.objects.all()