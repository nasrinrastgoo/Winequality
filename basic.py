import pandas as pd


# indexing
##index based selection
def index(wine):
    wine.iloc[2]
    print(wine.iloc[2])


## indexing from the end
def index_end(wine):
    wine.iloc[-6:]
    print(wine.iloc[-6:])


# set index
def set_index(wine):
    wine.set_index('pH')


# reset indexing
# print(wine.sample(frac=1).reset_index(drop=True))

##show column, [row,column]
def show_column(wine):
    wine.iloc[:, 0]
    print(wine.iloc[:, 0])


# wine.iloc[:4,0]
# print(wine.iloc[:4,0])

##label based selection
def label_selection(wine, column):
    wine.loc[0, column]
    print(wine.loc[0, column])


def more_label_selectiom(wine):
    wine.loc[:, ['pH', 'alcohol']]
    print(wine.loc[:, ['pH', 'alcohol']])


# conditional selection
def conditional_selection(wine):
    wine.loc[wine.quality == 7]
    print(wine.loc[wine.quality == 7])


# wine.loc[(wine.quality == 7) & (wine.volatile_acidity == 0.56)]
# print(wine.loc[(wine.quality == 7) & (wine.volatile_acidity > 0.56)])
# wine.loc[(wine.quality == 7) | (wine.volatile_acidity == 0.56)]
# print(wine.loc[(wine.quality == 7) | (wine.volatile_acidity == 0.56)])

##is in a list of values
def in_in_list(wine):
    wine.loc[wine.quality.isin([7, 5])]
    print(wine.loc[wine.quality.isin([7, 5])])


# a list of unique values and how often they occur in the dataset
def unique_value(wine):
    wine.pH.value_counts()
    print(wine.pH.value_counts())


##---Grouping & Sorting
def grouping(wine):
    wine.groupby('quality').quality.count()
    print(wine.groupby('quality').quality.count())


# print(wine.quality.value_counts())
# print(wine.groupby('quality').quality.count().sort_values())
# wine.groupby('quality').pH.mean()
# print(wine.groupby('quality').pH.mean())
# print(wine.groupby('quality').alcohol.mean())
# wine.groupby('quality').alcohol.agg([min,max,len])
# print(wine.groupby('quality').alcohol.agg([min,max,len]))
# wine.groupby(['quality','alcohol'])
# wine_grouping=wine.groupby(['quality','alcohol']).pH.mean()
# print(wine_grouping)
# t=wine_grouping.index
# print(type(t))

##sort
def sorting(wine):
    wine_grouping_sort = wine.groupby(['quality', 'alcohol']).pH.mean().sort_values(ascending=False)
    print(wine_grouping_sort)


##---Map
def mapping(wine):
    wine_quality_mean = wine.quality.mean()
    print(wine.quality.map(lambda q: q - wine_quality_mean))


# print(wine.quality - wine_quality_mean)
# wine_quality_ph=wine.quality.apply(str) + "-" + wine.pH.apply(str)
# print(wine_quality_ph)

##-------rename
def remane(wine):
    wine_renamed = wine.rename(columns={'pH': 'pH_point'})
    wine = wine_renamed
    print(wine)


def rename_another(wine):
    wine.rename(index={0: 'first', 1: 'second'})
    print(wine.rename(index={0: 'first', 1: 'second'}))


# wine.rename_axis('wine',axis='rows').rename_axis('material_points',axis='columns')
# print(wine.rename_axis('wine',axis='rows').rename_axis('material_points',axis='columns'))

##----Drop
# drop a row
def drop(wine):
    wine.drop(1)
    print(wine.drop(1))


# print(wine.drop([1,2,3]))

# drop column
def drop_column(wine):
    wine.drop('pH', axis=1)
    print(wine.drop('pH', axis=1))


# wine.drop(columns='pH')
# print(wine.drop(columns='pH'))
# wine.drop(wine.columns[[10]],axis=1)
# print(wine.drop(wine.columns[[10]],axis=1))

##------add a row
def adding_row(wine):
    wine_2 = pd.DataFrame({'fixed_acidity': [4, 5],
                           'volatile_acidity': [0.1, 0.2],
                           'pH': [2, 3]})
    wine.append(wine_2, ignore_index=True)
    print(wine.append(wine_2, ignore_index=True))


##---Shuffle data
def shuffle(wine):
    wine.sample(frac=1)
    print(wine.sample(frac=1))


# convert dataframe to numpy
def to_numpy(wine):
    new_wine = pd.DataFrame(wine['pH'].head())
    print(new_wine.to_numpy(dtype='int'))

# convert series to numpy
def wine_ph_series(wine):
    wine_series=pd.Series(wine['pH'])
    print(wine_series.to_numpy())
