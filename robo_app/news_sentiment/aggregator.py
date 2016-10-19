import feedparser
from dateutil import parser

from crawler import NewsCrawler
from robo_app import models
from robo_app.news_sentiment.sentiment import SentimentScorer


class NewsAggregator:
    def get_live_feeds(self, keywords, newsGroup):
        feed = feedparser.parse('http://feeds.reuters.com/reuters/hotStocksNews')
        count = 0;
        sentiment_sum = 0
        for entry in feed.entries:
            for keyword in keywords:
                if keyword in entry.title_detail.value:
                    title = entry.title_detail.value
                    article_link = entry.link
                    publishedString = entry.published
                    published = parser.parse(publishedString)
                    article_text = NewsCrawler.crawl_article(NewsCrawler(), article_link)
                    sentimentScore = SentimentScorer()
                    sentiment_score = sentimentScore.scoreArticle(article_text)
                    sentiment_sum += sentiment_score
                    count += 1
                    models.News(headline=title, timeStamp=published, url=article_link,
                                sentiment=sentiment_score['Polarity'], group=newsGroup).save()
        newsGroup.effect = sentiment_sum if count==0 else sentiment_sum/count
        newsGroup.save()