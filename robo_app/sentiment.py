import os
import sys

path = os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0]
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "robo_app.settings")

import django

django.setup()

from robo_app.models import NewsGroup
from robo_app.news_sentiment.aggregator import NewsAggregator

keywords = {1: ["Oil"], 2: ["Google", "Alphabet Inc", "GOOGL"]}
for newsGroup in NewsGroup.objects.all():
    NewsAggregator().get_live_feeds(keywords=keywords[newsGroup.id], newsGroup=newsGroup)
