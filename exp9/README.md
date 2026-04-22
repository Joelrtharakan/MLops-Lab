# AdaBoost + Iris

## Objective

Train and evaluate an AdaBoost classifier on the Iris dataset and save the model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- AdaBoost
- ensemble methods
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment trains an AdaBoost ensemble on the Iris dataset, evaluates accuracy and weighted F1 score, and saves the trained model.

## Implementation

1. Load the Iris dataset with load_iris().
2. Split data into training and test sets.
3. Train AdaBoostClassifier with n_estimators=50.
4. Evaluate test accuracy and weighted F1 score.
5. Save the trained model with joblib.dump().

## Commands

```bash
python experiment9.py
```

## Result

A saved AdaBoost model for Iris classification and evaluation metrics.

## Learning Outcome

- How boosting improves weak learners
- How to evaluate multi-class models
- How to persist trained models

## Exam Tips

- AdaBoost builds a strong model from weak learners.
- Check weighted F1 for class-balanced evaluation.
- Save models after training.
