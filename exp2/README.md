# Logistic Regression + Breast Cancer

## Objective

Train and evaluate a logistic regression classifier on the breast cancer dataset and save the final model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- logistic regression
- stratified splitting
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment builds a binary classification pipeline for breast cancer prediction. It trains a logistic regression model with stratified splitting and saves the trained classifier.

## Implementation

1. Load the breast cancer dataset with load_breast_cancer().
2. Split the data into train/test using stratify=y.
3. Scale the data with StandardScaler to improve convergence.
4. Train LogisticRegression with max_iter=1000.
5. Evaluate performance with accuracy, confusion matrix, precision, and recall.
6. Save the trained model to disk with joblib.dump().

## Commands

```bash
python experiment2.py
```

## Result

A trained and saved logistic regression classifier for breast cancer prediction and evaluation metrics.

## Learning Outcome

- How to preprocess data before classification
- Why scaling helps logistic regression
- How to save and reuse a trained model

## Exam Tips

- Use stratified split to preserve label distribution.
- Scale data before training logistic regression.
- Check model convergence warnings and increase max_iter if needed.
