# KNN + Iris

## Objective

Train and evaluate a K-Nearest Neighbors classifier on the Iris dataset and save the model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- KNN
- classification
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment uses KNN to classify Iris flowers, evaluates accuracy, makes a sample prediction, and saves the classifier.

## Implementation

1. Load the Iris dataset with load_iris().
2. Split the data into training and test sets.
3. Train KNeighborsClassifier with n_neighbors=5.
4. Predict and print test accuracy.
5. Make a single-sample prediction and save the model using joblib.dump().

## Commands

```bash
python experiment5.py
```

## Result

A trained KNN classifier for Iris and a saved model file ready for reuse.

## Learning Outcome

- How KNN works for classification
- How to evaluate KNN accuracy
- How to persist a trained model

## Exam Tips

- KNN is simple but can be slow on large datasets.
- Use a test split to verify performance.
- Save the model for inference without retraining.
