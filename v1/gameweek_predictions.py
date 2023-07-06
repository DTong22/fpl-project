import sqlite3
import pandas as pd
from algorithm_model import train_model

def load_preprocessed_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("fpl_database.db")

    # Query the preprocessed player data from the 'preprocessed_players' table
    query = "SELECT * FROM preprocessed_players"
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    return df

def preprocess_data(df):
    # Fill missing values with the mean of the column
    df.fillna(df.mean(), inplace=True)

    return df

def predict_gameweek_points(df, model):
    # Select the relevant features for prediction
    features = ["moving_average"]
    
    # Create a new DataFrame to store the predicted points for each gameweek
    predictions_df = pd.DataFrame(columns=["gameweek", "player_id", "predicted_points", "total_points"])

    # Iterate over each gameweek
    for gameweek in range(1, 39):
        # Filter the data for the current gameweek
        gw_df = df[df["gameweek"] == gameweek]

        # Select the features for prediction
        X = gw_df[features]

        # Generate predictions using the trained model
        predictions = model.predict(X)

        # Add the predicted points to the DataFrame
        gw_df["predicted_points"] = predictions

        # Sort the DataFrame by predicted points in descending order
        ranked_df = gw_df.sort_values("predicted_points", ascending=False)

        # Select the top 5 players for the current gameweek
        top_5 = ranked_df.head(5)

        # Append the top 50 players and their predicted points to the predictions DataFrame
        predictions_df = predictions_df.append(top_5[["gameweek", "player_id", "predicted_points", "total_points"]])

    return predictions_df

def main():
    # Load the preprocessed player data
    df = load_preprocessed_data()

    # Preprocess the data to handle missing values
    df = preprocess_data(df)

    # Train the model
    model = train_model()

    # Predict gameweek points for players and retrieve top 50 players for each gameweek
    predictions_df = predict_gameweek_points(df, model)

    # Print the predictions for each gameweek
    for gameweek in range(1, 39):
        print(f"Gameweek {gameweek}")
        gameweek_df = predictions_df[predictions_df["gameweek"] == gameweek]
        print(gameweek_df)
        print()

if __name__ == "__main__":
    main()

