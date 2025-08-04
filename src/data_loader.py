import pandas as pd

class DataLoader:

    @staticmethod
    def load_csv(file_path ="../data/tweets_dataset.csv"): #I added a fixed path for the purpose of this exercise.

        try:
            df = pd.read_csv(file_path)
            print(f"Data loaded successfully. Length: {len(df)}")
            return df

        except Exception as e:
            print(f"Error while loading file: {e}")
            return None


