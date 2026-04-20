# Continuous Deployment (CD) of a Machine Learning Model using Docker and Flask

## 1. Title
Continuous Deployment (CD) of a Machine Learning Model using Docker and Flask

## 2. Objective
To learn how to deploy a trained ML model in a Docker container with a Flask API.

## 3. Job Role
MLOps Engineer and DevOps Engineer

## 4. Skills Required
- Basic Python
- Basic Flask web API
- Basic Docker knowledge
- Understanding of ML model files

## 5. Prerequisites
- Python installed
- Docker installed
- Basic command line skills
- Basic understanding of machine learning

## 6. Theory
- Continuous Deployment (CD) means automatically sending code and models to production.
- CD is important for ML because it makes model updates easy and fast.
- Docker is a tool that puts code and files into a small package called a container.
- Model serving means running a model inside a web API so other programs can ask it for predictions.

## 7. Workflow Explanation
- Prepare: save the model and give it a version name.
- Build: create a Docker image with the app and the model.
- Test & validate: check that the container works and the API responds.
- Publish: upload the Docker image to a registry (optional concept).
- Deploy: run the container so the app is live.
- Monitor & rollback: watch the app and restart an older version if needed.

## 8. Project Structure

ml-cd/
│
├── serve.py
├── Dockerfile
├── requirements.txt
└── iris.joblib (model file)

## 9. Implementation

### Step 1: Create folder
- Create a folder named `EX6`.

### Step 2: Create files
- Create `serve.py`, `Dockerfile`, `requirements.txt`, and `iris.joblib`.

### Step 3: Train model (optional)
- Train a simple model with the iris dataset.
- Save the model to `iris.joblib`.

### Step 4: Create Flask API
- Use Flask to make a small web app.
- Add `/health` and `/predict` endpoints.
- Load the saved model with joblib.

### Step 5: Create requirements.txt
- Add Flask, scikit-learn, and joblib.

### Step 6: Create Dockerfile
- Use `python:3.10-slim`.
- Copy requirements and install them.
- Copy the app and the model file.
- Run the Flask server.

### Step 7: Build Docker image
- Use `docker build -t ml-cd-app .`

### Step 8: Run container
- Use `docker run -p 5000:5000 ml-cd-app`

## Code

### serve.py
```python
from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load('iris.joblib')

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return 'ML model server is running. Use /health or /predict.'

# Health endpoint
@app.route('/health')
def health():
    return 'ok'

# Predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

### requirements.txt
```text
flask
scikit-learn
joblib
```

### Dockerfile
```dockerfile
# Use a small Python image
FROM python:3.10-slim

# Set work directory inside the container
WORKDIR /app

# Copy dependency file and install packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY serve.py .
COPY iris.joblib .

# Run the Flask server
CMD ["python", "serve.py"]
```

## 10. Commands Section

Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```
- This installs Flask, scikit-learn, and joblib.

Run locally:
```bash
python3 serve.py
```
- This starts the Flask model server on port 5000.

Build image:
```bash
docker build -t ml-cd-app .
```
- This builds the Docker image and gives it the name `ml-cd-app`.

Run container:
```bash
docker run -p 5001:5001 ml-cd-app
```
- This runs the container and connects port 5000 inside the container to port 5000 on your machine.

## 11. Output
- Server runs at `http://localhost:5001`.
- `/health` returns `ok`.
- `/predict` returns the model prediction.

### Test predict
Use this command after the server is running:
```bash
curl -X POST http://127.0.0.1:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'
```

## 12. Answer Questions Clearly

- Prepare: save and version the model file.
- Build: Docker creates a portable image.
- Test & Gate: check the container and API before release.
- Publish: push the image to a registry so others can use it.
- Deploy: run the container in the target environment.
- Monitor & Rollback: watch the app and restart an earlier image if needed.

## 13. Advantages
- Reproducibility
- Easy deployment
- Scalability
- Consistency

## 14. Conclusion
This lab shows how to deploy a machine learning model with Docker and Flask. It makes deployment simple, automated, and reliable.
