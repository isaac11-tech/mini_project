import pandas as pd

class DataCleaning:

    @staticmethod
    def cleaning(df: pd.DataFrame):
        new_df = df[df["Text", "Biased"]]
        print(new_df)
       return df



