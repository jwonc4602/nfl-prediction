#### Preamble ####
# Purpose: Downloads and saves the data from https://pypi.org/project/nfl-data-py/#description
# Author: Jiwon Choi
# Date: 27 March 2024
# Contact: jwon.choi@mail.utoronto.ca
# License: MIT
# Pre-requisites: None

#### Workspace setup ####
import nfl_data_py as nfl
import pandas as pd

#### Download and save data ####
def download_weekly_qb_stats(years):
    # Define the columns you're interested in
    # Adjust this list based on your specific needs for forecasting 'passing_epa'
    columns = [
        'player_id', 'season', 'week', 'season_type', 'passing_epa', 
        'completions', 'attempts', 'passing_yards', 'passing_tds', 'interceptions'
    ]
    
    # Fetch weekly data for the specified years and columns
    # The 'downcast' parameter is set to True to reduce memory usage
    weekly_data = nfl.import_weekly_data(years=years, columns=columns, downcast=True)
    
    # Filter for regular season data only
    regular_season_data = weekly_data[weekly_data['season_type'] == 'REG']
    
    # Since we're focusing on quarterbacks, you might want to filter by position here if your columns include position
    # If 'position' column is available, uncomment the next line
    # qb_data = regular_season_data[regular_season_data['position'] == 'QB']
    
    return regular_season_data  # or return qb_data if filtering by position

if __name__ == "__main__":
    years = [2023]  # Example: Fetching data for the 2023 season
    weekly_qb_stats = download_weekly_qb_stats(years)
    
    # Define the output file path
    output_path = 'data/raw_data/weekly_qb_stats_2023.csv'
    weekly_qb_stats.to_csv(output_path, index=False)
    print(f"Weekly quarterback stats for {', '.join(map(str, years))} downloaded and saved to {output_path}.")
