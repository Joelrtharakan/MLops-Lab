from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from joblib import dump, load

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
dump(model, "iris_api_model.pkl")

# Load model
loaded_model = load("iris_api_model.pkl")

# Test prediction
print("Prediction:", loaded_model.predict([X[0]]))