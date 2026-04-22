# MLP Classifier + Digits

## Objective

Train and evaluate an MLP neural network on the Digits dataset and save the trained model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- neural networks
- MLP
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment uses a multi-layer perceptron to classify handwritten digits, evaluates accuracy, and saves the trained model.

## Implementation

1. Load the Digits dataset with load_digits().
2. Split into training and testing sets.
3. Train MLPClassifier with max_iter=300.
4. Evaluate test accuracy and confusion matrix.
5. Save the trained model with joblib.dump().

## Commands

```bash
python experiment10.py
```

## Result

A saved neural network model for digit classification and evaluation output.

## Learning Outcome

- How to train an MLP classifier
- How to evaluate digit recognition models
- How to persist a neural network model

## Exam Tips

- MLPs may require tuning max_iter for convergence.
- Use confusion matrix to see digit-level performance.
- Save the model so it can be reused.
