# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (species)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Function to predict species of new flower
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = clf.predict(X_new)
    return iris.target_names[prediction[0]]

# Example usage
print("Enter the measurements of the new flower:")
sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

# Predict species of the new flower
predicted_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)
print(f"Predicted Species: {predicted_species}")
