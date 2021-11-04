import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import pyspark
#import datawig
from scipy.stats import skew
import logging

df=pd.read_csv('data_preprocessed/clean_data.csv')

logging.basicConfig(filename='logs/model_development.txt',filemode='a',format='%(asctime)s %(message)s',datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("Feature Scaling")

logging.warning("Reading Dataset...")

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df.location = le.fit_transform(df.location)
df.rest_type = le.fit_transform(df.rest_type)
df.cuisines = le.fit_transform(df.cuisines)
df.dish_liked = le.fit_transform(df.dish_liked)
df.type = le.fit_transform(df.type)
df.city = le.fit_transform(df.city)

del df['Unnamed: 0']
del df['Unnamed: 0.1']

logging.warning("Feature Scaling Done")

logging.warning("Storing Final data in the folder...")

df.to_csv('data_preprocessed/processed_data.csv')

logging.warning("Data is Stored")
