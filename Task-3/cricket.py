import pandas as pd

weights = {
    'Clean Pick': 1,
    'Good Throw': 2,
    'Catch': 3,
    'Dropped Catch': -3,
    'Stumping': 2,
    'Run Out': 3,
    'Missed Run Out': -2,
    'Direct Hit': 4
}

data = {
    'Match No.': [1, 1, 1, 1, 1, 1],
    'Innings': [1, 1, 1, 1, 1, 1],
    'Team': ['Team A', 'Team A', 'Team A', 'Team A', 'Team A', 'Team A'],
    'Player Name': ['Player 1', 'Player 1', 'Player 2', 'Player 3', 'Player 2', 'Player 3'],
    'Ballcount': [1, 2, 3, 4, 5, 6],
    'Position': ['Slip', 'Mid-Off', 'Long-On', 'Deep Fine Leg', 'Short Fine Leg', 'Deep Square Leg'],
    'Short Description': ['Clean Pick', 'Good Throw', 'Fumble', 'Catch', 'Dropped Catch', 'Run Out'],
    'Pick': ['Clean Pick', 'Good Throw', 'Fumble', 'Catch', 'Dropped Catch', 'None'],
    'Throw': ['Run Out', 'Missed Run Out', 'None', 'None', 'None', 'Run Out'],
    'Runs': [2, 1, -1, 3, -2, 4],
    'Overcount': [1, 1, 1, 1, 1, 1],
    'Venue': ['Stadium X', 'Stadium X', 'Stadium X', 'Stadium X', 'Stadium X', 'Stadium X']
}

df = pd.DataFrame(data)

def calculate_ps(row):
    action = row['Pick']
    throw = row['Throw']
    runs_saved = row['Runs']
    pick_score = weights.get(action, 0)
    throw_score = weights.get(throw, 0)
    return pick_score + throw_score + runs_saved

df['Performance Score'] = df.apply(calculate_ps, axis=1)

print(df[['Match No.', 'Player Name', 'Short Description', 'Performance Score']])

df.to_excel('C:/Users/Dell/Documents/Python Dev Internship/Advance Tasks/fielding_analysis_with_ps.xlsx', index=False)
