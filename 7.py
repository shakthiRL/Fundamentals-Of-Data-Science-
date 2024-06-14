import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data for a month
data = {
    'day': range(1, 6),  # Days of the month from 1 to 30
    'sales': [60,115, 120, 130, 125, 195]  # Random sales data
}
sales_data = pd.DataFrame(data)
# Line plot of sales over the month
plt.figure(figsize=(10, 5))
plt.plot(sales_data['day'], sales_data['sales'], marker='o', linestyle='-', color='b')
plt.title('Sales Over the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Scatter plot of sales over the month
plt.figure(figsize=(10, 5))
plt.scatter(sales_data['day'], sales_data['sales'], color='r')
plt.title('Sales Over the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Bar plot of sales over the month
plt.figure(figsize=(10, 5))
plt.bar(sales_data['day'], sales_data['sales'], color='g')
plt.title('Sales Over the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


