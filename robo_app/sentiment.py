import os
import sys
import django

path = (os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
print(path)
sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "robo_app.settings")

django.setup()

from robo_app.models import NewsGroup
from robo_app.news_sentiment.aggregator import NewsAggregator

keywords = {1: ["Vanguard large cap index adm"], 2: ['US aggregate bond'], 3: ['SPDR Gold Shares'],
            4: ['United States oil'], 5: ['Chevron Corporation'], 6: ['Apple Inc'], 7: ['Valero energy corporation'],
            8: ['Berkshire Hathaway'], 9: ['Facebook'],
            10: ["Google", "Alphabet Inc", "GOOG"]}
# for newsGroup in NewsGroup.objects.all():
#     NewsAggregator().get_live_feeds(keywords=keywords[newsGroup.id], newsGroup=newsGroup)
#     break


NewsAggregator().run(NewsGroup.objects.get(asset_id = 6))