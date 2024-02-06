import pandas as p

data = p.read_csv('Population Data.csv')
# print(type(data['pop']))
# pop = p.Series([1000, 5000, 500], index=['london', 'berlin', 'tokyo'])
# print(pop.index)
# print(pop)
# print(pop[0])

colors = p.Series(['blue', 'red', 'green', 'yellow', 'cyan'], index=[1, 2, 3, 4, 5])
# print(colors[1]) prints blue but it should print red because red is at index 1
# so to avoid this confusion we use loc and iloc method

print(colors.loc[1])  # it checks label index--- op = blue
print(colors.iloc[1])  # it checks positional index--- op = red
print(colors.loc[1:2])  # last element is included
print(colors.iloc[1:2])  # last element is excluded
