# Simple Flask App

## Objective

Expose a saved Iris model as a simple Flask web API with GET and POST prediction routes.

## Job Role

Data Scientist and ML Engineer

## Skills Required

- Python
- Flask
- scikit-learn
- API development
- model serving

## Prerequisites

- Python installed on your computer
- pip available to install packages
- Basic familiarity with running Python scripts

## Description

This experiment loads a saved Iris model and builds a lightweight Flask application to serve predictions through a /predict endpoint.

## Implementation

1. Load a saved model from iris_api_model.pkl with joblib.load().
2. Create a Flask app with a /predict route.
3. Accept default GET input or feature arrays via POST.
4. Predict the class label and return JSON output.
5. Run the Flask app locally.

## Commands

```bash
python experiment15.py
```

## Result

A running Flask application that serves machine learning predictions through an API endpoint.

## Learning Outcome

- How to build a simple Flask API
- How to serve model predictions over HTTP
- How to handle GET and POST requests for inference

## Exam Tips

- Verify the saved model file exists before starting the app.
- Use JSON POST requests for new input data.
- Test the endpoint with curl or a browser.
