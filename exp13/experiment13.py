from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump, load

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
dump(model, "breast_cancer_model.pkl")

# Load model
loaded_model = load("breast_cancer_model.pkl")

# Predict using loaded model
print("Prediction:", loaded_model.predict([X_test[0]]))