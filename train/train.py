import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

model_dir="/storage/salary"

sal = pd.read_csv('sal.csv',header=0, index_col=None)
X = sal[['x']]
y = sal['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)

lm = LinearRegression() 
lm.fit(X_train,y_train) 

print('Intercept :', round(lm.intercept_,2))
print('Slope :', round(lm.coef_[0],2))

from sklearn.metrics import mean_squared_error
y_predict= lm.predict(X_test)
mse = mean_squared_error(y_predict,y_test)
print('MSE :', round(mse,2))

from sklearn.externals import joblib

if not os.path.exists(model_dir):
    os.makedirs(model_dir)
filename = model_dir+'/sal_model.pkl'

joblib.dump(lm, filename)