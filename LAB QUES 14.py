import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'body_fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

mean_age = df['age'].mean()
median_age = df['age'].median()
std_age = df['age'].std()

mean_body_fat = df['body_fat'].mean()
median_body_fat = df['body_fat'].median()
std_body_fat = df['body_fat'].std()

print("Age:")
print(f"Mean: {mean_age:.2f}")
print(f"Median: {median_age}")
print(f"Standard Deviation: {std_age:.2f}\n")

print("%Fat:")
print(f"Mean: {mean_body_fat:.2f}")
print(f"Median: {median_body_fat}")
print(f"Standard Deviation: {std_body_fat:.2f}")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df.boxplot(column=['age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
df.boxplot(column=['body_fat'])
plt.title('Boxplot of %Fat')
plt.show()

plt.figure(figsize=(6, 6))
plt.scatter(df['age'], df['body_fat'])
plt.title('Scatter Plot of Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.show()

plt.figure(figsize=(6, 6))
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.show()

plt.figure(figsize=(6, 6))
stats.probplot(df['body_fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of %Fat')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.show()
