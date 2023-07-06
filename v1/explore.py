import requests

def get_stats_keys(gameweek):
    # Define the endpoint URL for player information
    url = f"https://fantasy.premierleague.com/api/event/{gameweek}/live/"

    # Send a GET request to retrieve data from the FPL API
    response = requests.get(url)
    data = response.json()

    # Get the keys of the stats
    stats_keys = data["elements"][0]["stats"].keys()

    return stats_keys

# Define the gameweek for which you want to retrieve the stats keys
gameweek = 1  # Replace with the desired gameweek

# Call the function to get the stats keys
stats_keys = get_stats_keys(gameweek)

# Print the stats keys
print("Stats Keys:")
for key in stats_keys:
    print(key)

