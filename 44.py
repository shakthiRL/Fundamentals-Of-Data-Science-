from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

# Example dataset with customer features
# Replace this with your actual dataset or data loading mechanism
# Example features: 'SpendingScore' and 'Frequency'
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'SpendingScore': [40, 65, 80, 10, 5, 90, 75, 25, 95, 30],
    'Frequency': [5, 3, 8, 1, 1, 9, 7, 2, 10, 4]
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 1: Prepare the data
X = df[['SpendingScore', 'Frequency']]  # Features

# Step 2: Build a K-Means clustering model
k = 3  # Number of clusters (you can adjust this)
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# Step 3: Accept user input for a new customer
print("\nEnter details for the new customer:")
spending_score = float(input("Spending score (0-100): "))
frequency = int(input("Frequency of purchases: "))

# Step 4: Predict the cluster for the new customer
new_customer = np.array([[spending_score, frequency]])
predicted_cluster = kmeans.predict(new_customer)

# Step 5: Output the predicted cluster
print(f"\nThe new customer is predicted to belong to cluster: {predicted_cluster[0]}")
