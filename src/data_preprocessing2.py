import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import pyspark
#import datawig
from scipy.stats import skew
import logging

df=pd.read_csv('data_preprocessed/data_preprocessing1.csv')

logging.basicConfig(filename='logs/model_development.txt',filemode='a',format='%(asctime)s %(message)s',datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("DATA PREPROCESSING 2 STAGE")

logging.warning("Reading Dataset...")

df.agg(['skew', 'kurtosis']).transpose()
logging.warning('Checking Skewness...')

df['votes']=np.sqrt(df['votes'])
df['costfor2']=np.sqrt(df['costfor2'])

logging.warning("Filtering Done")

logging.warning("Storing Filtered Data in data_processed folder...")

df.to_csv('data_preprocessed/clean_data.csv')

logging.warning("Data is Stored")