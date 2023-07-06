from flask import Flask, render_template
from gameweek_predictions import load_preprocessed_data, preprocess_data, predict_gameweek_points, train_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gameweek')
def gameweek():
    # Load the preprocessed player data
    df = load_preprocessed_data()

    # Preprocess the data to handle missing values
    df = preprocess_data(df)

    # Train the model
    model = train_model()

    # Predict gameweek points for players and retrieve top 5 players for each gameweek
    predictions_df = predict_gameweek_points(df, model)

    # Convert predictions to a dictionary for easier access in the template
    predictions = {}
    for gameweek in range(1, 39):
        gameweek_df = predictions_df[predictions_df["gameweek"] == gameweek]
        predictions[gameweek] = gameweek_df.to_dict(orient='records')

    return render_template('gameweek.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
