import pysentiment

class SentimentScorer:

    def scoreArticle(self, url):
        article_file = open(url, "r")
        article_text = article_file.read()
        lm = pysentiment.LM()

        tokens = lm.tokenize(article_text)
        score = lm.get_score(tokens)
        return score




if __name__ == "__main__":
    parser = SentimentScorer()
    parser.scoreArticle("/Users/nevethap/Documents/projects/fintech/robo_app/feeds/articles/textile.txt")
