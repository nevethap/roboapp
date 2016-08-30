import pandas as pd

data_table = pd.read_csv("/Users/nevethap/Documents/projects/fintech/robo_app/news_sentiment/datasets/LoughranMcDonald_MasterDictionary_2014.csv")
pos_neg_score = pd.DataFrame(data_table, columns=['Word','Negative','Positive'])

def noramalize(x):
    return x / 2009

pos_neg_score['Negative'] = pos_neg_score.apply(lambda row: noramalize(row['Negative']), axis=1)
pos_neg_score['Positive'] = pos_neg_score.apply(lambda row: noramalize(row['Positive']), axis=1)

print pos_neg_score.head(5)

