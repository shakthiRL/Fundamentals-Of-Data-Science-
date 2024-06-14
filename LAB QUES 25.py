# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Sample dataset (replace with your actual dataset)
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 35, 40, 45],
    'AnnualIncome': [50000, 80000, 60000, 70000, 90000],
    'SpendingScore': [50, 80, 70, 60, 85]
}
df = pd.DataFrame(data)

# Select features for clustering (AnnualIncome, SpendingScore)
X = df[['AnnualIncome', 'SpendingScore']]

# Train K-Means clustering model
k = 3  # Number of clusters (you can adjust this)
model = KMeans(n_clusters=k, random_state=42)
model.fit(X)

# Function to predict cluster for new customer
def predict_cluster(annual_income, spending_score):
    X_new = np.array([[annual_income, spending_score]])
    cluster = model.predict(X_new)
    return cluster[0]

# Example usage
print("Enter the shopping-related features of the new customer:")
annual_income = float(input("Annual Income: $"))
spending_score = float(input("Spending Score (1-100): "))

# Predict cluster for the new customer
predicted_cluster = predict_cluster(annual_income, spending_score)
print(f"Predicted Cluster: {predicted_cluster}")
