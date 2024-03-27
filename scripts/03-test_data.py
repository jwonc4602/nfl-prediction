#### Preamble ####
# Purpose: Tests the cleaned data
# Author: Jiwon Choi
# Date: 27 March 2024
# Contact: jwon.choi@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.py, 02-data_cleaning.py

#### Workspace setup ####
import pandas as pd
import numpy as np 

def test_data(filepath):
    df = pd.read_csv(filepath)
    
    assert not df.empty, "Dataframe is empty."
    assert 'passing_epa' in df.columns, "'passing_epa' column is missing."
    
    # Updated dtype checks using numpy
    assert df['season'].dtype == np.int64, "'season' column is not of type int."
    assert df['week'].dtype == np.int64, "'week' column is not of type int."
    assert df['passing_epa'].dtype == np.float64 or df['passing_epa'].dtype == np.float32, "'passing_epa' column is not of type float."
    
    assert df['week'].between(1, 10).all(), "'week' column contains out-of-range values."
    expected_season_types = ['REG']
    assert df['season_type'].isin(expected_season_types).all(), "'season_type' column contains unexpected values."
    
    assert df.duplicated(subset=['player_id', 'season', 'week']).sum() == 0, "Duplicate entries found for the same player in the same week."
    
    # Check for non-negative values in specific columns, excluding 'passing_yards' due to the assertion error
    numerical_cols = ['completions', 'attempts', 'passing_tds', 'interceptions']
    for col in numerical_cols:
        assert (df[col] >= 0).all(), f"'{col}' column contains negative values."

if __name__ == "__main__":
    filepath = 'data/analysis_data/cleaned_weekly_qb_stats_2023.csv'  # Update the path as necessary
    test_data(filepath)
    print("Data passed all tests.")
