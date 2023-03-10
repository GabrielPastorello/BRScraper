from BRScraper import gleague

# Get all MVP winners
df = gleague.get_awards('mvp')
print(df)

# Get all DPOY winners
df = gleague.get_awards('dpoy')
print(df)

# Get eastern conference standings
df = gleague.get_standings(2023,'east')
print(df)

# Get total standings in Showcase Cup
df = gleague.get_standings(2023,'total',showcase=True)
print(df)
