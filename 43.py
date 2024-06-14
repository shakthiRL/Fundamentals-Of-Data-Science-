from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

# Example dataset with customer features and churn status
# Replace this with your actual dataset or data loading mechanism
# Example features: usage minutes, contract duration
data = {
    'UsageMinutes': [300, 400, 350, 200, 500],
    'ContractMonths': [12, 24, 12, 6, 36],
    'Churn': [0, 1, 0, 1, 0]  # 0 for not churned, 1 for churned
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 1: Prepare the data
X = df[['UsageMinutes', 'ContractMonths']]  # Features
y = df['Churn']  # Target variable

# Step 2: Build a Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X, y)

# Step 3: Accept user input for a new customer
print("\nEnter details for the new customer:")
usage_minutes = float(input("Usage minutes: "))
contract_months = int(input("Contract duration (months): "))

# Step 4: Predict whether the new customer will churn
new_customer = np.array([[usage_minutes, contract_months]])
predicted_churn = model.predict(new_customer)

# Step 5: Output the predicted churn status
if predicted_churn[0] == 1:
    print("\nThe model predicts that the customer will churn.")
else:
    print("\nThe model predicts that the customer will not churn.")
