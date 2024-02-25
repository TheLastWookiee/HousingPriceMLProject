from sklearn.model_selection import GridSearchCV

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint, uniform
from sklearn.model_selection import train_test_split

import pandas as pd

# Load the dataset
HouseDF = pd.read_csv('C:/Users/Caiden Henn/Downloads/archive (1)/Housing.csv')

# Convert categorical variables to numerical
HouseDF = pd.get_dummies(HouseDF, columns=['mainroad', 'guestroom', 'basement', 
                                           'hotwaterheating', 'airconditioning', 
                                           'prefarea', 'furnishingstatus'])

# Filling missing values with 0
HouseDF.fillna(0, inplace=True)

# Separating features and target variable
X = HouseDF.drop('price', axis=1)
y = HouseDF['price']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

model = RandomForestClassifier() 
model.fit(X_train, y_train) 


# Define the hyperparameters grid to search
rf_hyperparameters = {
    'n_estimators': [25, 50, 100, 150], 
    'max_features': ['sqrt', 'log2', None], 
    'max_depth': [3, 6, 9], 
    'max_leaf_nodes': [3, 6, 9], 
} 

grid_search = GridSearchCV(RandomForestClassifier(), 
                           param_grid=rf_hyperparameters) 
grid_search.fit(X_train, y_train) 
print(grid_search.best_estimator_) 

# Print the best hyperparameters and corresponding score
print("Best hyperparameters:", grid_search.best_params_)
print("Best score for cost function:", grid_search.best_score_)
