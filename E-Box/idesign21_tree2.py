from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
import numpy as np
import pandas as pd

data = pd.read_csv('apple_stock_prepared.csv')
df = pd.DataFrame(data)
print(df.head())
#print(df.columns)

X = df[['volume', 'close_lag1', 'close_lag2', 'close_lag3', 'close_lag4',
       'close_lag5', 'close_lag6', 'ma_3', 'rsi_3', 'ma_6', 'rsi_6', 'ma_9',
       'rsi_9', 'ma_12', 'rsi_12', 'event']]
y = df['close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print(f"Length Of training data  {len(X_train)}")
print(f"Length Of test data  {len(X_test)}")
print(f"Length Of training Y {len(y_train)}")
print(f"Length Of test data Y {len(y_test)}")

tree_model = DecisionTreeRegressor(max_depth=5, min_samples_split=5)
tree_model.fit(X_train, y_train)

y_pred_train = tree_model.predict(X_train)
y_pred_test = tree_model.predict(X_test)

r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

print(r2_train)
print(r2_test)