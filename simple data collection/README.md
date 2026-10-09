# Basketball Statistics Analysis

## Overview

This project explores how Python can be used to load, clean, summarize, and visualize structured sports data. It analyzes a small basketball player statistics dataset containing 15 player records and seven columns: player, team, position, games played, points, rebounds, and assists.

The dataset is included in [`basketball_stats.csv`](./basketball_stats.csv). No external source URL is recorded for this sample dataset; add the original source link here if one is available.

The analysis script answers two questions: which team scored the most total points, and which position had the highest average points per game. It also creates a bar chart comparing team point totals.

[Software Demo Video]https://drive.google.com/file/d/1wEt2YP_6tfbopukTCe3GCbP-xC--aLb-/view?usp=sharing

Replace the placeholder above with a link to a 4–5 minute YouTube demonstration covering the dataset, questions and answers, the program running, and a walkthrough of the code.

## Data Analysis Results

1. **Which team scored the most total points?** The Wolves scored the most, with **4,050 points**.
2. **Which position averages the most points per game?** Guards averaged the most, at **23.0 points per game**. This is the unweighted mean of the individual players' points-per-game values for each position.

The script saves a team comparison chart as [`team_points_chart.png`](./team_points_chart.png).

## Development Environment

- The analysis is implemented in Python in [`analysis.py`](./analysis.py).
- The input data is stored in a CSV file and loaded with **Pandas**.
- **Matplotlib** is used to create and save the team points bar chart.
- Run the script from the project directory with `python analysis.py`. The required Python packages are `pandas` and `matplotlib`.

## Useful Websites

* [Python Documentation](https://docs.python.org/3/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib Documentation](https://matplotlib.org/stable/)

## Future Work

* Record and cite the original source of the dataset, or replace the sample data with a sourced dataset.
* Add validation for missing values and zero games played before calculating per-game statistics.
* Expand the analysis with rebounds and assists, and add visualizations for positional averages.
