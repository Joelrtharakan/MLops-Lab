# Naive Bayes + Wine

## Objective

Train and evaluate a Gaussian Naive Bayes classifier on the Wine dataset and save the model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- Naive Bayes
- classification
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment trains a Gaussian Naive Bayes classifier on the Wine dataset, evaluates accuracy and classification metrics, and saves the model.

## Implementation

1. Load the Wine dataset with load_wine().
2. Split the data into training and test sets.
3. Train GaussianNB on the training data.
4. Evaluate accuracy and classification report.
5. Save the trained model using joblib.dump().

## Commands

```bash
python experiment7.py
```

## Result

A saved Naive Bayes model for Wine classification and its evaluation output.

## Learning Outcome

- How Gaussian Naive Bayes works
- How to evaluate a multi-class classifier
- How to save models for reuse

## Exam Tips

- Naive Bayes assumes feature independence.
- Use classification_report for detailed metrics.
- Persist models to avoid retraining.
