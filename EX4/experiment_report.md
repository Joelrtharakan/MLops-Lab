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
- The feature names are printed.
- The baseline accuracy value is printed.
- Feature importance values are printed in the original feature order.
- A horizontal bar chart of feature importance appears.
- The most important and least important feature are shown.

## 12. Result Analysis
- The code shows which features change model accuracy most when shuffled.
- Petal length and petal width are often the most important features.
- Sepal length and sepal width are usually less important.
- The feature with the highest importance mean is the most important.
- The feature with the lowest importance mean is the least important.

## 13. Exam Notes
- Know what Permutation Feature Importance means.
- Know how the code prints feature names and importance values.
- Know why baseline accuracy is needed.
- Remember the script uses `result.importances_mean` and `argmax` / `argmin`.

## 14. Conclusion
This lab shows how to use Permutation Feature Importance to explain a model. It makes the most important features easy to find.
