import sqlite3
import pandas as pd

def preprocess_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("fpl_database.db")

    # Query the player data from the 'players' table
    query = "SELECT * FROM players"
    df = pd.read_sql_query(query, conn)

    # Perform data preprocessing steps
    # Calculate the moving average of event points for each player
    window = 5  # Number of past gameweeks to consider for moving average
    df["moving_average"] = df.groupby("player_id")["total_points"].rolling(window=window, min_periods=1).mean().shift(1).reset_index(0, drop=True)

    # Drop unnecessary columns
    df.drop(["minutes", "goals_scored", "assists", "clean_sheets", "goals_conceded",
             "own_goals", "penalties_saved", "penalties_missed", "yellow_cards", "red_cards",
             "saves", "bonus", "bps", "influence", "creativity", "threat", "ict_index", "starts",
             "expected_goals", "expected_assists", "expected_goal_involvements", "expected_goals_conceded",
             "in_dreamteam"], axis=1, inplace=True)

    # Save the preprocessed data to a new table or file
    df.to_sql("preprocessed_players", conn, if_exists="replace", index=False)

    # Close the database connection
    conn.close()

# Call the function to preprocess the player data
preprocess_data()
