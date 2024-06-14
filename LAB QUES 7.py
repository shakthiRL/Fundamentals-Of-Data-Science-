import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start='2024-01-01', periods=90)
sales = np.random.randint(100, 200, size=(90,))

sales_data = pd.DataFrame({'date': dates, 'sales': sales})
sales_data['date'] = pd.to_datetime(sales_data['date'])

plt.figure(figsize=(10, 5))
plt.plot(sales_data['date'], sales_data['sales'], marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(sales_data['date'], sales_data['sales'], c='blue', marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

monthly_sales = sales_data.resample('ME', on='date').sum()

plt.figure(figsize=(10, 5))
plt.bar(monthly_sales.index, monthly_sales['sales'], color='green')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()
