import pandas as p

data = p.read_csv('Population Data.csv')
x = data.popu.mean()
y = data[(data.popu > x) & (data.country == 'France')]
y.to_csv('output file.csv')