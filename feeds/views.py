from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import RSSFeed

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'feeds/index.html'
    context_object_name = 'all_feeds'

    def get_queryset(self):
        return RSSFeed.objects.all()