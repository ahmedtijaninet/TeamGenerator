import pandas as pd
import csv
# Read in the data from teams.csv
with open('teams.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
# Create a list of tuples (name, skill_level) from the data
teams = [(row[0], row[1]) for row in data]
# Sort the teams by skill level, from highest to lowest
teams.sort(key=lambda x: x[1], reverse=True)
# Create a list of 5 empty lists to represent the 5 teams
team_lists = [[] for _ in range(4)]
# Iterate over the teams and evenly distribute them among the 5 lists
for i, team in enumerate(teams):
    team_lists[i % 4].append(team)
# Print out the teams
for i, team in enumerate(team_lists):
    print(f'Team {i+1}: {team}')

# Write the teams to teams_out.csv
with open('teams_out.csv', 'w') as f:
    writer = csv.writer(f)
    for i, team in enumerate(team_lists):
        writer.writerow([f'Team {i+1}'] + [t[0] for t in team])
teams = pd.read_csv('teams_out.csv').transpose()
teams.to_csv('teams_out_transpose.csv')
