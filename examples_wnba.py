from BRScraper import wnba

# Get all stats from player
df = wnba.get_player_stats('Sabrina Ionescu')
print(df)

# Get all MVP winners
df = wnba.get_awards('mvp')
print(df)

# Get all DPOY winners
df = wnba.get_awards('dpoy')
print(df)

# Get eastern conference standings
df = wnba.get_standings(2022,'east')
print(df)

# Get total standings in Showcase Cup
df = wnba.get_standings(2022,'total')
print(df)

# Get general info about WNBA history
df = wnba.get_general_info()
print(df)

# Get information about WNBA draft
df = wnba.get_draft_info(2022)
print(df)
