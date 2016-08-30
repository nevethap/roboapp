from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
from textblob import TextBlob
import pysentiment
from sklearn.naive_bayes import MultinomialNB

import re

import nltk

class SentimentScorer:

    def scoreArticle(self, url):
        article_file = open(url, "r")
        article_text = article_file.read()
        # clean_text = re.sub('[^\.A-Za-z0-9 ]+', '', article_text)
        # parsed_text = word_tokenize(clean_text)
        # sentences_list = sent_tokenize(article_text)
        # parsed_sentence_list = []
        # for sentence in sentences_list:
        #     parsed_sentence_list.append(word_tokenize(sentence))
        #
        # model = Word2Vec(parsed_sentence_list, min_count=1)
        # print model.negative
        # print nltk.pos_tag(parsed_text)
        # blob = TextBlob(article_text)
        # for sentence in blob.sentences:
        #     print sentence
        #     print sentence.sentiment.polarity
        lm = pysentiment.LM()

        tokens = lm.tokenize(article_text)
        score = lm.get_score(tokens)
        # # print tokens[0]
        #     print sentence
        #     print score
        return score




if __name__ == "__main__":
    parser = SentimentScorer()
    parser.scoreArticle("/Users/nevethap/Documents/projects/fintech/robo_app/feeds/articles/textile.txt")
