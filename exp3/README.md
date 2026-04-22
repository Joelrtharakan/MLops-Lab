# Decision Tree + Iris

## Objective

Train and evaluate a decision tree classifier on the Iris dataset and save the trained model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- decision trees
- classification metrics
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment trains a decision tree on the Iris dataset, evaluates test accuracy and classification metrics, and persists the model for future use.

## Implementation

1. Load the Iris dataset with load_iris().
2. Split the data into training and testing sets.
3. Train DecisionTreeClassifier on the training data.
4. Predict on the test set and evaluate accuracy and classification report.
5. Save the trained model using joblib.dump().

## Commands

```bash
python experiment3.py
```

## Result

A trained decision tree model for Iris classification, evaluation output, and a saved model file.

## Learning Outcome

- How decision trees work for classification
- How to evaluate class-level metrics
- How to save a scikit-learn model

## Exam Tips

- Use classification_report to understand per-class behavior.
- Decision trees are easy to interpret but can overfit.
- Save trained models to avoid retraining.
