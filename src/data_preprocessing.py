import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import pyspark
#import datawig
from scipy.stats import skew
import logging

df=pd.read_csv('zomato.csv')

logging.basicConfig(filename='logs/model_development.txt',filemode='a',format='%(asctime)s %(message)s',datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("DATA PREPROCESSING 1 STAGE")

logging.warning("Reading Dataset...")

df.info()

logging.warning("Data Info...")

del df['url']
del df['address']
del df['phone']
del df['name']
del df['reviews_list']

df['online_order'] = df['online_order'].map(dict(Yes=1, No=0))
df['book_table'] = df['book_table'].map(dict(Yes=1, No=0))

df4 = df['rate']
df['rate'] = df4.dropna().apply(lambda x: float(x.split('/')[0]) if (len(x)>3) else np.nan).dropna()

def comma(value):
    value = str(value)
    if ',' in value:
        value = value.replace(',','')
        return float(value)
    else:
        return float(value)
df['costfor2'] = df['approx_cost(for two people)'].apply(comma)
del df['approx_cost(for two people)']

df.drop_duplicates(inplace=True)

df.rename(columns={'approx_cost(for two people)':'costfor2','listed_in(type)':'type','listed_in(city)':'city'},inplace=True)

logging.warning("Renaming Done")

df['rate'].fillna(df['rate'].mean(),inplace=True)
df.drop(['menu_item'],axis=1,inplace=True)

logging.warning("Handling Missing Values...")

df.dropna(inplace=True)

logging.warning("Filtering Done")

logging.warning("Storing Filtered Data in data_processed folder...")

df.to_csv('data_preprocessed/data_preprocessing1.csv')

logging.warning("Data is Stored")