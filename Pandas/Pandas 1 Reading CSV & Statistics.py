# with open('Population Data.csv') as csvfile:
#     for rows in csvfile:
#         for rows in csvfile:
#         print(d)

# import csv

#
# with open('Population Data.csv') as csvfile:
#     data = csv.reader(csvfile)
#     for row in data:
#         print(row)

import pandas as p

data = p.read_csv('Population Data.csv')
# # print(data) # only prints first and last 5 rows
# # set print limit
# print(p.options.display.max_rows)  # to display max printing rows
# p.options.display.max_rows = 500  # to upgrade printing limit
#
p.set_option('display.max_rows', None)  # to remove limit
# print(type(data))
# print(len(data))  # for no of rows
# print(data.shape)  # for rows and columns
# print(data.head())  # first 5(default) rows
# print(data.tail(3))  # last 3(passed value) rows
# print(data.info())

# to check basic statistics
p.set_option('display.float_format', str)  # to print all values
basic_stats = data.describe(include='all')  # to include all columns
print(basic_stats)
