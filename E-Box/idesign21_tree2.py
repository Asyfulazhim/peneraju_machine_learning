from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split,  GridSearchCV
from sklearn.metrics import accuracy_score, r2_score
import numpy as np
import pandas as pd

df = pd.read_csv('apple_stock_prepared.csv')
#df = pd.DataFrame(data)
df = pd.DataFrame(df, columns=[
    'volume', 'close_lag1', 'close_lag2', 'close_lag3', 'close_lag4', 'close_lag5', 
    'close_lag6', 'ma_3', 'rsi_3', 'ma_6', 'rsi_6', 'ma_9', 'rsi_9', 'ma_12', 'rsi_12', 
    'event', 'close'
])
pd.set_option('display.max_columns', None)
print(df.head())
#print(df.head().to_string(header=True))
#print(df.columns)
#print(df.head().to_string(index=False, float_format=lambda x: '{:.6f}'.format(x)))

X = df[['volume', 'close_lag1', 'close_lag2', 'close_lag3', 'close_lag4',
       'close_lag5', 'close_lag6', 'ma_3', 'rsi_3', 'ma_6', 'rsi_6', 'ma_9',
       'rsi_9', 'ma_12', 'rsi_12', 'event']]
y = df['close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print(f"Length Of training data  {len(X_train)}")
print(f"Length Of test data  {len(X_test)}")
print(f"Length Of training Y {len(y_train)}")
print(f"Length Of test data Y {len(y_test)}")

# Define the hyperparameter grid
param_grid = {
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 5, 10]
}

# Initialize the Decision Tree Regressor model
tree_model = DecisionTreeRegressor()

# Perform grid search to find the best hyperparameters
grid_search = GridSearchCV(tree_model, param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)

# Get the best hyperparameters and the corresponding R-squared score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

tree_model = DecisionTreeRegressor(**best_params)
tree_model.fit(X_train, y_train)

y_pred_train = tree_model.predict(X_train)
y_pred_test = tree_model.predict(X_test)

r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

print(0.9212766627116157)
print(0.8680317979644208)