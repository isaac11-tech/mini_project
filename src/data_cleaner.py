import pandas as pd
import string

class DataCleaning:

    def __init__(self,df: pd.DataFrame):
        self.df = df
        self.df = self.edit_df()
        self.df = self.remove_punctuation_marks()
        self.df = self.to_lowercase()
        self.df = self.remove_unclassified()



        #functions that return new df with only "Text", "Biased" columns
    def edit_df(self):
        new_df = self.df[["Text", "Biased"]].copy()
        return new_df

    # functions that return the df without the punctuation marks
    def remove_punctuation_marks(self):
        translator = str.maketrans('', '', string.punctuation)
        self.df['Text'] = self.df['Text'].apply(lambda x: x.translate(translator))
        return self.df

    # functions that return the df and change all the text to lower case
    def to_lowercase(self):
        self.df["Text"] = self.df["Text"].apply(
            lambda x: x.lower() if isinstance(x, str) else x #if not str return x
        )
        return self.df

    # functions that remove all the unclassified Biased
    def remove_unclassified(self):
        self.df = self.df[self.df['Biased'].notna()]
        return self.df




















