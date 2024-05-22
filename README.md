<p align="center">
<img src="https://user-images.githubusercontent.com/57769272/224566374-c8c748c7-c663-489f-8b98-d7041ab4092a.png" width="150">
</p>
<p align="center">
    <a href="https://pypi.org/project/nbb-api/">
        <img src="https://img.shields.io/pypi/v/nbb-api" alt="pypi" />
    </a>
    <a href="https://pypi.org/project/nbb-api/">
        <img src="https://img.shields.io/pypi/pyversions/nbb-api" alt="python version" />
    </a>
    <a href="https://pypi.org/project/nbb-api/">
        <img src="https://img.shields.io/pypi/l/nbb-api" alt="license" />
    </a>
</p>

# 🏀🇧🇷 nbb_api

Python package for easy access to Brazilian basketball data through scraping of [LNB](https://lnb.com.br/) website.

This allows users to obtain statistics, standings, and scores for various seasons and phases of the following tournaments:
- **NBB** (Novo Basquete Brasil)
- **LDB** (Liga de Desenvolvimento de Basquete)
- **Liga Ouro**

## 🚀 Installing
### Via `pip`
Install with the following command:

```
pip install nbb-api
```

## 📖 Documentation
For documentation about the API methods refer to [the documentation](https://github.com/GabrielPastorello/nbb_api/blob/main/API.md).

## 🔌 Example of use
```
from nbb_api import nbb
```

```
nbb.get_stats('2022-23','regular','cestinhas').head()
```
Output:
|     | Jogador       | Equipe          | JO | Min   | Pts   | 3P      | 2P    | LL   | Camisa | Temporada |
| --- | ------------- | --------------- | -- | ----- | ----- | ------- | ----- | ---- | ------ | --------- |
| 0   | McClanahan    | Fortaleza B. C. | 27 | 34.11 | 20.89 | 6.11    | 10.89 | 3.89 | 22     | 2022-23   |
| 1   | Antonio       | UNIFACISA       | 26 | 31.74 | 17.96 | 6.00    | 8.85  | 3.12 | 11     | 2022-23   |
| 2   | Thomas        | Corinthians     | 27 | 32.13 | 17.67 | 5.44    | 8.15  | 4.07 | 0      | 2022-23   |
| 3   | Lucas Mariano | Sesi Franca     | 22 | 27.41 | 17.59 | 7.23    | 7.64  | 2.73 | 28     | 2022-23   |
| 4   | Lucas Dias    | Sesi Franca     | 20 | 30.65 | 17.50 | 5.85    | 8.60  | 3.05 | 9      | 2022-23   |

Use it wisely!
