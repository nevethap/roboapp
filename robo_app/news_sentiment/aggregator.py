import feedparser
from dateutil import parser
from datetime import datetime

from crawler import NewsCrawler
from robo_app import models
from robo_app.models import Asset
from robo_app.news_sentiment.sentiment import SentimentScorer


class NewsAggregator:
    def get_live_feeds(self, keyword, newsGroup):
        query = 'http://finance.yahoo.com/rss/headline?s=' + keyword
        feed = feedparser.parse(query)
        date_format = "%Y-%m-%d"
        count = 0
        sentiment_sum = 0
        for entry in feed.entries:
            try:
                title = entry.title_detail.value
                article_link = entry.link
                publishedString = entry.published
                published = parser.parse(publishedString)
                date = datetime.strptime(str(published.date()), date_format)
                article_text = NewsCrawler.crawl_article(NewsCrawler(), article_link)
                sentimentScore = SentimentScorer()
                sentiment_score = sentimentScore.scoreArticle(article_text)
                sentiment_sum += sentiment_score['Polarity']
                models.News(headline=title, timestamp=date, url=article_link,
                            sentiment=sentiment_score['Polarity'], asset=newsGroup.asset).save()
                count += 1
                if count == 5: break
            except:
                pass
        newsGroup.effect = sentiment_sum if count == 0 else sentiment_sum / count
        newsGroup.save()

