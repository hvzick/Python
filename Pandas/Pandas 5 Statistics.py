import pandas as p

data = p.read_csv('Population Data.csv')
# print(data.popu.sum())
# print(data.popu.min())
# print(data.popu.max())
# print(data.groupby('country')['popu'].sum())
print(data.groupby('country')['city'].count())