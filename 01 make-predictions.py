# 01. How to Make a Prediction - Intro to Deep Learning #1
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Read data
dataframe = pd.read_fwf('linear_regression_demo-master/brain_body.txt')
X = dataframe[['Brain']]
y = dataframe[['Body']]

body_reg = linear_model.LinearRegression()
body_reg.fit(X, y)

plt.scatter(X, y)
plt.plot(X, body_reg.predict(X))
plt.show()
