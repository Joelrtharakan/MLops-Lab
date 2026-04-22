# Random Forest + Wine

## Objective

Train and evaluate a random forest classifier on the Wine dataset and save the trained model.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- random forest
- ensemble learning
- model persistence

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment uses the Wine dataset to demonstrate an ensemble classification model. The random forest is trained, evaluated with accuracy and F1 score, and saved for reuse.

## Implementation

1. Load the Wine dataset with load_wine().
2. Split the data into training and test sets.
3. Train RandomForestClassifier with n_estimators=100.
4. Evaluate test accuracy and weighted F1 score.
5. Save the trained model with joblib.dump().

## Commands

```bash
python experiment4.py
```

## Result

A saved random forest model for wine classification and evaluation metrics.

## Learning Outcome

- Why ensemble methods improve stability
- How to use weighted F1 score
- How to persist trained models

## Exam Tips

- Random forests reduce overfitting compared to single trees.
- Check both accuracy and F1 for multi-class problems.
- Save models when training is expensive.
