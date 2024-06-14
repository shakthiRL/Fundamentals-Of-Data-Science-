import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Truck ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Distance Traveled (in miles)': [120, 150, 135, 140, 125, 130, 140, 145, 150, 133]
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Calculate the mean, median, and mode
mean_distance = df['Distance Traveled (in miles)'].mean()
median_distance = df['Distance Traveled (in miles)'].median()
mode_distance = df['Distance Traveled (in miles)'].mode()[0]

# Display the calculated values
mean_distance, median_distance, mode_distance

# Plotting the distribution of distances traveled
plt.figure(figsize=(10, 6))
plt.hist(df['Distance Traveled (in miles)'], bins=5, edgecolor='black', alpha=0.7)
plt.axvline(mean_distance, color='r', linestyle='dashed', linewidth=1, label=f'Mean: {mean_distance:.2f}')
plt.axvline(median_distance, color='g', linestyle='dashed', linewidth=1, label=f'Median: {median_distance}')
plt.axvline(mode_distance, color='b', linestyle='dashed', linewidth=1, label=f'Mode: {mode_distance}')
plt.title('Distribution of Distances Traveled by Trucks')
plt.xlabel('Distance Traveled (in miles)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
