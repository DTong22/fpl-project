import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def train_model():
    # Connect to the SQLite database
    conn = sqlite3.connect("fpl_database.db")

    # Query the preprocessed player data from the 'preprocessed_players' table
    query = "SELECT * FROM preprocessed_players"
    df = pd.read_sql_query(query, conn)
    
    df.fillna(df.mean(), inplace=True)

    # Define the features and target variable
    features = ["moving_average"]
    target = "total_points"

    # Split the data into training and testing sets
    train_data = df[df["gameweek"] < 28]
    test_data = df[df["gameweek"] >= 28]
    X_train = train_data[features]
    y_train = train_data[target]
    X_test = test_data[features]
    y_test = test_data[target]

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    score = model.score(X_test, y_test)
    print("Model Score:", score)

    # Generate predictions using the model
    y_pred = model.predict(X_test)
    '''
    # Visualize the linear regression
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
    plt.xlabel('Moving Average')
    plt.ylabel('Total Points')
    plt.title('Linear Regression Model')
    plt.legend()
    plt.show()
    '''
    # Close the database connection
    conn.close()

    return model

def main():
    # Train the model
    model = train_model()

    # Print the coefficients of the trained model
    print("Model Coefficients:")
    print(model.coef_)


if __name__ == "__main__":
    main()

