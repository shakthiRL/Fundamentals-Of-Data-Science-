import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_customers = 1000
customer_ids = np.arange(1, n_customers + 1)
amount_spent = np.random.normal(100, 50, n_customers)  # Normal distribution for amount spent
items_purchased = np.random.poisson(10, n_customers)   # Poisson distribution for items purchased

# Create DataFrame
data = {
    'CustomerID': customer_ids,
    'AmountSpent': amount_spent,
    'ItemsPurchased': items_purchased
}
df = pd.DataFrame(data)

# Display sample of the dataset
print(df.head())

# Step 2: Data preprocessing
X = df[['AmountSpent', 'ItemsPurchased']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Build K-Means clustering model
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)

# Step 4: Visualize clusters
df['Cluster'] = kmeans.labels_

plt.figure(figsize=(10, 6))
for cluster in sorted(df['Cluster'].unique()):
    plt.scatter(df[df['Cluster'] == cluster]['AmountSpent'], 
                df[df['Cluster'] == cluster]['ItemsPurchased'],
                label=f'Cluster {cluster}')

plt.title('Customer Segments based on Spending and Purchase Behavior')
plt.xlabel('Amount Spent')
plt.ylabel('Items Purchased')
plt.legend()
plt.show()
