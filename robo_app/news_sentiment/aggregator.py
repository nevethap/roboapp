import feedparser
from dateutil import parser
from datetime import datetime

from crawler import NewsCrawler
from robo_app import models
from robo_app.models import Asset
from robo_app.news_sentiment.sentiment import SentimentScorer


class NewsAggregator:
    def get_live_feeds(self, keywords, newsGroup):
        feed = feedparser.parse('http://feeds.reuters.com/reuters/hotStocksNews')
        date_format = "%Y-%m-%d"
        count = 0
        sentiment_sum = 0
        for entry in feed.entries:
            # for keyword in keywords:
                # if keyword in entry.title_detail.value:
                    title = entry.title_detail.value
                    article_link = entry.link
                    publishedString = entry.published
                    published = parser.parse(publishedString)
                    date = str(published.date())[0]
                    article_text = NewsCrawler.crawl_article(NewsCrawler(), article_link)
                    sentimentScore = SentimentScorer()
                    sentiment_score = sentimentScore.scoreArticle(article_text)
                    sentiment_sum += sentiment_score['Polarity']
                    count += 1
                    models.News(headline=title, timestamp=published, url=article_link,
                                sentiment=sentiment_score['Polarity'], asset=newsGroup.asset).save()
        newsGroup.effect = sentiment_sum if count==0 else sentiment_sum/count
        newsGroup.save()

    def addApple(self, newsGroup):
        date_format = "%Y-%m-%d"
        sentimentScore = SentimentScorer()
        date = datetime.strptime(str(datetime.now().date()), date_format)

        article = "Apple shares underperform and the company fiscal fourth-quarter earnings failed to impress investors even though Apple beat profit forecasts and essentially matched revenue projections. Investors seem to be focused instead on Apple profit margin forecast for the current quarter, which fell short of expectations. This left the investors sad."
        sentiment_score = sentimentScore.scoreArticle(article)
        title = "The Apple half full"
        url = "https://finance.yahoo.com/video/apple-half-full-135748727.html"
        symbol = "AAPL"
        models.News(headline=title, timestamp=date, url=url, sentiment=sentiment_score['Polarity'],asset=Asset.objects.get(symbol=symbol)).save()
        newsGroup.effect = sentiment_score['Polarity']
        newsGroup.save()

    def add7(self, newsGroup):
        date_format = "%Y-%m-%d"
        sentimentScore = SentimentScorer()
        date = datetime.strptime(str(datetime.now().date()), date_format)

        title = "Valero Stock Rose 5% Following Its Earnings Release"
        article = "Valero Energy (VLO) announced its results on October 25, 2016, before the markets opened. The stock received a strong opening, likely because its earnings surpassed analysts estimates. VLO opened at $57.3 per share, higher than its previous close of $56.2. Valero (VLO) saw highs of $59.5 and lows of $56.5 during the day. Eventually, VLO closed at $58.9, 4.9% higher than its previous day close."
        sentiment_score = sentimentScore.scoreArticle(article)
        url = "http://marketrealist.com/2016/10/valeros-stock-rose-5-following-earnings-release/"
        symbol = "VLO"
        models.News(headline=title, timestamp=date, url=url, sentiment=sentiment_score['Polarity'],
                    asset=Asset.objects.get(symbol=symbol)).save()
        newsGroup.effect = sentiment_score['Polarity']
        newsGroup.save()

    def add5(self, newsGroup):
        date_format = "%Y-%m-%d"
        sentimentScore = SentimentScorer()
        date = datetime.strptime(str(datetime.now().date()), date_format)

        title = "Companies in the Energy Sector Fell on October 24"
        article = "Below are the bottom five companies, who underperform in the major integrated oil and gas industry on October 24 : Chevron was at seconds lowest with a fall of 0.9%"
        sentiment_score = sentimentScore.scoreArticle(article)
        url = "http://marketrealist.com/2016/10/performance-companies-energy-sector-monday-october-24/"
        symbol = "CVX"
        models.News(headline=title, timestamp=date, url=url, sentiment=sentiment_score['Polarity'],
                    asset=Asset.objects.get(symbol=symbol)).save()
        newsGroup.effect = sentiment_score['Polarity']
        newsGroup.save()

    def add10(self, newsGroup):
        date_format = "%Y-%m-%d"
        sentimentScore = SentimentScorer()
        date = datetime.strptime(str(datetime.now().date()), date_format)

        title = "What to Expect When Alphabet, Inc. Reports Earnings"
        article = "Alphabet Inc. is set to release third-quarter 2016 results this Thursday, Oct. 27, 2016, after the market close. With shares up 9% over the past three months (as of this writing) thanks largely to a stellar second-quarter report in July, what can investors expect to hear from the internet-search behemoth this time?"
        article += "So while we don't typically pay close attention to Wall Street's near-term demands, note that consensus estimates predict Alphabet will grow revenue 18.1% year over year, to $22.05 billion, and generate earnings of $8.64 per share (up from $7.35 in last year's third quarter)."
        sentiment_score = sentimentScore.scoreArticle(article)
        url = "http://www.fool.com/investing/2016/10/26/what-to-expect-when-alphabet-inc-reports-earnings.aspx"
        symbol = "GOOG"
        models.News(headline=title, timestamp=date, url=url, sentiment=sentiment_score['Polarity'],
                    asset=Asset.objects.get(symbol=symbol)).save()
        newsGroup.effect = sentiment_score['Polarity']
        newsGroup.save()

