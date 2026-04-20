# Containerize ML Model for Deployment

## 1. Title
Containerize ML Model for Deployment

## 2. Objective
To learn how to package a simple ML model inside a Docker container.

## 3. Job Role
DevOps Engineer and Machine Learning Engineer

## 4. Skills Required
- Basic Python knowledge
- Basic understanding of machine learning
- Basic understanding of Docker containers
- Ability to create files and run terminal commands

## 5. Prerequisites
- Docker Desktop installed
- Python installed
- A text editor or VS Code
- Basic command line skills

## 6. Theory
- A container is a small package that holds code and its needed tools.
- Docker is a tool that makes and runs containers.
- Containerization is useful for ML models because the model can run the same way on many computers.
- The Dockerfile describes how to build the container.

## 7. Project Structure

ml-container/
│
├── Dockerfile
├── ML.py
└── requirements.txt

## 8. Implementation

### Step 1: Create the project folder
- Make a folder named `EX3`.
- Inside `EX3`, create the required files.

### Step 2: Create `ML.py`
- Write a simple Python script that trains a model and prints accuracy.
- Use the Iris dataset and `LogisticRegression`.

### Step 3: Create `requirements.txt`
- Add the dependency:

```text
scikit-learn
```

### Step 4: Create `Dockerfile`
- Use a small Python base image.
- Copy the code and requirements into the container.
- Install dependencies.
- Run the model script when the container starts.

### Step 5: Build the Docker image
- In the terminal, go to the `EX3` folder.
- Run:

```bash
docker build -t ml-model-container .
```

### Step 6: Run the Docker container
- Run:

```bash
docker run --rm ml-model-container
```

## 9. Code Example

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model accuracy:", accuracy)
```

## 10. Dockerfile Explanation
- `FROM python:3.10-slim`: Use a small Python image.
- `WORKDIR /app`: Set the working directory inside the container.
- `COPY requirements.txt .`: Copy the dependency file into the container.
- `COPY ML.py .`: Copy the Python script into the container.
- `RUN pip install --no-cache-dir -r requirements.txt`: Install packages.
- `CMD ["python", "ML.py"]`: Run the script when the container starts.

## 11. Commands Section

Install dependencies locally (optional):
```bash
python3 -m pip install -r requirements.txt
```

Build the Docker image:
```bash
docker build -t ml-model-container .
```

Run the Docker container:
```bash
docker run --rm ml-model-container
```

## 12. Output
- The program prints the model accuracy.
- The container starts, runs the code, and stops.
- You should see one accuracy line in the terminal.

## 13. Advantages
- The model runs the same way on any machine with Docker.
- It keeps code and dependencies together.
- It is easy to share and deploy.

## 14. Exam Tips
- Remember the Dockerfile steps: FROM, WORKDIR, COPY, RUN, CMD.
- Know why containers are useful for ML.
- Know the build command and run command.

## 15. Conclusion
This lab shows how to package a machine learning script in a Docker container. It makes the model easy to share and run consistently.
