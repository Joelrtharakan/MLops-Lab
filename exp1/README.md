# Linear Regression + Diabetes

## Objective

Train and evaluate a linear regression model on the diabetes dataset, then save the trained model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- linear regression
- model evaluation
- joblib model persistence

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment uses the diabetes regression dataset to demonstrate an end-to-end regression workflow. The model is trained, evaluated with MAE, MSE, and RMSE, and saved for reuse.

## Implementation

1. Load the diabetes dataset with load_diabetes().
2. Split the data into training and test sets with train_test_split.
3. Train a LinearRegression model on the training data.
4. Predict on the test set and calculate MAE, MSE, and RMSE.
5. Make a single-sample prediction using the trained model.
6. Save the trained model to disk with joblib.dump().

## Commands

```bash
python experiment1.py
```

## Result

A trained linear regression model, evaluation metrics for the diabetes dataset, and a saved model file for reuse.

## Learning Outcome

- How to build a regression model
- How to evaluate regression performance
- How to save a model for later use

## Exam Tips

- Always check model assumptions for regression.
- Use a test split for reliable evaluation.
- Save the model after training so you can reuse it later.
