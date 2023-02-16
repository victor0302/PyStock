import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from src.data_splitting import weekly_df

# Convert the '4. close' column to numeric type
weekly_df['4. close'] = pd.to_numeric(weekly_df['4. close'])

# Set the input features and target variable
X = weekly_df[['1. open', '2. high', '3. low', '4. close', '6. volume', '10-day MA', 'title_polarity',
               'description_polarity', 'content_polarity']]
y = weekly_df['4. close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the SVM model
model = SVR()

# Define the parameter grid for the GridSearchCV
param_grid = {'C': [0.1, 1, 10, 100, 1000], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'linear']}

# Use GridSearchCV to find the best hyperparameters for the model
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters found by GridSearchCV
print('Best hyperparameters:', grid_search.best_params_)

# Train the model on the training data using the best hyperparameters
model = SVR(kernel=grid_search.best_params_['kernel'], C=grid_search.best_params_['C'],
            gamma=grid_search.best_params_['gamma'])
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Convert the 'y_test' and 'y_pred' columns to numeric type
y_test = pd.to_numeric(y_test)
y_pred = pd.to_numeric(y_pred)







