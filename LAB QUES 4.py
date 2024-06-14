import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Temperature': [10, 12, 15, 18, 20],  
    'Rainfall': [50, 40, 60, 30, 70]  
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Trends')
plt.grid(True)
plt.show()

plt.scatter(df['Temperature'], df['Rainfall'])
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.title('Temperature vs. Rainfall')
plt.grid(True)
plt.show()
