import pandas as pd
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [120, 150, 200, 180, 210]

plt.figure(figsize=(8, 6))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales (in $1000s)')
plt.grid(True)
plt.show()

plt.bar(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales (in $1000s)')
plt.title('Monthly Sales Data')
plt.grid(True)
plt.show()
