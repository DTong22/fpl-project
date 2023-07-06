import requests
import sqlite3

def collect_player_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("fpl_database.db")
    cursor = conn.cursor()

    # Drop the existing 'players' table if it exists
    cursor.execute("DROP TABLE IF EXISTS players")

    # Create the 'players' table in the database
    cursor.execute('''
        CREATE TABLE players (
            player_id INT,
            gameweek INT,
            minutes INT,
            goals_scored INT,
            assists INT,
            clean_sheets INT,
            goals_conceded INT,
            own_goals INT,
            penalties_saved INT,
            penalties_missed INT,
            yellow_cards INT,
            red_cards INT,
            saves INT,
            bonus INT,
            bps INT,
            influence REAL,
            creativity REAL,
            threat REAL,
            ict_index REAL,
            starts INT,
            expected_goals REAL,
            expected_assists REAL,
            expected_goal_involvements REAL,
            expected_goals_conceded REAL,
            total_points INT,
            in_dreamteam INT,
            PRIMARY KEY (player_id, gameweek)
        )
    ''')

    # Define the range of gameweeks for which you want to collect player data
    start_gameweek = 1
    end_gameweek = 38

    # Iterate over each gameweek
    for gameweek in range(start_gameweek, end_gameweek + 1):
        # Define the endpoint URL for player information
        url = f"https://fantasy.premierleague.com/api/event/{gameweek}/live/"

        # Send a GET request to retrieve data from the FPL API
        response = requests.get(url)
        data = response.json()

        # Extract player statistics for the current gameweek
        players = data["elements"]
        for player in players:
            player_stats = [
                player["id"],
                gameweek,
                player["stats"]["minutes"],
                player["stats"]["goals_scored"],
                player["stats"]["assists"],
                player["stats"]["clean_sheets"],
                player["stats"]["goals_conceded"],
                player["stats"]["own_goals"],
                player["stats"]["penalties_saved"],
                player["stats"]["penalties_missed"],
                player["stats"]["yellow_cards"],
                player["stats"]["red_cards"],
                player["stats"]["saves"],
                player["stats"]["bonus"],
                player["stats"]["bps"],
                player["stats"]["influence"],
                player["stats"]["creativity"],
                player["stats"]["threat"],
                player["stats"]["ict_index"],
                player["stats"]["starts"],
                player["stats"]["expected_goals"],
                player["stats"]["expected_assists"],
                player["stats"]["expected_goal_involvements"],
                player["stats"]["expected_goals_conceded"],
                player["stats"]["total_points"],
                player["stats"]["in_dreamteam"]
            ]

            # Insert the player stats into the database
            cursor.execute('''
                INSERT INTO players (
                    player_id, gameweek, minutes, goals_scored, assists, clean_sheets,
                    goals_conceded, own_goals, penalties_saved, penalties_missed,
                    yellow_cards, red_cards, saves, bonus, bps, influence, creativity,
                    threat, ict_index, starts, expected_goals, expected_assists,
                    expected_goal_involvements, expected_goals_conceded, total_points,
                    in_dreamteam
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', player_stats)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Call the function to collect and store player data
collect_player_data()
