from BRScraper.international import players # All international players

# All player stats
df = players.get_player_stats('Bruno Caboclo')
print(df)
# All MVPs from international leagues
df = players.get_mvps()
print(df)

from BRScraper.international import olympics

# All players stats per game (Men's Olympics)
df = olympics.get_stats(2020, 'per_game', men=True)
print(df)
# Get standings from 2020 (Women's Olympics)
df = olympics.get_standings(2020, men=False)
print(df)

#########################################
######### International Leagues #########
#########################################

from BRScraper.international import euroleague

# All players stats per game
df = euroleague.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = euroleague.get_standings(2023)
print(df)

from BRScraper.international import eurocup

# All players stats per game
df = eurocup.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = eurocup.get_standings(2023)
print(df)

from BRScraper.international import acb # Spanish League

# All players stats per 36 minutes
df = acb.get_stats(2023, 'per_36')
print(df)
# Get standings from 2022
df = acb.get_standings(2022)
print(df)

from BRScraper.international import nbl # Australian League

# All players total stats
df = nbl.get_stats(2023, 'totals')
print(df)
# Get standings from 2023
df = nbl.get_standings(2023)
print(df)

from BRScraper.international import cba # Chinese League

# All players total stats
df = cba.get_stats(2023, 'totals')
print(df)
# Get standings from 2023
df = cba.get_standings(2023)
print(df)

from BRScraper.international import lnb # French League

# All players stats per game
df = lnb.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = lnb.get_standings(2023)
print(df)

from BRScraper.international import greece # Greek League

# All players stats per game
df = greece.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = greece.get_standings(2023)
print(df)

from BRScraper.international import israel # Israeli League

# All players stats per game
df = israel.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = israel.get_standings(2023)
print(df)

from BRScraper.international import italy # Italian League

# All players stats per game
df = italy.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = italy.get_standings(2023)
print(df)

from BRScraper.international import turkey # Turkish League

# All players stats per game
df = turkey.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = turkey.get_standings(2023)
print(df)

from BRScraper.international import russia # Russian League

# All players stats per game
df = russia.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = russia.get_standings(2023)
print(df)

from BRScraper.international import aba # ABA League

# All players stats per game
df = aba.get_stats(2023, 'per_game')
print(df)
# Get standings from 2023
df = aba.get_standings(2023)
print(df)
