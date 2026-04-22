# Saved Model Prediction System + Breast Cancer

## Objective

Train a breast cancer classifier, save it, reload it, and make a prediction with the loaded model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- joblib
- model persistence
- inference

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment shows how to save a trained model to disk and load it back later for prediction, demonstrating model persistence and reuse.

## Implementation

1. Load the breast cancer dataset with load_breast_cancer().
2. Split into training and testing sets.
3. Train a LogisticRegression model.
4. Save the trained model to disk.
5. Reload the model using joblib.load().
6. Make a prediction on a test sample with the loaded model.

## Commands

```bash
python experiment13.py
```

## Result

A saved logistic regression model that can be loaded and used for inference without retraining.

## Learning Outcome

- How to persist and reload scikit-learn models
- How to separate training from inference
- Why model persistence is useful in production workflows

## Exam Tips

- Keep model file names consistent.
- Load the saved model before making predictions.
- Use joblib for efficient scikit-learn serialization.
