# SVM + Breast Cancer

## Objective

Train and evaluate an SVM classifier on the breast cancer dataset and save the trained model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- SVM
- binary classification
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment trains an SVM model for breast cancer classification, evaluates key metrics, and saves the model to disk.

## Implementation

1. Load the breast cancer dataset with load_breast_cancer().
2. Split the data into training and testing sets.
3. Train SVC on the training data.
4. Evaluate accuracy, precision, recall, and F1 score.
5. Save the trained SVM model with joblib.dump().

## Commands

```bash
python experiment6.py
```

## Result

A saved SVM classifier for breast cancer with evaluation metrics.

## Learning Outcome

- How SVM works for binary classification
- How to interpret precision and recall
- How to persist a machine learning model

## Exam Tips

- SVM can be sensitive to feature scaling.
- Use test data to validate model performance.
- Save the trained model for future inference.
