from django.views import generic
from .models import RSSFeed
from news_sentiment import aggregator
import time

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'feeds/index.html'
    context_object_name = 'all_feeds'

    def get_queryset(self):
            aggregator.NewsAggregator.get_live_feeds(aggregator.NewsAggregator(), ["Oil", "Google", "Alphabet Inc", "GOOGL"])
            return RSSFeed.objects.order_by('-published')