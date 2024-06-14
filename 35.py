import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate synthetic data (replace this with your actual data loading logic)
n_customers = 1000
customer_ids = np.arange(1, n_customers + 1)
amount_spent = np.random.normal(100, 50, n_customers)  # Normal distribution for amount spent
frequency_visits = np.random.poisson(5, n_customers)   # Poisson distribution for frequency of visits

# Create DataFrame
data = {
    'CustomerID': customer_ids,
    'AmountSpent': amount_spent,
    'FrequencyVisits': frequency_visits
}
df = pd.DataFrame(data)

# Display sample of the dataset
print(df.head())

# Step 2: Preprocess the data and select features for clustering
X = df[['AmountSpent', 'FrequencyVisits']]

# Step 3: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Determine the optimal number of clusters using the Elbow method
def find_optimal_k(X_scaled):
    inertias = []
    sil_scores = []
    for k in range(2, 11):  # Trying different values of k from 2 to 10
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)  # Sum of squared distances to closest cluster center
        sil_scores.append(silhouette_score(X_scaled, kmeans.labels_))  # Silhouette score
    return inertias, sil_scores

inertias, sil_scores = find_optimal_k(X_scaled)

# Plotting the Elbow curve and Silhouette scores to determine the optimal k
plt.figure(figsize=(12, 4))

# Plotting Elbow curve
plt.subplot(1, 2, 1)
plt.plot(range(2, 11), inertias, marker='o', linestyle='--')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')

# Plotting Silhouette scores
plt.subplot(1, 2, 2)
plt.plot(range(2, 11), sil_scores, marker='o', linestyle='--')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Optimal k')

plt.tight_layout()
plt.show()

# Based on the Elbow method and Silhouette scores, choose the optimal value of k
optimal_k = 4  # Adjust based on the analysis from the plots or use a fixed value

# Step 5: Build the K-Means clustering model
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X_scaled)

# Step 6: Assign clusters back to the original dataset
df['Cluster'] = kmeans.labels_

# Step 7: Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(df['AmountSpent'], df['FrequencyVisits'], c=df['Cluster'], cmap='viridis', alpha=0.8, edgecolors='k')
plt.xlabel('Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segments based on Spending Patterns')
plt.colorbar(label='Cluster', ticks=range(optimal_k))
plt.show()
