# Gradient Boosting + Breast Cancer

## Objective

Train and evaluate a gradient boosting classifier on the breast cancer dataset and save the trained model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- gradient boosting
- ensemble learning
- model saving

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment uses gradient boosting on the breast cancer dataset, evaluates test accuracy, and persists the model.

## Implementation

1. Load the breast cancer dataset with load_breast_cancer().
2. Split into training and testing sets.
3. Train GradientBoostingClassifier on the training data.
4. Evaluate accuracy and confusion matrix.
5. Save the model using joblib.dump().

## Commands

```bash
python experiment8.py
```

## Result

A trained gradient boosting model saved to disk and evaluation metrics for breast cancer classification.

## Learning Outcome

- How gradient boosting works
- How to evaluate binary classification
- How to save scikit-learn models

## Exam Tips

- Gradient boosting is powerful for structured data.
- Check performance using accuracy and confusion matrix.
- Save trained models after training.
