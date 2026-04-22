# Compare Two Algorithms + Wine

## Objective

Compare Logistic Regression and Decision Tree performance on the Wine dataset and save both models.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- model comparison
- evaluation metrics
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment trains two different classifiers on the Wine dataset, compares their accuracy and weighted F1 scores, and saves both models for later use.

## Implementation

1. Load the Wine dataset with load_wine().
2. Split into training and testing sets.
3. Train LogisticRegression and DecisionTreeClassifier.
4. Predict on the test set for both models.
5. Evaluate and compare accuracy and weighted F1 scores.
6. Save both trained models with joblib.dump().

## Commands

```bash
python experiment12.py
```

## Result

Two saved models and a direct comparison of their Wine classification performance.

## Learning Outcome

- How to compare different classifiers
- How to use weighted F1 for multi-class problems
- How to save multiple models

## Exam Tips

- Compare models on the same test set.
- Look at multiple metrics, not just accuracy.
- Save each model separately for future analysis.
