import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer



class SENTIMENT_ANALYZER:

    def __init__(self, df):
        self.df = df

    def sentiment(self):
        sia = SentimentIntensityAnalyzer()
        res = {}
        for i, row in self.df.iterrows():
            text = row['reviews']
            myid = row['id']
            res[myid] = sia.polarity_scores(text)

        df_return = pd.DataFrame(res).T
        df_return = df_return.reset_index().rename(columns={'index':'id'})
        return df_return