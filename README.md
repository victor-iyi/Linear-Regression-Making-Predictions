# Linear-Regression-Making-Predictions
Udacity Nanodegree Programming Challenge

### Objective
To predict the body weight of an animal based on it's body weight

### Method
+ The data was loaded into a `dataset` variable using numpy's `loadtxt()` function.
+ A Linear Regression model was used because the task was to predict a continous value.
+ The `LinearRegression()` algorithm from `sklearn.linear_model` was used because of it's simplicity and ease of use.
+ An instance of the `LinearRegression()` class was defined so as to gain access to train and predict unknown values.
+ `fit()` method was called  on the instance of the `LinearRegression()` class to train the model.
+ `predict()` method was used to predict unknown values and stored in the variable `y_pred`.
+ To view the model's accuracy, `sklearn.metrics.accuracy_score()` was called passing in the predicted values and the known body weight.
+ Conversley, `LinearRegression().score()` can also be used to determine how accuracte the model is.
+ Finally, `matplotlib.pyplot` plots the data points and the regression (best fit) line for expert visualization.

### Result
+ A graph containing the training points and the regression line.
+ The accuracy score of the model
