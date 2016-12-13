import os
import sys
import django

path = (os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
print(path)
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "robo_app.settings")

django.setup()

from robo_app.models import NewsGroup, Asset
from robo_app.news_sentiment.aggregator import NewsAggregator

for newsGroup in NewsGroup.objects.all():
    symbol = (Asset.objects.get(id=newsGroup.asset_id)).symbol
    NewsAggregator().get_live_feeds(keyword=symbol, newsGroup=newsGroup)
