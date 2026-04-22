# Complete ML Pipeline + Iris

## Objective

Build a complete preprocessing and modeling pipeline for Iris classification and save the pipeline.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- scikit-learn
- pipelines
- scaling
- logistic regression
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment demonstrates an end-to-end ML pipeline with preprocessing and modeling in one object, then saves the pipeline for inference.

## Implementation

1. Load the Iris dataset with load_iris().
2. Split into training and testing sets.
3. Build a pipeline with StandardScaler and LogisticRegression.
4. Train the pipeline on the training data.
5. Predict test labels and evaluate accuracy.
6. Save the pipeline using joblib.dump().

## Commands

```bash
python experiment11.py
```

## Result

A saved ML pipeline for Iris classification and the ability to reuse preprocessing and model steps together.

## Learning Outcome

- How to use scikit-learn pipelines
- Why scaling belongs inside a pipeline
- How to save a pipeline for inference

## Exam Tips

- Pipelines keep preprocessing and modeling consistent.
- Always save the full pipeline, not just the model.
- Use pipelines to reduce inference-time errors.
