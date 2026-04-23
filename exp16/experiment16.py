from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# Load dataset
data = load_iris()
x, y = data.data, data.target

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict on test data
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict on new input
print("Prediction:", model.predict([x_test[0]]))

# Save model
dump(model, "end_to_end_model.pkl")