from random import uniform

class Quanitfier :

    def quantified_change_from_sentiment(self, sentiment_score):
        change = sentiment_score * uniform(0.001, 0.01)
        return change

if __name__=="__main__":
    quant = Quanitfier()
    print quant.quantified_change_from_sentiment(-0.80)
