import pandas as p

data = p.read_csv('Population Data.csv')
# p.set_option('display.float_format', str)
# print(type(data['pop']))
# pop = p.Series([1000,5000,500], index=['london','berlin','tokyo'])
# print(pop.index)
# print(pop)

l = data['pop'].tolist()
# print(l)
# t = 0
# for i in range(0, len(l)):
#     t = t + l[i]
#
# print(t/len(l))

# or
avg = sum(l) / len(l)
# print(avg)

# or

mean = data['pop'].mean()
# print(mean)

max = data['pop'].max()
# print(max)

# print(data.name)  # it takes heading of csv file as an attribute and data as object
# # print(data.pop.max())  # it shows error because pop is a keyword so it cant be the heading in csv file
# print(data.name.max())  # it works fine

# creating data frames
population = p.Series([1000, 5000, 500], index=['london', 'berlin', 'tokyo'])
offices = p.Series([10, 50], index=['london', 'berlin'])
dataa = p.DataFrame({'pop': population, 'offices':offices})
# print(dataa)
# print(dataa.axes)
# print(dataa.axes[0])
# print(dataa.axes[1])
# print('pop' in data)
print(data.iloc[-2:, 1])  # -2: for row, 1 for column
