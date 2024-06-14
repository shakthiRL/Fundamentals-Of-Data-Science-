import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'total_amount_spent': [120.50, 340.10, 150.00, 220.25, 130.00, 90.50, 500.75, 80.00, 230.60, 170.00],
    'frequency_of_visits': [10, 30, 15, 20, 12, 5, 40, 4, 18, 9]
}
df = pd.DataFrame(data)

X = df[['total_amount_spent', 'frequency_of_visits']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_amount_spent', y='frequency_of_visits', hue='cluster', data=df, palette='viridis', s=100, alpha=0.7)
plt.title('Customer Segments based on Spending and Visit Frequency')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.legend(title='Cluster')
plt.show()

centroids = kmeans.cluster_centers_
print("Centroids of the clusters:")
print(centroids)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_amount_spent', y='frequency_of_visits', hue='cluster', data=df, palette='viridis', s=100, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', label='Centroids', marker='X')
plt.title('Customer Segments with Centroids')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.legend(title='Cluster')
plt.show()
