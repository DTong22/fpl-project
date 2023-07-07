# Full stack FPL prediction project

## Project Intro
Predict top 5 players in FPL gameweeks

## Project Description
1. [data_collection.py](https://github.com/DTong22/fpl-project/blob/main/v1/data_collection.py) collects data from the FPL API, and stores it in a SQL database.
2. [data processing.py](https://github.com/DTong22/fpl-project/blob/main/v1/data_processing.py) creates moving average features.
3. [algorithm_model.py](https://github.com/DTong22/fpl-project/blob/main/v1/algorithm_model.py) trains the linear regression model.
4. [gameweek_predictions.py](https://github.com/DTong22/fpl-project/blob/main/v1/gameweek_predictions.py) predicts players points for each gameweek.
3. [app.py](https://github.com/DTong22/fpl-project/blob/main/v1/app.py) creates web framework using Flask.

### Methods Used
* Machine Learning
* Data Visualization
* Predictive Modeling
* Front End Development

### Technologies
* Python
* SQL (SQLite)
* Jupyter Notebook

### Tools
* Pandas
* Matplotlib
* Sklearn
* FPL API
* Flask

### Machine Learning Methods
* Linear Regression

### Future Imporovements
* More seasons data
* Use more features
* Different algorithms
* Cloud based
