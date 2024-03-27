#### Preamble ####
# Purpose: Cleans the raw plane data to pretend that you are an NFL analyst and that it is half way through the 2023 regular season
# Author: Jiwon Choi
# Date: 27 March 2024
# Contact: jwon.choi@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.py

#### Workspace setup ####
import pandas as pd

def clean_weekly_data(input_file):
    df = pd.read_csv(input_file)
    
    # Filter for regular season data up to Week 9
    df = df[(df['season_type'] == 'REG') & (df['week'] <= 9)]
    
    # Ensure correct data types
    df['season'] = df['season'].astype(int)
    df['week'] = df['week'].astype(int)
    
    # Handling missing values for key columns, specifically for 'passing_epa'
    # Assuming a missing 'passing_epa' can be considered as 0 for weeks where a QB may not have played
    df['passing_epa'] = df['passing_epa'].fillna(0)

    # Save the cleaned data to a new CSV file
    cleaned_file_path = input_file.replace('data/raw_data/', 'data/analysis_data/cleaned_')
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to: {cleaned_file_path}")
    
    return cleaned_file_path

if __name__ == "__main__":
    input_file_path = 'data/raw_data/weekly_qb_stats_2023.csv'  # Adjust this to your actual file path
    cleaned_file_path = clean_weekly_data(input_file_path)
