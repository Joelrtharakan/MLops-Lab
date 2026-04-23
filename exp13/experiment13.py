from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump, load

# Load dataset
data = load_breast_cancer()
x, y = data.data, data.target

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(x_train, y_train)

# Save model
dump(model, "breast_cancer_model.pkl")

# Load model
loaded_model = load("breast_cancer_model.pkl")

# Predict using loaded model
print("Prediction:", loaded_model.predict([x_test[0]]))