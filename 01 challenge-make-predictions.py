import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import accuracy_score

X,y = np.loadtxt('challenge_dataset.txt',
                  delimiter=',', unpack=True)
X = X.reshape((-1, 1))
y = y.reshape((-1, 1))

print(X.shape, y.shape)

# Define the machine learning model
model = linear_model.LinearRegression()
# Train the model
model.fit(X, y)
# Predict
y_pred = model.predict(X)

# Print Accuracy
accuracy = model.score(X, y_pred)
print('{:.1%}'.format(accuracy))

# Visualize model's performance
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.show()
