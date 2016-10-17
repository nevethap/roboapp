import feedparser
import codecs
from feeds import models
from crawler import NewsCrawler
import re
from dateutil import parser
from news_sentiment.sentiment import SentimentScorer

class NewsAggregator:

    def get_live_feeds(self):
        feed = feedparser.parse('http://feeds.reuters.com/reuters/hotStocksNews')
        for entry in feed.entries:
            # for keyword in keywords:
            #     if keyword in entry.title_detail.value:
            title = entry.title_detail.value
            try:
                description = entry.summary_detail.value
            except:
                description = ""
            article_link = entry.link
            publishedString = entry.published
            published = parser.parse(publishedString)
            article_text = NewsCrawler.crawl_article(NewsCrawler(), article_link)
            content_file = "feeds/articles/" + re.sub('[^A-Za-z0-9]+', '', title) + ".txt"
            file = codecs.open(content_file, "w", encoding="utf")
            file.write(article_text)
            file.close()
            SS = SentimentScorer()
            sentiment_score = SS.scoreArticle(content_file)
            models.News(title, description, published, article_link, content_file, sentiment_score['Polarity']).save()