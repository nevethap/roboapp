from newspaper import Article

hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'User-Agent': "Magic Browser"}


class NewsCrawler:

    def crawl_article(self, link):
        try:
            a = Article(link, language='en')
            a.download()
            a.parse()
            return a.text
        except Exception as e:
            print(str(e))
            return

