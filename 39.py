import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Step 1: Load and explore the dataset (replace with your actual dataset)
# Example dataset with customer features
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'AnnualIncome': [50000, 70000, 90000, 60000, 80000, 100000, 85000, 75000, 95000, 55000],
    'SpendingScore': [50, 80, 30, 70, 20, 90, 60, 40, 75, 35]
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 2: Data preprocessing
# Select relevant features for clustering (Age, AnnualIncome, SpendingScore)
X = df[['Age', 'AnnualIncome', 'SpendingScore']]

# Standardize features by scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Choose the number of clusters (K) using the Elbow method
# Elbow method to find optimal K
inertia = []
silhouette_scores = []
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plotting the Elbow curve and Silhouette scores
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(range(2, 8), inertia, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')

plt.subplot(1, 2, 2)
plt.plot(range(2, 8), silhouette_scores, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score')

plt.tight_layout()
plt.show()

# Based on the plots, select the optimal K (number of clusters)
optimal_k = 3  # Example based on Elbow method analysis

# Step 4: Build the K-Means clustering model
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X_scaled)

# Step 5: Interpret the clusters
# Add cluster labels to original dataset
df['Cluster'] = kmeans.labels_

# Analyze cluster characteristics (mean values)
cluster_means = df.groupby('Cluster').mean()

print("\nCluster Characteristics:")
print(cluster_means)

# Step 6: Visualize clusters (using PCA for dimensionality reduction and plotting)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans.labels_, cmap='viridis', edgecolor='k', s=100)
plt.title('PCA Plot of Clusters')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Cluster', ticks=range(optimal_k))
plt.grid(True)
plt.show()

# Step 7: Utilize segments for targeted marketing strategies
# Example: Analyze each cluster and tailor marketing campaigns accordingly
for cluster_id in range(optimal_k):
    print(f"\nCluster {cluster_id}:")
    print(df[df['Cluster'] == cluster_id])

# Note: Replace 'data' with your actual dataset loading logic using pd.read_csv(), etc.
