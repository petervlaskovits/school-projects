import pandas as pd

uncleaned = pd.read_csv('data/raw/bank-additional-full.csv', sep=";")
cleaned = pd.read_csv('data/cleaned_data.csv', index_col=False)