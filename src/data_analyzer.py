import pandas as pd
import json
from data_loader import DataLoader

class DataAnalyzer:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.tweets_by_category = self.get_tweets_by_category()

    #functions that return dict of tweets by category
    def get_tweets_by_category(self):
        return {
            'anti_semite': len(self.df[self.df['Biased'] == 1]),
            'not_anti_semite': len(self.df[self.df['Biased'] == 0]),
            'indefinite': len(self.df[self.df['Biased'].isna()])
        }


    #functions that return dict of avg for all kinds in Biased
    def get_average_length_by_category(self):
        self.df['word_count'] = self.df['Text'].astype(str).apply(lambda x: len(x.split()))

        avg_by_category = self.df.groupby('Biased')['word_count'].mean()

        result = {
            #if its empty return 0 for Biased == 1
            'anti_semite': avg_by_category.get(1, 0),
            # if its empty return 0 for Biased == 0
            'not_anti_semite': avg_by_category.get(0, 0),
            'indefinite': self.df[self.df['Biased'].isna()]['word_count'].mean(),
            'overall': self.df['word_count'].mean()
        }

        return result




