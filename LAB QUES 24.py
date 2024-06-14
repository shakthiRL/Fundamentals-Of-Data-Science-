# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Sample dataset (replace with your actual dataset)
data = {
    'UsageMinutes': [300, 400, 200, 350, 500],
    'ContractDuration': [1, 2, 1, 3, 2],
    'Age': [25, 30, 21, 28, 35],
    'Churn': [0, 1, 0, 1, 0]  # 0 for not churned, 1 for churned
}
df = pd.DataFrame(data)

# Standardize numerical features
scaler = StandardScaler()
df[['UsageMinutes', 'ContractDuration', 'Age']] = scaler.fit_transform(df[['UsageMinutes', 'ContractDuration', 'Age']])

# Select features (UsageMinutes, ContractDuration, Age)
X = df[['UsageMinutes', 'ContractDuration', 'Age']]
y = df['Churn']

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Function to predict churn for new customer
def predict_churn(usage_minutes, contract_duration, age):
    X_new = scaler.transform([[usage_minutes, contract_duration, age]])  # Scale new data
    churn_prob = model.predict_proba(X_new)[0][1]  # Probability of churn
    return churn_prob

# Example usage
print("Enter the details of the new customer:")
usage_minutes = float(input("Usage Minutes: "))
contract_duration = int(input("Contract Duration (in months): "))
age = int(input("Age: "))

# Predict churn probability for the new customer
churn_prob = predict_churn(usage_minutes, contract_duration, age)

# Determine churn prediction based on probability threshold (e.g., 0.5)
if churn_prob >= 0.5:
    print(f"Prediction: The new customer is likely to churn with a probability of {churn_prob:.2f}.")
else:
    print(f"Prediction: The new customer is unlikely to churn with a probability of {churn_prob:.2f}.")
