# End-to-End Project + Any Inbuilt Dataset

## Objective

Complete a full machine learning workflow from training to saving a model on an inbuilt dataset.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- end-to-end ML workflow
- model persistence
- evaluation

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment demonstrates a full machine learning project cycle using a built-in dataset, training a model, evaluating it, making a sample prediction, and saving the final model.

## Implementation

1. Load an inbuilt dataset with load_iris().
2. Split into training and testing sets.
3. Train a RandomForestClassifier.
4. Evaluate the model on the test set.
5. Make a single-sample prediction.
6. Save the trained model using joblib.dump().

## Commands

```bash
python experiment16.py
```

## Result

A complete saved ML model ready for reuse and a demonstration of a full training-to-deployment workflow.

## Learning Outcome

- How to execute an end-to-end ML project
- How to evaluate and save a model
- How to make predictions with a trained model

## Exam Tips

- Treat each experiment as a full project pipeline.
- Save your final model after training and validation.
- Test model predictions on sample inputs.
