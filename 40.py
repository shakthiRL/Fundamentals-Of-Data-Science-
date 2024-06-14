import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Load the dataset (replace with your actual dataset)
# Example dataset with patient features and labels
data = {
    'Symptom1': [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    'Symptom2': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'Symptom3': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    'Condition': [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]  # 1 for condition, 0 for no condition
}
df = pd.DataFrame(data)

# Display the dataset to understand its structure
print("Dataset:")
print(df)

# Step 2: Build a KNN classifier
X = df[['Symptom1', 'Symptom2', 'Symptom3']]  # Features
y = df['Condition']  # Target variable

# Accept user input for a new patient
print("\nEnter details for the new patient:")
symptom1 = int(input("Symptom 1 (0 or 1): "))
symptom2 = int(input("Symptom 2 (0 or 1): "))
symptom3 = int(input("Symptom 3 (0 or 1): "))
k = int(input("Enter the value of k (number of neighbors): "))

# Create a new patient input
new_patient = pd.DataFrame({
    'Symptom1': [symptom1],
    'Symptom2': [symptom2],
    'Symptom3': [symptom3]
})

# Create a KNN classifier with the chosen k value
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# Predict the condition for the new patient
predicted_condition = knn.predict(new_patient)

# Output the predicted condition
if predicted_condition[0] == 1:
    print("\nThe patient is predicted to have the medical condition.")
else:
    print("\nThe patient is predicted to not have the medical condition.")
