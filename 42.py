from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Example dataset with house features and prices
# Replace this with your actual dataset or data loading mechanism
# Example features: area (in sq. ft.), number of bedrooms
data = {
    'Area': [1500, 2000, 1700, 1800, 2100],
    'Bedrooms': [3, 4, 3, 4, 3],
    'Price': [300000, 400000, 350000, 380000, 420000]
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 1: Prepare the data
X = df[['Area', 'Bedrooms']]  # Features
y = df['Price']  # Target variable

# Step 2: Build a Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 3: Accept user input for a new house
print("\nEnter details for the new house:")
area = float(input("Area (sq. ft.): "))
bedrooms = int(input("Number of bedrooms: "))

# Step 4: Predict the price of the new house
new_house = np.array([[area, bedrooms]])
predicted_price = model.predict(new_house)

# Step 5: Output the predicted price
print(f"\nThe predicted price of the new house is: ${predicted_price[0]:,.2f}")
