# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression  # Replace with your model

# Sample dataset (replace with your actual dataset loading)
# Assuming you have a dataset CSV file 'data.csv'
# df = pd.read_csv('data.csv')

# Sample dataset (replace with your actual dataset loading)
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [10, 20, 30, 40, 50],
    'Target': [0, 1, 0, 1, 0]  # Binary classification target (0 or 1)
}
df = pd.DataFrame(data)

# Assuming X contains features and y contains target
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train your model (replace with your model training)
model = LogisticRegression()  # Example with Logistic Regression
model.fit(X_train, y_train)

# Function to evaluate model performance
def evaluate_model_performance(model, X_test, y_test):
    # Make predictions on test data
    y_pred = model.predict(X_test)
    
    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Display the evaluation metrics
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")

# Example usage
print("Enter the names of the features and the target variable:")
feature_names = input("Features (comma-separated): ").strip().split(',')
target_name = input("Target variable: ")

# Select columns from the dataset based on user input
X_eval = df[feature_names]
y_eval = df[target_name]

# Evaluate model performance on evaluation set
evaluate_model_performance(model, X_eval, y_eval)
