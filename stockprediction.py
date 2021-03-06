# -*- coding: utf-8 -*-
"""StockPrediction.ipynb

Stock Prediction using Machine Learning
"""

#Stock Price prediction program using Machine Learning model

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#Get Stock data
df = quandl.get("WIKI/FB")
#Print few data
print(df.head())

#Get the adjusted Close Price
df = df[['Adj. Close']]
#print column close data
print(df.head())

# Variable for predicting 'n' days into future
forecast_out = 30
#create the target variable shifted 'n' units up
df['Prediction'] = df[['Adj. Close']].shift(-(forecast_out))
#Print new data
print(df.tail())

# Create independent data set (X)
#convert the data frame to a numpy array
X = np.array(df.drop(['Prediction'],1))
#Remove the last 'n' rows
X = X[:-forecast_out]
print(X) #List of list

# Create the dependent data_set(y)
# Convert the dataframe to numpy array (All of the values including NAN)
y = np.array(df['Prediction'])
#Get all y values except last 'n' rows
y = y[:-forecast_out]
print(y) #List

# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the Support Vector Machine(Regresor)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

# Testing Model: Score returns the coefficient of determination of R^2 of the predicttion
# Best score is 1.0
svm_confidence = svr_rbf.score(x_test, y_test)
print("svm Confidence: ", svm_confidence)

# Create and train the Linear Regression model
lr = LinearRegression()
#train the model
lr.fit(x_train, y_train)

# Testing Model: Score returns the coefficient of determination of R^2 of the predicttion
# Best score is 1.0
lr_confidence = lr.score(x_test, y_test)
print("lr Confidence: ", lr_confidence)

# Set x_forecast equal to the lat 30 rows of the original data set from Adj. Close
x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]
print(x_forecast)

#Print Linear Regression model prediction for the next 'n' days
lr_prediction = lr.predict(x_forecast)
print(lr_prediction)
print()
#Print Support Vector Regressor model prediction for the next 'n' days
svm_prediction = svr_rbf.predict(x_forecast)
print(svm_prediction)

