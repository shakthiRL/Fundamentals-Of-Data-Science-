import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset creation
data = {
    'property_size': [1500, 2500, 1800, 2400, 3000, 1400, 2200, 2100, 1600, 2000],
    'num_bedrooms': [3, 4, 3, 4, 5, 3, 4, 4, 3, 4],
    'num_bathrooms': [2, 3, 2, 3, 4, 2, 3, 3, 2, 3],
    'location': ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'],
    'sale_price': [300000, 450000, 350000, 480000, 600000, 280000, 420000, 410000, 320000, 500000]
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Ensure data types are correct
df['property_size'] = df['property_size'].astype(float)
df['num_bedrooms'] = df['num_bedrooms'].astype(int)
df['num_bathrooms'] = df['num_bathrooms'].astype(int)
df['sale_price'] = df['sale_price'].astype(float)

# Display the data types
print("\nData types of the dataset:")
print(df.dtypes)

# Summary statistics
print("\nSummary statistics of the dataset:")
print(df.describe())


# Correlation heatmap
plt.figure(figsize=(10, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
