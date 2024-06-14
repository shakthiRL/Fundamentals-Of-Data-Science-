# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Sample dataset (replace with your actual dataset)
data = {
    'Symptom1': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'Symptom2': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'Symptom3': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    'Condition': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 for condition, 0 for no condition
}
df = pd.DataFrame(data)

# Select features (symptoms) and target variable (condition)
X = df[['Symptom1', 'Symptom2', 'Symptom3']]
y = df['Condition']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KNN model
def train_knn(X_train, y_train, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    return knn

# Function to predict condition for new patient
def predict_condition(knn_model, X_new):
    X_new_scaled = scaler.transform(X_new.reshape(1, -1))  # Reshape for single sample
    prediction = knn_model.predict(X_new_scaled)
    return prediction[0]

# Example usage
print("Enter symptoms for the new patient:")
symptom1 = int(input("Symptom 1 (0 or 1): "))
symptom2 = int(input("Symptom 2 (0 or 1): "))
symptom3 = int(input("Symptom 3 (0 or 1): "))
k_value = int(input("Enter the value of k (number of neighbors): "))

# Train KNN model with the entire dataset
knn_model = train_knn(X_scaled, y, k_value)

# Predict condition for the new patient
X_new = np.array([symptom1, symptom2, symptom3])
prediction = predict_condition(knn_model, X_new)

# Output the prediction
if prediction == 1:
    print("Prediction: The patient is likely to have the medical condition.")
else:
    print("Prediction: The patient is likely not to have the medical condition.")
