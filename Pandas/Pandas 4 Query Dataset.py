import pandas as p

data = p.read_csv('Population Data.csv')
# print(data[data.popu > 1000000])
# print(data[data.country == 'Russia'])
# print(data[data.popu.notnull()])
# print(data[data.country.str.startswith('L')])
# print(data[data.country.str.endswith('l')])
# print(data[(data.city.str.endswith('e')) & (data.country == 'Germany')])
# print(data[(data.popu < 1000000) & (data.country == 'Spain')])
x = data.popu.mean()
y = data[(data.popu > x) & (data.country == 'France')]
print(y)