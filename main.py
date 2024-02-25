import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
HouseDF = pd.read_csv('C:/Users/Caiden Henn/Documents/Project/Housing Data/1553768847-housing.csv')

# Convert categorical variables to numerical
HouseDF = pd.get_dummies(HouseDF, columns=['ocean_proximity'
])

# Filling missing values with 0
HouseDF.fillna(0, inplace=True)

# Separating features and target variable
X = HouseDF.drop('median_house_value', axis=1)
y = HouseDF['median_house_value']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
#TRAINING
# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Ridge Regression
ridge = Ridge(alpha=3)
ridge.fit(X_train, y_train)

# Gradient Boosting
DT = RandomForestRegressor(criterion='absolute_error')
DT.fit(X_train, y_train)

# Model Performance
models = [lr, ridge, DT]
model_names = ["Linear Regression", "Ridge Regression", "Random Forest"]
#PREDICTING
for model, name in zip(models, model_names):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r_squared = model.score(X_test, y_test)
    
    print("\n{} Performance:".format(name))
    print('MSE:', mse)
    print('RMSE:', rmse)
    print('R-squared:', r_squared)
    # Scatter Plot
    plt.figure(figsize=(10,10))
    plt.scatter(y_test, predictions, c='crimson')
    plt.yscale('log')
    plt.xscale('log')
    p1 = max(max(predictions), max(y_test))
    p2 = min(min(predictions), min(y_test))
    plt.plot([p1, p2], [p1, p2], 'b-')
    plt.xlabel('True Values', fontsize=15)
    plt.ylabel('Predictions', fontsize=15)
    plt.title("{} Scatter Plot".format(name), fontsize=15)
    plt.axis('equal')
    plt.show()


