import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Show the feature names and a small preview of the dataset
print("Features used for Permutation Feature Importance:")
for feature in X.columns:
    print("-", feature)

print("\nDataset preview:")
print(X.head().to_string(index=False))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train a simple Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Calculate baseline accuracy
baseline_accuracy = model.score(X_test, y_test)
print(f"\nBaseline Accuracy: {baseline_accuracy:.3f}")

# Apply Permutation Feature Importance
pfi_result = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)

importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Mean Importance': pfi_result.importances_mean,
    'Std Deviation': pfi_result.importances_std
}).sort_values(by='Mean Importance', ascending=False)

print("\nPermutation Feature Importance Results:")
print(importance_df.to_string(index=False))

# Plot the importance values
plt.figure(figsize=(8, 4))
plt.barh(importance_df['Feature'], importance_df['Mean Importance'], color='skyblue')
plt.gca().invert_yaxis()
plt.title('Permutation Feature Importance (Random Forest - Iris Dataset)')
plt.xlabel('Mean Decrease in Accuracy')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()

most_important = importance_df.iloc[0]['Feature']
least_important = importance_df.iloc[-1]['Feature']
print(f"\nMost Important Feature: {most_important}")
print(f"Least Important Feature: {least_important}")

print("\nSummary:")
print(f"- The most important feature is {most_important}.")
print(f"- The least important feature is {least_important}.")
