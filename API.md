# NBA

For code examples, check the `examples_nba.py` file.

**Importing:**
```
from BRScraper import nba
```

**Functions:**
### `get_current_salaries(info='players')`
Gets the current salaries for all players or teams.

Parameters:
  - **`info`**: Desired information (one of `'players'`, `'teams'`). Default value is `'players'`.  
  
### `get_stats(season, info='per_game', playoffs=False, rename=False)`
Gets the stats of NBA players from a given season and format.

Parameters:
  - **`season`**: Desired season (in format `2023`).
  - **`info`**: Desired data format (one of `'per_game'`,`'totals'`,`'advanced'`,`'per_36'`,`'per_100'`). Default value is `'per_game'`. 
  - **`playoffs`**: Whether to return numbers from the playoffs or regular season (one of `True`,`False`). Default value is `False`.
  - **`rename`**: Wheter to rename the columns to the selected `info` (one of `True`,`False`) (Example: if `info='per_game'` and `rename=True`, columns would be renamed as `'PTS_per_game'`, etc.). Default value is `False`.

### `get_standings(season, info='total')`
Gets the NBA standings from a given season.

Parameters:
  - **`season`**: Desired season (in format `2023`).
  - **`info`**: Desired information (one of `'total'`,`'east'`,`'west'`). Default value is `'total'`.

### `get_general_info()`
Gets general info from all NBA seasons such as champions, MVPs and league leaders.

### `get_season_leaders(season, info, n=10, playoffs=False, per_game=False)`
Get the season leaders in a certain category for a given season.

Parameters:
  - **`season`**: Desired season (in format `2023`).
  - **`info`**: Desired category (one of `'pts'`,`'reb'`,`'oreb'`,`'dreb'`,`'ast'`,`'stl'`,`'blk'`,`'fg%'`,`'ft%'`,`'3pt%'`,`'2pt%'`,`'efg%'`,`'ts%'`,`'fg'`,`'fga'`,`'2p'`,`'2pa'`,`'3p'`,`'3pa'`,`'fgm'`,`'ft'`,`'fta'`,`'min'`,`'tov'`,`'pf'`,`'per'`,`'ws'`,`'ows'`,`'dws'`,`'ws48'`,`'bpm'`,`'obpm'`,`'dbpm'`,`'vorp'`,`'ortg'`,`'drtg'`,`'usg%'`,`'trb%'`,`'orb%'`,`'ast%'`,`'drb%'`,`'stl%'`,`'blk%'`,`'tov%'`).
  - **`n`**: Number of players to select. Maximum of 20 for regular season and 10 for playoffs. Default value is `10`.
  - **`playoffs`**: Whether to return numbers from the playoffs or regular season (one of `True`,`False`). Default value is `False`.
  - **`per_game`**: Whether the desired ranking is on per game or total statistics.  Default value is `False`.

### `get_coach_data(season)`
Get information from current coaches.

Parameters:
  - **`season`**: Desired season (in format `2023`).

### `get_player_stats(name)`
Get stats from individual player career.

Parameters:
  - **`name`**: Name of the desired player (Example: `'Bruno Caboclo'`).

### `get_draft_info(season)`
Get draft information from a given season.

Parameters:
  - **`season`**: Desired season (in format `2023`).

### `get_playoffs_probs(conf)`
Get current season playoffs probabilities for a given conference.

Parameters:
  - **`conf`**: Desired conference (one of `'east'`,`'west'`).

### `get_rookies(season)`
Get information on rookies from a given season.

Parameters:
  - **`season`**: Desired season (in format `2023`).

### `get_birthdays()`
Get birthdays from today.

### `get_awards(award)`
Get all winners of a given award.

