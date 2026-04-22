# Flask Model Serving + Iris

## Objective

Serve a saved Iris model through a Flask API endpoint for real-time prediction.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- Flask
- scikit-learn
- model serving
- joblib

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment saves a trained Iris decision tree model and then loads it to demonstrate how a saved model can support API-based predictions.

## Implementation

1. Load the Iris dataset with load_iris().
2. Train a DecisionTreeClassifier on the full dataset.
3. Save the trained model to iris_api_model.pkl.
4. Reload the model from disk.
5. Make a test prediction using the loaded model.

## Commands

```bash
python experiment14.py
```

## Result

A saved Iris model that can be loaded for inference, demonstrating steps for API-ready model persistence.

## Learning Outcome

- How to save and reload a model for serving
- Why model persistence is important for APIs
- How to test saved model predictions

## Exam Tips

- Save the trained model before deployment.
- Reload the saved model to verify persistence.
- Use saved models to avoid retraining in production.
