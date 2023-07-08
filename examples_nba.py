from BRScraper import nba

# All players current salaries
df = nba.get_current_salaries(info='players')
print(df)

# All teams total current salaries
df = nba.get_current_salaries(info='teams')
print(df)

# All players stats per game regular season
df = nba.get_stats(2023, info='per_game', playoffs=False, rename=False)
print(df)

# All players advanced stats playoffs
df = nba.get_stats(2022, info='advanced', playoffs=True, rename=False)
print(df)

# Standings from league
df = nba.get_standings(2023, info='total')
print(df)

# Standings from eastern conference
df = nba.get_standings(2023, info='east')
print(df)

# General info from NBA history
df = nba.get_general_info()
print(df)

# Get the 20 season leaders in points per game for regular season
df = nba.get_season_leaders(2023, info='pts', n=20,
                            playoffs=False, per_game=True)
print(df)

# Get the 5 season leaders in total rebounds for playoffs
df = nba.get_season_leaders(2022, info='reb', n=5,
                            playoffs=True, per_game=False)
print(df)

# Get info from current coaches
df = nba.get_coach_data(2023)
print(df)

# Get stats from individual player
df = nba.get_player_stats('Bruno Caboclo')
print(df)

# Get 2003 draft information
df = nba.get_draft_info(2003)
print(df)

# Get current season playoffs probabilities for eastern conference
df = nba.get_playoffs_probs('east')
print(df)

# Get information on rookies
df = nba.get_rookies(2023)
print(df)

# Get birthdays from today
df = nba.get_birthdays()
print(df)

# Get all MVPs
df = nba.get_awards('mvp')
print(df)
