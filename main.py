import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data_path = 'input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(data_path)
home_data = home_data.loc[:, home_data.columns != 'Id']
home_data = pd.get_dummies(home_data)

original_features = home_data.columns
print(f"Original features shape: {home_data.shape}")
print(f"Number of features: {len(original_features)}")
print(home_data.head())

selected_features = []
y = home_data.SalePrice # Sale prices
def split_data(features):
    global y, home_data
    X = home_data[features]
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1) # Create training data and validation data
    home_data = pd.get_dummies(home_data) # Convert any string values into numerical data
    home_model.fit(train_X, train_y) # Train the model with the training data
    return val_X, val_y

def predict(input_columns, output):
    global home_model
    pred = home_model.predict(input_columns) # Make the predictions
    mean_error = mean_absolute_error(output, input_columns) # Calculate the Mean absolute error
    return pred, mean_error

home_model = RandomForestRegressor(random_state=1) # Current ML model
previous_mae = 0

for feature in original_features:
    if feature not in selected_features: # We append a new feature to a list to test the new MAE
        selected_features.append(feature)
        val_X, val_y = split_data(selected_features)
        predictions, mae = predict(val_X, val_y)
        print(f"MAE for {feature}: {mae}") # Check current feature tested

        if not previous_mae: previous_mae = mae
        if min(mae, previous_mae) == mae:
            previous_mae = mae
            print(f"New MAE: {mae}")
        else:
            selected_features.remove(feature)

# Write the important features to a file:
home_data = home_data[selected_features]
home_data.to_csv("one-to-one.csv", index=False)