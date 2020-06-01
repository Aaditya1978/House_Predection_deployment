# Home Pricing Model

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('homeprices.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:2])
X[:, 1:2] = imputer.transform(X[:, 1:2])

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 1)
X = pca.fit_transform(X)

# Training the Polynomial Regression model on the whole dataset
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

pickle.dump(lin_reg, open('lin_reg.pkl', 'wb'))
pickle.dump(poly_reg, open('poly_reg.pkl', 'wb'))
pickle.dump(pca, open('pca.pkl', 'wb'))


# Predicting the Train set results
y_pred = lin_reg.predict(X_poly)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y.reshape(len(y),1)),1))

# Calculating r2 Score for model trained
from sklearn.metrics import r2_score
print(r2_score(y,y_pred))

# Predicting Housing Price for A 3000 Sq feet and 6 bedroom and 28 yeras old
y_predicted = lin_reg.predict(poly_reg.fit_transform(pca.transform([[3000, 6, 28]])))
print(y_predicted)

# Visualising the Training set results
training = plt.scatter(X, y, color = 'red')
predicting = plt.scatter(pca.transform([[3000, 6, 28]]), y_predicted, color = 'magenta')
plt.plot(X, y_pred, color = 'blue')
plt.title('Home Prices')
plt.xlabel('PC1')
plt.ylabel('Prices')
plt.legend((training, predicting), ('Training set points', 'Predicting a Price'))
plt.show()
