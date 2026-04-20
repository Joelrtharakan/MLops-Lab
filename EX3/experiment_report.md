# Containerize ML Model for Deployment

## 1. Title
Containerize ML Model for Deployment

## 2. Objective
To learn how to put a simple ML model inside a Docker container.

## 3. Job Role
DevOps Engineer and Machine Learning Engineer

## 4. Skills Required
- Basic Python knowledge
- Basic understanding of machine learning
- Basic understanding of Docker containers
- Ability to create files and run commands

## 5. Prerequisites
- Docker Desktop installed
- Python installed
- VS Code or a text editor
- Basic knowledge of command line

## 6. Theory
- A container is a small package that holds code and its needed tools.
- Docker is a tool that makes and runs containers.
- Containerization is useful for ML models because the model can run the same way on many computers.

## 7. Project Structure

ml-container/
│
├── Dockerfile
├── ML.py
└── requirements.txt

## 8. Implementation

### Step 1: Install Docker Desktop
- Download Docker Desktop from the Docker website.
- Install it on your computer.
- Start Docker Desktop.

### Step 2: Open VS Code and create project folder
- Open VS Code.
- Create a folder named `EX3`.
- Inside `EX3`, you will make the files.

### Step 3: Create ML.py file
- Create a file named `ML.py`.
- Put this code:

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a simple logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and print accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model accuracy:", accuracy)
```

### Step 4: Create requirements.txt
- Create a file named `requirements.txt`.
- Put this text:

```text
scikit-learn
```

### Step 5: Create Dockerfile
- Create a file named `Dockerfile`.
- Put this code:

```dockerfile
# Use a small Python image
FROM python:3.10-slim

# Set the working folder inside the container
WORKDIR /app

# Copy files from our computer into the container
COPY requirements.txt .
COPY ML.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python file when the container starts
CMD ["python", "ML.py"]
```

### Step 6: Build Docker image
- In the terminal, run this command:

```bash
cd "/Users/joeltharakan/Downloads/MLOPS LAB/EX3"
docker build -t ml-model-container .
```

### Step 7: Run Docker container
- In the terminal, run this command:

```bash
docker run --rm ml-model-container
```

## 9. Explain Dockerfile Line-by-Line
- `FROM`: Chooses the base Python image.
- `WORKDIR`: Sets the folder inside the container.
- `COPY`: Copies files from the project into the container.
- `RUN`: Runs a command inside the container to install packages.
- `CMD`: Says which command to run when the container starts.

## 10. Commands Section

```bash
docker build -t ml-model-container .
```
- Builds the Docker image and gives it the name `ml-model-container`.

```bash
docker run --rm ml-model-container
```
- Runs the container and removes it after it stops.

## 11. Output / Result
- The model runs successfully inside the container.
- You should see the model accuracy printed.
- The container runs and stops automatically after the program finishes.

## 12. Advantages
- Portability: The container can run on any computer with Docker.
- Reproducibility: The same code and environment run every time.
- Easy deployment: It is easy to move the container to another machine.

## 13. Conclusion
This lab shows how to package a simple ML model into a Docker container. It helps the model run in a clean and repeatable way.
