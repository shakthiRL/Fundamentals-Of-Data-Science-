import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Step 1: Generate synthetic dataset
np.random.seed(42)

# Generating synthetic data
n_patients = 1000
age = np.random.randint(18, 80, n_patients)
gender = np.random.choice(['Male', 'Female'], size=n_patients)
blood_pressure = np.random.randint(90, 180, n_patients)
cholesterol = np.random.randint(120, 300, n_patients)
response = np.random.choice(['Good', 'Bad'], size=n_patients)

# Create DataFrame
data = {
    'Age': age,
    'Gender': gender,
    'BloodPressure': blood_pressure,
    'Cholesterol': cholesterol,
    'Outcome': response
}
df = pd.DataFrame(data)

# Display sample of the synthetic dataset
print(df.head())

# Step 2: Data preprocessing
# Convert categorical variables to numerical using one-hot encoding
df_processed = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# Map 'Good' to 1 and 'Bad' to 0 for the target variable
df_processed['Outcome'] = df_processed['Outcome'].map({'Good': 1, 'Bad': 0})

# Split data into features (X) and target variable (y)
X = df_processed.drop('Outcome', axis=1)
y = df_processed['Outcome']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by scaling them
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 3: Build the KNN model
k = 5  # Example value of k, you can choose based on model evaluation
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# Step 4: Model evaluation
y_pred = knn.predict(X_test_scaled)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Display evaluation metrics
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1-score: {f1:.4f}')

# Classification report (includes precision, recall, F1-score for both classes)
print(classification_report(y_test, y_pred))

# Step 5: Make predictions on new data (test set) and display results
predictions_df = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})
print(predictions_df.head(10))
