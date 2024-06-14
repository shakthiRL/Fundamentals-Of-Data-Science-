import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data creation (normally, you would load this from a CSV or other data source)
data = {
    'SmokingHabits': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],  # Number of cigarettes per day
    'LungCancerIncidence': [5, 15, 20, 40, 60, 80, 100, 120, 140, 160]  # Number of lung cancer cases per 1000 individuals
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculating the correlation coefficient
correlation_coefficient = df['SmokingHabits'].corr(df['LungCancerIncidence'])
print(f"\nCorrelation coefficient between smoking habits and lung cancer incidence: {correlation_coefficient:.2f}")

# Creating a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['SmokingHabits'], df['LungCancerIncidence'], color='blue')
plt.title('Scatter Plot of Smoking Habits vs. Lung Cancer Incidence')
plt.xlabel('Smoking Habits (Number of cigarettes per day)')
plt.ylabel('Lung Cancer Incidence (Cases per 1000 individuals)')
plt.grid(True)
plt.show()
