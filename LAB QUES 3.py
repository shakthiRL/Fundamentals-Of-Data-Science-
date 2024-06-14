import pandas as pd
import matplotlib.pyplot as plt

data = {
    'OrderDate': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Clothing'],
    'TotalSales': [1000, 800, 1200, 600, 900]
}

df = pd.DataFrame(data)

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
monthly_sales = df.groupby(df['OrderDate'].dt.to_period('M'))['TotalSales'].sum()

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index.to_timestamp(), monthly_sales.values, marker='o', linestyle='-', color='b')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trends')
plt.grid(True)
plt.show()

plt.scatter(df['ProductCategory'], df['TotalSales'])
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.title('Product Performance: Sales vs. Category')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

category_sales = df.groupby('ProductCategory')['TotalSales'].sum()
plt.figure(figsize=(10, 6))
plt.bar(category_sales.index, category_sales.values)
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.title('Sales by Product Category')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
