# Serving a Trained ML Model over HTTP using FastAPI

## 1. Title
Serving a Trained ML Model over HTTP using FastAPI

## 2. Objective
To learn how to serve a machine learning model with a simple web API.

## 3. Prerequisites
- Python installed
- Basic knowledge of Python scripts
- Basic understanding of machine learning models
- Ability to run commands in terminal

## 4. Theory
- Model serving means making a trained model available so other programs can use it.
- FastAPI is a simple Python library for building web APIs quickly.
- A `.pkl` file is a saved file that stores a trained model so we can load it later.

## 5. Project Structure

ml-api/
│
├── train_model.py
├── app.py
└── requirements.txt

## 6. Implementation

### Step 1: Create project folder
- Create a folder named `EX5`.

### Step 2: Create files
- Inside `EX5`, create `train_model.py`, `app.py`, and `requirements.txt`.

### Step 3: Install dependencies
- Install FastAPI, uvicorn, scikit-learn, and joblib.

### Step 4: Train and save model
- Use the iris dataset from sklearn.
- Train a simple model.
- Save the model to `model.pkl` using joblib.

### Step 5: Create FastAPI app
- Load the saved model.
- Create a FastAPI app.
- Add one endpoint at `/predict`.
- Accept feature values and return the prediction.

### Step 6: Run server
- Start the server with uvicorn.
- Open the browser to use the API.

## Code

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

## 7. Commands Section

Install dependencies:
```bash
pip install fastapi uvicorn scikit-learn joblib python-multipart
```

Train model:
```bash
python train_model.py
```

Run server:
```bash
uvicorn app:app --reload
```

## 8. Output
- Model trained and saved as `model.pkl`.
- Server runs at `http://127.0.0.1:8000`.
- API docs available at `http://127.0.0.1:8000/docs`.

## 9. Example API Usage
- Input values:
  - sepal_length: 5.1
  - sepal_width: 3.5
  - petal_length: 1.4
  - petal_width: 0.2
- Output prediction:
  - `{'prediction': 0}`

## 10. Advantages
- Easy deployment
- Real-time prediction
- Lightweight API

## 11. Conclusion
This lab shows how to serve a trained ML model with FastAPI. It makes the model available over HTTP so other programs can use it.
