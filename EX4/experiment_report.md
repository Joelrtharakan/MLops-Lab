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
- Ability to read simple code and results

## 5. Prerequisites
- Python installed
- scikit-learn installed
- Basic knowledge of datasets and models

## 6. Theory
- Model explainability means understanding why a model makes decisions.
- Permutation Feature Importance (PFI) measures how much each feature affects the model’s prediction accuracy.
- Simple example: if a feature is very important, mixing its values will make the model worse.
- If a feature is not important, mixing its values will not change the model much.

## 7. Dataset Explanation
We use the Iris dataset from sklearn.

Features:
- sepal length
- sepal width
- petal length
- petal width

## 8. Implementation

### Step 1: Import libraries
- Import the iris dataset from sklearn.
- Import RandomForestClassifier, train_test_split, permutation_importance, and matplotlib.

### Step 2: Load dataset
- Use `load_iris()`.
- Save the data as `X` and labels as `y`.

### Step 3: Split dataset
- Split the data into training and testing sets.
- Use `test_size=0.3` for a simple split.

### Step 4: Train simple model (Random Forest)
- Create a Random Forest classifier.
- Train it with the training data.

### Step 5: Calculate baseline accuracy
- Measure model accuracy on the test data before permutation.

### Step 6: Apply Permutation Feature Importance
- Shuffle values for one feature at a time.
- Measure how much accuracy drops.

### Step 7: Display feature importance
- Print feature names and importance values.
- Sort from most important to least important.
- Print the most and least important feature.
- Show a simple bar chart.

## Implementation Code

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

# Show the feature names and a small preview of the dataset
print("Features used for Permutation Feature Importance:")
for name in feature_names:
    print("-", name)

print("\nDataset preview:")
for i in range(5):
    row = X[i]
    print(" ".join(f"{x:.1f}" for x in row))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create and train a simple Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Calculate baseline accuracy
baseline_accuracy = model.score(X_test, y_test)
print(f"\nBaseline Accuracy: {baseline_accuracy:.3f}")

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

print("\nPermutation Feature Importance Results:")
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

most_important = feature_importance[0][0]
least_important = feature_importance[-1][0]
print(f"\nMost Important Feature: {most_important}")
print(f"Least Important Feature: {least_important}")

print("\nSummary:")
print(f"- The most important feature is {most_important}.")
print(f"- The least important feature is {least_important}.")
```

## 9. Output
Example output:

Baseline accuracy: 1.000

Permutation Feature Importance Results:
petal width -> 0.176
petal length -> 0.144
sepal length -> 0.000
sepal width -> 0.000

A simple bar chart of feature importance is shown.

## 10. Explanation of Results
- The most important features are petal length and petal width.
- These features have the biggest effect on model accuracy.
- Sepal length is medium important.
- Sepal width is the least important.

## 11. Answer the Questions Clearly

Q1: Identify features
- sepal length
- sepal width
- petal length
- petal width

Q2: Explain PFI working
- Train a model and get baseline accuracy.
- For each feature, shuffle its values.
- Measure how much the model accuracy drops.
- The larger the drop, the more important the feature.
- If accuracy does not change, the feature is not important.

Q3: Demonstrate the process
- Train a Random Forest classifier on the Iris dataset.
- Use `permutation_importance` from sklearn.
- Print baseline accuracy and importance values.
- Example code is shown above.

Q4: Analyze results
- Petal length and petal width have the most significant impact.
- Sepal length has moderate impact.
- Sepal width has the smallest impact.

Q5: Evaluate effectiveness
- PFI is effective for the Iris dataset because it shows direct feature impact.
- It works well here because the dataset is small and balanced.
- It can be slower than other methods because it repeats model scoring.
- It can be misleading if features are correlated.
- Compared to other techniques:
  - Permutation Importance: model-agnostic, interpretable, slower, affected by correlated features.
  - Mean Decrease in Impurity: fast but biased to some feature types.
  - SHAP Values: detailed but very computationally heavy.

## 12. Advantages and Limitations

Benefits:
- Model-agnostic
- Easy to understand
- Shows real impact on accuracy
- Helps detect redundant or irrelevant features

Limitations:
- Slow for large datasets
- Affected by correlated features
- Sensitive to random shuffling and the chosen metric

## 13. Conclusion
For the Iris dataset, Permutation Feature Importance is effective and clearly shows that petal length and petal width are key features.

python3 -m venv venv 
source venv/bin/activate
python3 -m pip install -r requirements.txt
cd "/Users/joeltharakan/Downloads/MLOPS LAB/EX4"
python3 ex4_pfi.py