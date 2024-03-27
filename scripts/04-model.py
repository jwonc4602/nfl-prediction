#### Preamble ####
# Purpose: Model passing epa forecasting using logistic regression
# Author: Jiwon Choi
# Date: 27 March 2024
# Contact: jwon.choi@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.py, 02-data_cleaning.py

#### Workspace setup ####
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import joblib

def prepare_features(df):
    """
    Prepare your features for modeling. This function should be adjusted based on your feature engineering.
    """
    # Use completions, attempts, passing yards, passing tds, interceptions as features
    features = ['completions', 'attempts', 'passing_yards', 'passing_tds', 'interceptions']
    X = df[features]
    
    # Convert 'passing_epa' to a binary outcome based on a defined threshold
    # Here, we use the median as a simple threshold for demonstration
    threshold = df['passing_epa'].median()
    y = (df['passing_epa'] > threshold).astype(int)
    
    return X, y

def train_model(X, y):
    """
    Train the forecasting model using logistic regression.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)  # Increase max_iter if convergence warning appears
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")

    return model

if __name__ == "__main__":
    # Load the cleaned data
    df = pd.read_csv('data/analysis_data/cleaned_weekly_qb_stats_2023.csv')  # Ensure correct file path
    
    # Prepare features and target
    X, y = prepare_features(df)
    
    # Train the model
    model = train_model(X, y)

    # Save the model for later use or further analysis
    joblib.dump(model, 'models/passing_epa_forecasting_model.pkl')
    print("Model saved as passing_epa_forecasting_model.pkl")
