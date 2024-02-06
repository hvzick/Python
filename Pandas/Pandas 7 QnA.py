import pandas as p

data = p.read_csv('Sales.csv')
x = data.groupby(['customer_id', 'salesman_id']).agg({'amount': ['sum', 'count']})
x.columns = ['sum', 'count']
print(x)
x.to_csv('Sales_op.csv')