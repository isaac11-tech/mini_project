import pandas as pd
import json
from data_loader import DataLoader
from results import *


#loading the csv
df = DataLoader.load_csv()
#analyzer the data and save the json
data_analyzed = data_analyzer(df)
#print the data_analyzed
print(data_analyzed)
#cleaning the data
tweets_dataset_cleaned.csv = data_cleaner(df)
#analyzer the cleaning data and save the result csv in result
result = data_analyzer(df)
print(result)