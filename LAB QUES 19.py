import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder

data = {
    'Mileage': [50000, 60000, 30000, 35000, 40000],
    'Age': [3, 2, 5, 1, 4],
    'Brand': ['Toyota', 'BMW', 'Honda', 'BMW', 'Toyota'],
    'Engine Type': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol'],
    'Price': [25000, 30000, 18000, 40000, 21000]
}
df = pd.DataFrame(data)

label_encoders = {}
for col in ['Brand', 'Engine Type']:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

X = df[['Mileage', 'Age', 'Brand', 'Engine Type']]
y = df['Price']

tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(X, y)

def predict_car_price(mileage, age, brand, engine_type):
    brand_encoded = label_encoders['Brand'].transform([brand])[0]
    engine_type_encoded = label_encoders['Engine Type'].transform([engine_type])[0]
    
    predicted_price = tree_reg.predict([[mileage, age, brand_encoded, engine_type_encoded]])[0]
    
    tree_rules = export_text(tree_reg, feature_names=['Mileage', 'Age', 'Brand', 'Engine Type'])
    print("Decision Path:")
    print(tree_rules)
    
    return predicted_price

print("\nExample Usage:")
predicted_price = predict_car_price(45000, 2, 'Toyota', 'Petrol')
print(f"\nPredicted Price: ${predicted_price:.2f}")
