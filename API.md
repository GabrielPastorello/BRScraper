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
Gets the stats of NBA players from a given season, format and .

Parameters:
  - **`season`**: Desired season (from `'xxxx-xx'` to `'2022-23'`) 
  - **`info`**: Desired data format (one of `'per_game'`,`'totals'`,`'advanced'`,`'per_36'`,`'per_100'`). Default value is `'per_game'`. 
  - **`playoffs`**: Whether to return numbers from the playoffs or regular season (one of `True`,`False`). Default value is `False`.