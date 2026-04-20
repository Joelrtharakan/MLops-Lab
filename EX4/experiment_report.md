# Permutation Feature Importance (PFI)

## 1. Title
Permutation Feature Importance (PFI)

## 2. Objective
To learn how to measure which features are most important for a model using Permutation Feature Importance.

## 3. Job Role
Data Scientist and Machine Learning Engineer

## 4. Skills Required
- Basic Python knowledge
- Basic machine learning understanding
- Ability to use scikit-learn
- Ability to read simple charts and output

## 5. Prerequisites
- Python installed
- scikit-learn installed
- Basic knowledge of datasets and models

## 6. Theory
- Model explainability means understanding why a model makes decisions.
- Permutation Feature Importance (PFI) measures how much each feature affects model accuracy.
- If a feature is important, shuffling it will hurt accuracy.
- If a feature is not important, shuffling it will not change accuracy much.

## 7. Dataset Explanation
We use the Iris dataset from scikit-learn.

Features:
- sepal length
- sepal width
- petal length
- petal width

## 8. Implementation

### Step 1: Import libraries
- Import the Iris dataset, RandomForestClassifier, permutation_importance, and train_test_split.
- Import matplotlib for plotting.

### Step 2: Load dataset
- Load the Iris data.
- Store feature values in `X` and labels in `y`.

### Step 3: Split dataset
- Split the data into training and test sets.
- Use `test_size=0.3`.

### Step 4: Train the model
- Create a Random Forest classifier.
- Train the model on the training data.

### Step 5: Calculate baseline accuracy
- Measure accuracy on the test set before shuffling features.

### Step 6: Apply Permutation Feature Importance
- Shuffle one feature at a time in the test set.
- Measure how much the accuracy changes.
- Larger drops mean more important features.

### Step 7: Display results
- Print feature importance values.
- Show which feature is most important.
- Plot a simple bar chart.

## 9. Implementation Code

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train a random forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Calculate baseline accuracy
baseline_accuracy = model.score(X_test, y_test)
print(f"Baseline Accuracy: {baseline_accuracy:.3f}")

# Apply Permutation Feature Importance
pfi_result = permutation_importance(
    model, X_test, y_test, n_repeats=10, random_state=42
)

# Sort features by importance
feature_importance = sorted(
    zip(feature_names, pfi_result.importances_mean),
    key=lambda x: x[1],
    reverse=True,
)

print("Permutation Feature Importance Results:")
for name, importance in feature_importance:
    print(f"{name} -> {importance:.3f}")

# Plot the importance values
names = [name for name, _ in feature_importance]
values = [importance for _, importance in feature_importance]
plt.figure(figsize=(8, 4))
plt.barh(names, values, color='skyblue')
plt.gca().invert_yaxis()
plt.title('Permutation Feature Importance (Random Forest - Iris)')
plt.xlabel('Mean Decrease in Accuracy')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()

print(f"Most Important Feature: {feature_importance[0][0]}")
print(f"Least Important Feature: {feature_importance[-1][0]}")
```

## 10. Commands Section

Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

Run the script:
```bash
python3 ex4_pfi.py
```

## 11. Output
- A baseline accuracy value is printed.
- A list of feature importance values is printed.
- A bar chart of feature importance appears.
- The most important and least important feature are shown.

## 12. Result Analysis
- Petal length and petal width are usually the most important features.
- Sepal length and sepal width are less important.
- The larger the importance number, the more the feature matters.

## 13. Exam Notes
- Know what Permutation Feature Importance means.
- Know how shuffling a feature tests its importance.
- Know why baseline accuracy is needed.

## 14. Conclusion
This lab shows how to use Permutation Feature Importance to explain a model. It makes the most important features easy to find.
