import pandas as pd
import matplotlib.pyplot as plt

# Sample data creation (normally, you would load this from a CSV or other data source)
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5, 7, 12, 18, 22, 26, 28, 27, 23, 18, 12, 7],  # in degrees Celsius
    'Rainfall': [78, 60, 55, 45, 50, 70, 80, 85, 75, 65, 85, 90]  # in mm
}

# Creating DataFrame
df = pd.DataFrame(data)

# Line Plot for Temperature
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Line Plot for Rainfall
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Rainfall'], marker='o', linestyle='-', color='g')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter Plot for Temperature
plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Temperature'], color='r')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter Plot for Rainfall
plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Rainfall'], color='c')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
