import pandas as pd


##data which are not empty
def not_empty(wine):
    return wine.loc[wine.quality.notnull()]


##missing data and replace
def wine_isnull(wine):
    wine[pd.isnull(wine.quality)]
    print(wine[pd.isnull(wine.quality)])


def missed_filled(wine):
    wine.quality.fillna("missed")
    print(wine.quality.fillna("missed"))


def replace(wine):
    wine.quality.replace('salam', 'nasrin')
    print(wine.quality.replace('salam', 'nasrin'))