Parameters:
  - **`award`**: Desired award (one of `'mvp'`,`'roy'`,`'dpoy'`,`'smoy'`,`'tmoy'`,`'mip'`,`'citizenship'`,`'finals_mvp'`,`'playoffs_mvp'`,`'wcf_mvp'`,`'ecf_mvp'`,`'all_star_mvp'`,`'cpoy'`,`'player_of_the_seeding_games'`,`'tsn_mvp'`,`'tsn_roy'`,`'hustle'`,`'social_justice'`,`'coy'`,`'nbca_coy'`,`'eoy'`)


# G League

For code examples, check the `examples_gleague.py` file.

**Importing:**
```
from BRScraper import gleague
```

**Functions:**
### `get_awards(award)`
Get all winners of a given award.

Parameters:
  - **`award`**: Desired award (one of `'mvp'`,`'roy'`,`'dpoy'`,`'mip'`,`'ipoy'`,`'all_gleague'`,`'all_rookie'`,`'all_defense'`,`'sc_mvp'`)

### `get_standings(season, info='total', showcase=False)`
Gets the G League standings from a given season.

Parameters:
  - **`season`**: Desired season (in format `2023`).
  - **`info`**: Desired information (one of `'total'`,`'east'`,`'west'`). Default value is `'total'`.
  - **`showcase`**: Wheter to output standings from Showcase Cup (one of `True`,`False`). Default value is `False`.

# International Basketball

For code examples, check the `examples_international.py` file.

## Players

**Importing:**
```
from BRScraper.international import players
```

**Functions:**
### `get_player_stats(name)`
Get stats from individual player international career.

Parameters:
  - **`name`**: Name of the desired player (Example: `'Bruno Caboclo'`)

### `get_mvps()`
Get all MVPs from international leagues.

## Olympics

**Importing:**
```
from BRScraper.international import olympics
```

**Functions:**
### `get_stats(season, info='per_game', men=True, rename=False)`
Gets the stats of Olympics players from a given year and format.

Parameters:
  - **`season`**: Desired season (in format `2020`).
  - **`info`**: Desired data format (one of `'per_game'`,`'totals'`,`'per_36'`). Default value is `'per_game'`. 
  - **`men`**: Whether to return numbers from the Men's or Woman's Olympics (one of `True`,`False`). Default value is `True`.
  - **`rename`**: Wheter to rename the columns to the selected `info` (one of `True`,`False`) (Example: if `info='per_game'` and `rename=True`, columns would be renamed as `'PTS_per_game'`, etc.). Default value is `False`.

### `get_standings(season, men=True)`
Gets the Olympics standings from a given season.

Parameters:
  - **`season`**: Desired season (in format `2020`).
  - **`men`**: Whether to return numbers from the Men's or Woman's Olympics (one of `True`,`False`). Default value is `True`.

## International Leagues

**Importing:**

All the following have the same functions:
```
from BRScraper.international import euroleague
from BRScraper.international import eurocup
from BRScraper.international import acb # Spanish League
from BRScraper.international import nbl # Australian League
from BRScraper.international import cba # Chinese League
from BRScraper.international import lnb # French League
from BRScraper.international import greece # Greek League
from BRScraper.international import israel # Israeli League
from BRScraper.international import italy # Italian League
from BRScraper.international import turkey # Turkish League
from BRScraper.international import russia # Russian League
from BRScraper.international import aba # ABA League
```

**Functions:**
### `get_stats(season, info='per_game', rename=False)`
Gets the stats of players from a given year and format.

Parameters:
  - **`season`**: Desired season (in format `2023`).
  - **`info`**: Desired data format (one of `'per_game'`,`'totals'`,`'per_36'`). Default value is `'per_game'`. 
  - **`rename`**: Wheter to rename the columns to the selected `info` (one of `True`,`False`) (Example: if `info='per_game'` and `rename=True`, columns would be renamed as `'PTS_per_game'`, etc.). Default value is `False`.

### `get_standings(season)`
Gets the standings from a given season.

Parameters:
  - **`season`**: Desired season (in format `2023`).
