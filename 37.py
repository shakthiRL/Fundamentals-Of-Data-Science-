import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Step 1: Load and explore the dataset
# Example dataset with house features and prices
data = {
    'HouseSize': [1500, 1800, 2200, 1600, 1900],
    'NumBedrooms': [3, 4, 3, 3, 4],
    'Location': ['CityA', 'CityB', 'CityA', 'CityB', 'CityC'],
    'Price': [300000, 400000, 330000, 360000, 410000]
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 2: Perform bivariate analysis (select 'HouseSize' as the feature)
feature = 'HouseSize'
target = 'Price'

plt.figure(figsize=(8, 6))
plt.scatter(df[feature], df[target], color='blue', label='Data points')
plt.title(f'Bivariate Analysis: {feature} vs {target}')
plt.xlabel(feature)
plt.ylabel(target)
plt.grid(True)
plt.legend()
plt.show()

# Step 3: Build the linear regression model
X = df[[feature]]  # Feature matrix (independent variable)
y = df[target]     # Target variable (dependent variable)

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate model performance
# Make predictions
y_pred = model.predict(X_test)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2:.4f}')

# Calculate mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.4f}')

# Plotting the regression line
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual data points')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
plt.title(f'Linear Regression: {feature} vs {target}')
plt.xlabel(feature)
plt.ylabel(target)
plt.grid(True)
plt.legend()
plt.show()
