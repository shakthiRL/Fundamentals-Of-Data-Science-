import pandas as pd
import matplotlib.pyplot as plt

# Sample data creation (normally, you would load this from a CSV or other data source)
data = {
    'ProductCategory': ['Electronics', 'Clothing', 'Groceries', 'Books', 'Home & Kitchen', 'Sports', 'Toys'],
    'TotalSales': [120000, 85000, 95000, 65000, 115000, 75000, 50000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(df['ProductCategory'], df['TotalSales'], marker='o', linestyle='-', color='b')
plt.title('Total Sales by Product Category (Line Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['ProductCategory'], df['TotalSales'], color='r')
plt.title('Total Sales by Product Category (Scatter Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(df['ProductCategory'], df['TotalSales'], color='g')
plt.title('Total Sales by Product Category (Bar Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()
