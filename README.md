# Scatter Plot

## Description

This project fetches video game data from the RAWG Video Games Database API and visualizes it using Python.  
The script creates a scatter plot showing the relationship between the number of ratings and the release year of games.

Each point in the chart represents a game, and the game name is displayed next to it.

## Technologies Used

- Python 3
- requests
- pandas
- seaborn
- matplotlib

## How It Works

1. Sends an HTTP request to the RAWG API.
2. Converts the JSON response into a pandas DataFrame.
3. Selects relevant columns: game name, release date, and ratings count.
4. Converts release dates to datetime and extracts the release year.
5. Generates a scatter plot with:
   - X-axis: number of ratings
   - Y-axis: release year
6. Adds game names as labels on the plot.
