import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import statsmodels
import statsmodels.api as sm

#read the data
ad_data = pd.read_csv('advertising.csv')
print(ad_data.head())

# data visualization
print("\nshape :")
print('#############################################################')
print(ad_data.shape)
print('#############################################################')

print("\ndescribe :")
print('#############################################################')
print(ad_data.describe())
print('#############################################################')

print("\ninfo :")
print('#############################################################')
print(ad_data.info)
print('#############################################################')

sns.pairplot(data=ad_data, x_vars = ['TV', 'Radio', 'Newspaper'], y_vars = 'Sales')
plt.show()

print("\ncorrelation :")
print('#############################################################')
print(ad_data.corr())
print('#############################################################')

plt.title('Correlation b/w Data Attributes')
sns.heatmap(ad_data.corr(), annot = True)
plt.show()

#creating data
X = ad_data['TV']
y = ad_data['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state = 100)
print("\nSample of train data :")
print('#############################################################')
print(X_train.head())
print('#############################################################')


X_train_sm = sm.add_constant(X_train)

lr = sm.OLS(y_train, X_train_sm) #OLS - Ordinary Least Squares
lr_model = lr.fit()

print("\nCoefficients :")
print('#############################################################')
print(lr_model.params)
print('#############################################################')

print("\nSummary :")
print('#############################################################')
print(lr_model.summary())
print('#############################################################')

#visualizing our fitted line
plt.title('Our Fitted-line for train data')
plt.scatter(X_train, y_train)
plt.plot(X_train, 6.948683 + 0.054546*X_train, 'r')
plt.show()

#residual analysis
y_train_predicted = lr_model.predict(X_train_sm)
residuals = y_train - y_train_predicted

plt.title('Residuals Distribution')
sns.distplot(residuals)
plt.show()

plt.title('train data vs Residuals')
plt.scatter(X_train, residuals)
plt.show()

#prediction on test data
X_test_sm = sm.add_constant(X_test)
y_test_predicted = lr_model.predict(X_test_sm)
plt.title('Our Fitted-line for test data')
plt.scatter(X_test, y_test)
plt.plot(X_test, y_test_predicted, 'r')
plt.show()

r_score = r2_score(y_true = y_test, y_pred = y_test_predicted)
print('r-squared score : ',r_score)
