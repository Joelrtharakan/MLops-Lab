# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
features = iris.feature_names

# Print features
print("Features used:")
for f in features:
    print("-", f)

# Split data (with random_state)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model (with random_state)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Baseline accuracy
acc = model.score(X_test, y_test)
print("\nBaseline Accuracy:", acc)

# Permutation Importance (with random_state)
result = permutation_importance(
    model, X_test, y_test, random_state=42
)

# Print importance
print("\nFeature Importance:")
for i in range(len(features)):
    print(features[i], "->", result.importances_mean[i])

# Plot
plt.barh(features, result.importances_mean)
plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Permutation Feature Importance")
plt.show()

# Most & least important
most = features[result.importances_mean.argmax()]
least = features[result.importances_mean.argmin()]

print("\nMost Important Feature:", most)
print("Least Important Feature:", least)