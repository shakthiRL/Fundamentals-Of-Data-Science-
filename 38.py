import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text

# Step 1: Load the car dataset (replace with your actual dataset)
# Example dataset with car features and prices
data = {
    'Mileage': [60000, 80000, 30000, 40000, 25000],
    'Age': [6, 8, 3, 5, 2],
    'Brand': ['Toyota', 'BMW', 'Honda', 'Toyota', 'Ford'],
    'EngineType': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol'],
    'Price': [15000, 18000, 12000, 17000, 14000]
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 2: Build a CART model (Decision Tree Regressor)
X = df[['Mileage', 'Age']]  # Features
y = df['Price']  # Target variable

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X, drop_first=True)

# Train the Decision Tree Regressor
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Step 3: Accept user input for a new car
print("\nEnter details for the new car:")
mileage = int(input("Mileage (in km): "))
age = int(input("Age (in years): "))
brand = input("Brand: ")
engine_type = input("Engine Type (Petrol/Diesel): ")

# Step 4: Predict car price based on user input
# Convert user input into a format compatible with the model
new_car = pd.DataFrame({
    'Mileage': [mileage],
    'Age': [age],
    'Brand': [brand],
    'EngineType': [engine_type]
})

# Convert categorical variables to numerical using one-hot encoding
new_car = pd.get_dummies(new_car)

# Ensure new_car has all necessary columns after one-hot encoding
missing_cols = set(X.columns) - set(new_car.columns)
for col in missing_cols:
    new_car[col] = 0

# Reorder columns to match the training data
new_car = new_car[X.columns]

# Predict the price of the new car
predicted_price = model.predict(new_car)
print(f"\nPredicted Price of the Car: ${predicted_price[0]:,.2f}")

# Step 5: Display decision path
# Get the decision path as text
tree_rules = export_text(model, feature_names=list(X.columns))
print("\nDecision Path:")
print(tree_rules)
