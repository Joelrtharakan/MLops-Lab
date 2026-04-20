# Serving a Trained ML Model over HTTP using FastAPI

## 1. Title
Serving a Trained ML Model over HTTP using FastAPI

## 2. Objective
To learn how to serve a machine learning model with a simple web API.

## 3. Prerequisites
- Python installed
- Basic knowledge of Python scripts
- Basic understanding of machine learning models
- Ability to run terminal commands

## 4. Theory
- Model serving means making a trained model available so other programs can use it.
- FastAPI is a Python library for building web APIs quickly.
- A `.pkl` file stores a trained model so it can be loaded later.
- The web API receives input, loads the model, and returns predictions.

## 5. Project Structure

ml-api/
│
├── train_model.py
├── app.py
└── requirements.txt

## 6. Implementation

### Step 1: Create the project folder
- Make a folder named `EX5`.
- Inside it, create `train_model.py`, `app.py`, and `requirements.txt`.

### Step 2: Install dependencies
- Install the required packages using pip.

### Step 3: Train and save the model
- Use the Iris dataset from scikit-learn.
- Train a `RandomForestClassifier`.
- Save the model to `model.pkl` with joblib.

### Step 4: Create the FastAPI app
- Load the saved model in `app.py`.
- Create a FastAPI application.
- Add a `/predict` endpoint that accepts feature values.
- Return the prediction as JSON.

### Step 5: Run the server
- Start the FastAPI server with uvicorn.
- Open the browser or use an API client to send requests.

## 7. Code Example

### train_model.py
```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("Model trained and saved!")
```

### app.py
```python
from fastapi import FastAPI
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Model is running!"}

@app.post("/predict")
def predict(features: list):
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
```

### requirements.txt
```text
fastapi
uvicorn
scikit-learn
joblib
numpy
```

## 8. Commands Section

Install dependencies:
```bash
pip install -r requirements.txt
```

Train the model:
```bash
python train_model.py
```

Run the server:
```bash
uvicorn app:app --reload
```

## 9. Output
- `train_model.py` prints `Model trained and saved!`.
- The FastAPI server runs at `http://127.0.0.1:8000`.
- API docs are available at `http://127.0.0.1:8000/docs`.

## 10. Example API Usage
Send a POST request to `/predict` with JSON body:
```json
{"features": [5.1, 3.5, 1.4, 0.2]}
```
Expected response:
```json
{"prediction": 0}
```

## 11. Advantages
- Easy deployment for real-time prediction.
- The model can be used by other programs.
- FastAPI is simple and fast.

## 12. Exam Tips
- Know how the model is loaded from `model.pkl`.
- Know that `/predict` returns JSON.
- Remember to install requirements before running the app.

## 13. Conclusion
This lab shows how to serve a machine learning model with FastAPI. It makes predictions available over HTTP so other programs can use the model.
