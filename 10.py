import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Sample data
data = {'Age': [23, 24, 31, 33, 36, 40, 43, 48, 52, 57, 59, 60, 61, 63, 64, 67, 70, 74],
        '%Fat': [15.1, 18.7, 22.6, 25.5, 29.7, 32.1, 35.2, 37.8, 40.5, 41.2, 42.7, 45.6, 47.8, 49.2, 50.1, 51.8, 53.3, 54.6]}
df = pd.DataFrame(data)

# Calculate statistics
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

mean_fat = df['%Fat'].mean()
median_fat = df['%Fat'].median()
std_fat = df['%Fat'].std()

print("Mean Age:", mean_age)
print("Median Age:", median_age)
print("Standard Deviation of Age:", std_age)
print("Mean %Fat:", mean_fat)
print("Median %Fat:", median_fat)
print("Standard Deviation of %Fat:", std_fat)

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Boxplots
sns.boxplot(y=df['Age'], ax=axes[0, 0]).set_title('Boxplot of Age')
sns.boxplot(y=df['%Fat'], ax=axes[0, 1]).set_title('Boxplot of %Fat')

# Scatter plot
sns.scatterplot(x='Age', y='%Fat', data=df, ax=axes[0, 2]).set_title('Scatter Plot of Age vs %Fat')

# Q-Q plots
stats.probplot(df['Age'], dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot of Age')
stats.probplot(df['%Fat'], dist="norm", plot=axes[1, 1])
axes[1, 1].set_title('Q-Q Plot of %Fat')

# Hide empty subplot
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()
