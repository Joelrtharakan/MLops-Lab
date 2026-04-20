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
