import pandas as pd
import basic as b
import missingValue as mv

wine = pd.read_csv('winequality-red.csv')
##-----------Summary
wine.pH.describe()
print(wine.pH.describe())
# print(wine.pH.mean())
# print(wine.pH.unique())
# print(wine.pH.value_counts())
# print(wine.tail())
# print(wine.describe())
# pH=wine['pH']
# print(pH)
# print(wine['pH'][0])
# ph_alcohol=wine[['pH','alcohol']]
# print(ph_alcohol)
# print(wine.dtypes)

##---------Dataframe info
# wine.info()
## no.rows
# print(len(wine))
##no.columns
# print(len(wine.columns))
# no. rows and columns
# print(wine.shape)
# print(wine.size)
##memory usage for each column
# print(wine.memory_usage())

##------- Basic
# b.index(wine)
# b.index_end(wine)
# b.set_index(wine)
# b.label_selection(wine)
# b.more_label_selectiom(wine)
# b.show_column(wine)
# b.conditional_selection(wine)
# b.in_in_list(wine)
# b.grouping(wine)
# b.sorting(wine)
# b.sorting(wine)
# b.mapping(wine)
# b.remane(wine)
# b.rename_another(wine)
# b.drop_column(wine)
# b.adding_row(wine)
# b.to_numpy(wine)
# b.wine_ph_series(wine)
# b.truncate(wine)
b.iteration(wine)



##------------Missing Value
# mv.not_empty(wine)
# mv.wine_isnull(wine)
# mv.missed_filled(wine)
# mv.replace(wine)


wine.info()
