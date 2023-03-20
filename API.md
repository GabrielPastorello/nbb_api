# NBB

For code examples, check the `examples.py` file.

**Importing:**
```
from nbb_api import nbb
```

**Functions:**
### `get_stats(season, fase, categ, tipo='avg', quem='athletes', sofrido=False)`
Gets the individual statistics of all NBB players from a given season.

Parameters:
  - **`season`**: Desired season (from `'2008-09'` to `'2022-23'`)
  - **`fase`**: Desired season phase (one of `'regular'`, `'playoffs'`, `'total'`)
  - **`categ`**: Desired category of stats (one of `'cestinhas'`, `'rebotes'`, `'assistencias'`, `'arremessos'`, `'bolas-recuperadas'`, `'tocos'`, `'erros'`, `'eficiencia'`, `'duplos-duplos'`, `'enterradas'`)
  - **`tipo`**: Data format (one of `'avg'`, `'sum'`). Default value is `'avg'`.
  - **`quem`**: Whether to return data from players or teams (one of `'athletes'`, `'teams'`). Default value is `'athletes'`.
  - **`sofrido`**:  Whether to return numbers suffered by the team (one of `True`, `False`). *Only meaningful for team stats*. Default value is `False`.  
  
### `get_classificacao(season)`
Gets the standings of NBB regular season from a given season.

Parameters:
  - **`season`**: Desired season (from `'2008-09'` to `'2022-23'`)  
  
### `get_placares(season, fase)`
Gets all the NBB scores from a given season.

Parameters:
  - **`season`**: Desired season (from `'2008-09'` to `'2022-23'`)
  - **`fase`**: Desired season phase (one of `'regular'`, `'playoffs'`, `'total'`)


# LDB

**Importing:**
```
from nbb_api import ldb
```

**Functions:**
### `get_stats(season, fase, categ, tipo='avg', quem='athletes', sofrido=False)`
Gets the individual statistics of all LDB players from a given season.

Parameters:
  - **`season`**: Desired season (from `2011` to `2022` without 2020)
  - **`fase`**: Desired season phase (one of `'regular'`, `'total'`)
  - **`categ`**: Desired category of stats (one of `'cestinhas'`, `'rebotes'`, `'assistencias'`, `'arremessos'`, `'bolas-recuperadas'`, `'tocos'`, `'erros'`, `'eficiencia'`, `'duplos-duplos'`, `'enterradas'`)
  - **`tipo`**: Data format (one of `'avg'`, `'sum'`). Default value is `'avg'`.
  - **`quem`**: Whether to return data from players or teams (one of `'athletes'`, `'teams'`). Default value is `'athletes'`.
  - **`sofrido`**:  Whether to return numbers suffered by the team (one of `True`, `False`). *Only meaningful for team stats*. Default value is `False`.  
  
### `get_classificacao(season)`
Gets the standings of LDB regular season from a given season.

Parameters:
  - **`season`**: Desired season (from `2011` to `2022` without 2020)

### `get_placares(season, fase)`
Gets all the LDB scores from a given season.

Parameters:
  - **`season`**: Desired season (from `2011` to `2022` without 2020)
  - **`fase`**: Desired season phase (one of `'regular'`, `'total'`)  
  
# Liga Ouro

**Importing:**
```
from nbb_api import liga_ouro
```

**Functions:** 
### `get_classificacao(season)`
Gets the standings of Liga Ouro regular season from a given season.

Parameters:
  - **`season`**: Desired season (from `2014` to `2019`)  
  
### `get_placares(season, fase)`
Gets all the Liga Ouro scores from a given season.

Parameters:
  - **`season`**: Desired season (from `2014` to `2019`)
  - **`fase`**: Desired season phase (one of `'regular'`, `'playoffs'`, `'total'`)
