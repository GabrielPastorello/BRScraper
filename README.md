<p align="center">
<img src="https://github.com/GabrielPastorello/BRScraper/assets/57769272/cb95ffa0-0806-4469-89bb-28ba6bc7ff00" width="150">
</p>
<p align="center">
    <a href="https://pypi.org/project/BRScraper/">
        <img src="https://img.shields.io/pypi/v/BRScraper" alt="pypi" />
    </a>
    <a href="https://pypi.org/project/BRScraper/">
        <img src="https://img.shields.io/pypi/pyversions/BRScraper" alt="python version" />
    </a>
    <a href="https://pypi.org/project/BRScraper/">
        <img src="https://img.shields.io/pypi/l/BRScraper" alt="license" />
    </a>
</p>

# 🏀 BRScraper

Python package for easy access to basketball data through scraping of [Basketball Reference](https://www.basketball-reference.com/) website.

This allows users to obtain statistics, standings, and scores for various seasons and phases of the following tournaments:
- **NBA**
- **G-League**
- **International Tournaments** (Olympics, EuroLeague, EuroCup and international leagues from: Spain, Australia, China, France, Greece, Israel, Italy, Turkey, Russia and ABA)

## 🚀 Installing
### Via `pip`
This library was written as an exercise for creating my first PyPi package. Hopefully you will find it valuable!
Install with the following command:

```
pip install BRScraper
```

## 📖 Documentation
For documentation about the API methods refer to [the documentation](https://github.com/GabrielPastorello/BRScraper/blob/main/API.md).

## 🔌 Example of use
```
from BRScraper import nba
```

```
# All players stats per game regular season
nba.get_stats(2023, info='per_game', playoffs=False, rename=False).head()
```
Output:
|     | Player           | Pos | Age | Tm  | G  | GS | ... | STL | BLK | TOV | PF  | PTS  | Season  |
| --- | ---------------- | --- | --- | --- | -- | -- | --- | --- | --- | --- | --- | ---- | ------- |
| 0   | Precious Achiuwa | C   | 23  | TOR | 55 | 12 | ... | 0.6 | 0.5 | 1.1 | 1.9 | 9.2  | 2022-23 |
| 1   | Steven Adams     | C   | 29  | MEM | 42 | 42 | ... | 0.9 | 1.1 | 1.9 | 2.3 | 8.6  | 2022-23 |
| 2   | Bam Adebayo      | C   | 25  | MIA | 75 | 75 | ... | 1.2 | 0.8 | 2.5 | 2.8 | 20.4 | 2022-23 |
| 3   | Ochai Agbaji     | SG  | 22  | UTA | 59 | 22 | ... | 0.3 | 0.3 | 0.7 | 1.7 | 7.9  | 2022-23 |
| 4   | Santi Aldama     | SF  | 22  | MEM | 77 | 20 | ... | 0.6 | 0.6 | 0.8 | 1.9 | 9.0  | 2022-23 |

More examples in the files.

Use it wisely!
