"""
CSE 310 - Data Analysis Module
Basketball Player Statistics Analysis

Questions answered:
  1. Which team scored the most total points this season?
  2. Which position averages the most points per game?

To use a real dataset, replace basketball_stats.csv with any CSV that has
the columns: Player, Team, Position, Games, Points, Rebounds, Assists
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "basketball_stats.csv"


# ---------------------------------------------------------------
# STEP 1: Load the CSV file into a Pandas DataFrame
# ---------------------------------------------------------------
df = pd.read_csv(DATA_FILE)


# ---------------------------------------------------------------
# STEP 2: Display basic information about the dataset
# ---------------------------------------------------------------
print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print(f"\nThe dataset has {df.shape[0]} rows and {df.shape[1]} columns.")

print("\nColumn data types:")
print(df.dtypes)


# ---------------------------------------------------------------
# STEP 3: Check for missing values and clean them
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("MISSING VALUES CHECK")
print("=" * 60)

print("\nMissing values per column:")
print(df.isnull().sum())

# Replace missing stats with 0 so calculations still work
df = df.fillna(0)
print("\nMissing values were replaced with 0.")


# ---------------------------------------------------------------
# QUESTION 1: Which team scored the most total points?
# Techniques: aggregation (sum) + sorting
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("QUESTION 1: Which team scored the most total points?")
print("=" * 60)

# Group players by team, add up their points, and sort highest to lowest
team_points = df.groupby("Team")["Points"].sum().sort_values(ascending=False)

print("\nTotal points by team:")
print(team_points)

top_team = team_points.index[0]
top_team_points = team_points.iloc[0]
print(f"\nANSWER: The {top_team} scored the most points with "
      f"{top_team_points} total points.")


# ---------------------------------------------------------------
# QUESTION 2: Which position averages the most points per game?
# Techniques: data conversion (new column) + aggregation (mean) + sorting
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("QUESTION 2: Which position averages the most points per game?")
print("=" * 60)

# Convert season totals into a per-game stat for each player
df["PointsPerGame"] = df["Points"] / df["Games"]

# Average the per-game points for each position and sort highest to lowest
position_ppg = (
    df.groupby("Position")["PointsPerGame"].mean().sort_values(ascending=False)
)

print("\nAverage points per game by position:")
print(position_ppg.round(1))

top_position = position_ppg.index[0]
top_position_ppg = position_ppg.iloc[0]
print(f"\nANSWER: {top_position}s score the most, averaging "
      f"{top_position_ppg:.1f} points per game.")


# ---------------------------------------------------------------
# STEP 4: Create a bar chart for Question 1
# ---------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(team_points.index, team_points.values, color="steelblue")
plt.title("Total Points Scored by Team")
plt.xlabel("Team")
plt.ylabel("Total Points")
plt.tight_layout()

plt.savefig("team_points_chart.png")
print("\nBar chart saved as team_points_chart.png")
plt.show()
