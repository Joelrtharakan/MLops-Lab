from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump

# Load dataset (same style)
data = load_iris()
x, y = data.data, data.target

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create pipeline (scaling + model)
model = make_pipeline(StandardScaler(), LogisticRegression())

# Train model
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))

# New sample prediction
print("New Prediction:", model.predict([x_test[0]]))

# Save model
dump(model, "pipeline_iris.pkl")