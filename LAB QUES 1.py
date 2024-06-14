import pandas as pd
import matplotlib.pyplot as plt

data = {
    'OrderID': [1, 2, 3, 4],
    'CustomerID': ['A', 'B', 'A', 'C'],
    'ProductID': ['P1', 'P2', 'P1', 'P3'],
    'Quantity': [5, 3, 2, 4],
    'TotalPrice': [100, 50, 80, 120]
}

df = pd.DataFrame(data)

print(df.head())
print(df.info())
print(df.describe())

df.dropna(inplace=True)

df['TotalOrderValue'] = df['Quantity'] * df['TotalPrice']

revenue_per_customer = df.groupby('CustomerID')['TotalOrderValue'].sum()

df['OrderDate'] = pd.to_datetime('2024-06-01')  
df.set_index('OrderDate', inplace=True)
df.resample('ME')['TotalOrderValue'].sum().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Monthly Total Revenue')
plt.show()
