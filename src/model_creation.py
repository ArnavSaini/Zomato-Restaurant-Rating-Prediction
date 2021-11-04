import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import pyspark
#import datawig
from scipy.stats import skew
import logging

df=pd.read_csv('data_preprocessed/processed_data.csv')

logging.basicConfig(filename='logs/model_development.txt',filemode='a',format='%(asctime)s %(message)s',datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("Feature Selection")

logging.warning("Reading Dataset...")

del df['Unnamed: 0']
x=df.iloc[:,[0,1,3,4,5,6,7,8,9,10]]
y=df['rate']

from sklearn.ensemble import  ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=10)

ET_Model=ExtraTreesRegressor(n_estimators = 120)
ET_Model.fit(x_train,y_train)
y_predict=ET_Model.predict(x_test)
R2_Score=r2_score(y_test,y_predict)

logging.warning("R2 Score: %s", R2_Score*100)


from sklearn import metrics

Mean_Absolute_Error= metrics.mean_absolute_error(y_test, y_predict)
Mean_Squared_Error=metrics.mean_squared_error(y_test, y_predict)
Root_Mean_Squared_Error= np.sqrt(metrics.mean_squared_error(y_test, y_predict))

logging.warning('Mean Absolute Error: %s', Mean_Absolute_Error)
logging.warning('Mean Squared Error: %s', Mean_Squared_Error)
logging.warning('Root Mean Squared Error: %s', Root_Mean_Squared_Error)

import pickle 
# Saving model to disk
logging.warning('Making Pickle File...')
pickle.dump(ET_Model, open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

logging.warning('MOdel Creation Done !!!')