from .models import News
from news_sentiment import aggregator

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'feeds/index.html'
    context_object_name = 'all_feeds'

    def get_queryset(self):
            aggregator.NewsAggregator.get_live_feeds(aggregator.NewsAggregator())
            return News.objects.order_by('-published')