from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  # Example model

# Example dataset with features and target variable
# Replace this with your actual dataset or data loading mechanism
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6],
    'Feature3': [3, 4, 5, 6, 7],
    'Target': [0, 1, 0, 0, 1]  # Example target variable (0 or 1)
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 1: Prepare the data
features = df[['Feature1', 'Feature2', 'Feature3']]  # Features
target = df['Target']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 2: Build and train a machine learning model (example with Logistic Regression)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Step 3: Accept user input for evaluation features and target variable
print("\nEnter names of the features and target variable for evaluation:")
feature_names = input("Enter feature names separated by comma (e.g., Feature1, Feature2, Feature3): ").strip().split(',')
target_name = input("Enter target variable name (e.g., Target): ").strip()

# Step 4: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 5: Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Step 6: Output evaluation metrics
print("\nEvaluation Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
