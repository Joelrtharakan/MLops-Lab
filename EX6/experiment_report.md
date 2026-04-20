# Continuous Deployment (CD) of a Machine Learning Model using Docker and Flask

## 1. Title
Continuous Deployment (CD) of a Machine Learning Model using Docker and Flask

## 2. Objective
To learn how to deploy a trained ML model in a Docker container with a Flask API.

## 3. Job Role
MLOps Engineer and DevOps Engineer

## 4. Skills Required
- Basic Python
- Basic Flask web API knowledge
- Basic Docker knowledge
- Understanding of ML model files

## 5. Prerequisites
- Python installed
- Docker installed
- Basic command line skills
- Basic understanding of machine learning

## 6. Theory
- Continuous Deployment (CD) means sending code and models to production automatically.
- CD is important for ML because it makes model updates faster and safer.
- Docker packages code and dependencies into a container.
- Flask creates a small API that can serve model predictions.
- This combination makes the model easy to deploy.

## 7. Project Structure

ml-cd/
│
├── serve.py
├── Dockerfile
├── requirements.txt
└── iris.joblib

## 8. Implementation

### Step 1: Create the project folder
- Make a folder named `EX6`.
- Add the required files inside it.

### Step 2: Create `serve.py`
- Load the saved model with joblib.
- Create a Flask app.
- Add `/health` and `/predict` endpoints.
- Return JSON responses.

### Step 3: Create `requirements.txt`
- Add the package names:

```text
flask
scikit-learn
joblib
```

### Step 4: Create `Dockerfile`
- Use a Python base image.
- Copy the requirements and install them.
- Copy the code and model file.
- Start the Flask server.

### Step 5: Build the Docker image
- Run:

```bash
docker build -t ml-cd-app .
```

### Step 6: Run the Docker container
- Run:

```bash
docker run -p 5001:5001 ml-cd-app
```

## 9. Code Example

### serve.py
```python
from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load('iris.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return 'ML model server is running. Use /health or /predict.'

@app.route('/health')
def health():
    return 'ok'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

### Dockerfile
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY serve.py .
COPY iris.joblib .
CMD ["python", "serve.py"]
```

## 10. Commands Section

Install dependencies locally:
```bash
python3 -m pip install -r requirements.txt
```

Run locally:
```bash
python3 serve.py
```

Build Docker image:
```bash
docker build -t ml-cd-app .
```

Run Docker container:
```bash
docker run -p 5001:5001 ml-cd-app
```

## 11. Output
- Server runs at `http://127.0.0.1:5001`.
- `http://127.0.0.1:5001/health` returns `ok`.
- `http://127.0.0.1:5001/predict` returns predictions.

Example predict request:
```bash
curl -X POST http://127.0.0.1:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'
```

Expected response:
```json
{"prediction": 0}
```

## 12. Advantages
- Reproducible deployment
- Easy to run on any machine with Docker
- Simple API access to the model
- Good for production use

## 13. Exam Tips
- Remember the Dockerfile steps: FROM, WORKDIR, COPY, RUN, CMD.
- Know why the API has `/health` and `/predict`.
- Know the commands to build and run the container.

## 14. Conclusion
This lab shows how to deploy a machine learning model using Docker and Flask. It makes the model easy to run and share in a consistent environment.
