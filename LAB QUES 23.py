# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset (replace with your actual dataset)
data = {
    'Area': [1500, 2000, 2500, 3000, 3500],
    'Bedrooms': [3, 4, 3, 5, 4],
    'Location': ['A', 'B', 'A', 'C', 'B'],
    'Price': [300000, 400000, 500000, 600000, 700000]
}
df = pd.DataFrame(data)

# Convert categorical variable 'Location' to dummy variables
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Select features (Area, Bedrooms, Location_B)
X = df[['Area', 'Bedrooms', 'Location_B']]
y = df['Price']

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Function to predict price of new house
def predict_price(area, bedrooms, location):
    location_b = 1 if location == 'B' else 0  # Convert location to Location_B dummy variable
    X_new = [[area, bedrooms, location_b]]
    price = model.predict(X_new)
    return price[0]

# Example usage
print("Enter the details of the new house:")
area = float(input("Area (sqft): "))
bedrooms = int(input("Number of Bedrooms: "))
location = input("Location (A, B, C): ")

# Predict price of the new house
predicted_price = predict_price(area, bedrooms, location)
print(f"Predicted Price: ${predicted_price:.2f}")
