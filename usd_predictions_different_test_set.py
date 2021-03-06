#USD_Predictions_Different_Test_Set.ipynb

import pandas as pd
import numpy as np
import os 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import PCA

pinr=pd.read_csv('C:/Users/Akshay Kumar Ambavat/INR_USD/inr_final.csv')

X_train=pinr.iloc[:,2:].values
X_test=pinr.iloc[:,2:].values
y_train=pinr.iloc[:,1].values
y_test=pinr.iloc[:,1].values
y_train=y_train.reshape(-1,1)
y_test=y_test.reshape(-1,1)

sc_X=StandardScaler()
sc_y=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
y_train=sc_y.fit_transform(y_train)
y_test=sc_y.transform(y_test)

regressor=RandomForestRegressor(n_estimators=100,random_state=0)
model=regressor.fit(X_train,y_train.ravel())

model=regressor.predict(X_test)
c=sc_y.inverse_transform(model)
d=sc_y.inverse_transform(y_test)

error=mean_absolute_error(d,c)
error
