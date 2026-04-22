# Machine Learning Interoperability with ONNX

## 1. Title
Machine Learning Interoperability with ONNX

## 2. Objective
Learn how to convert a simple machine learning model to ONNX and run it using ONNX Runtime.

## 3. Job Role
Machine Learning Engineer / Data Science student

## 4. Skills Required
- Python basics: write and run code
- Machine learning: use a simple model
- ONNX: convert and run a saved model

## 5. Prerequisites
- Python installed
- Basic terminal use
- Basic understanding of a model training script

## 6. Theory
- Interoperability means different tools can use the same model.
- ONNX is a model format that works with many libraries.
- ONNX is useful because it lets you move a model from training to deployment.
- Model portability means you can take a model from one system and run it in another.
  - Example: train with scikit-learn, run with ONNX Runtime.

## 7. Implementation

### Step 1: Install libraries
Install the required libraries:
```bash
pip install -r requirements.txt
```

### Step 2: Create a simple ML model
Use the Iris dataset and train a simple Logistic Regression model.

### Step 3: Train the model
Train the model on the iris data and print a message when it is ready.

### Step 4: Convert model to ONNX format
Use `skl2onnx` to convert the trained scikit-learn model to `model.onnx`.

### Step 5: Load ONNX model
Use `onnxruntime` to load the saved `model.onnx` file.

### Step 6: Run inference using ONNX Runtime
Run a prediction on one sample and compare it to the expected label.

## 8. Sample Code (FULL PROGRAM)
Use the full code in `app.py`.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import onnxruntime as ort
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Load data
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print('Model trained')

# Convert to ONNX
onnx_model = convert_sklearn(
    model,
    initial_types=[('input', FloatTensorType([None, 4]))]
)

# Save model
with open('model.onnx', 'wb') as f:
    f.write(onnx_model.SerializeToString())
print('Saved model.onnx')

# Load ONNX model
session = ort.InferenceSession('model.onnx')
input_name = session.get_inputs()[0].name

# Test prediction
sample = X_test[:1].astype('float32')
prediction = session.run(None, {input_name: sample})[0]
print('Prediction:', prediction)
print('Actual:', y_test[0])
```

## 9. Commands Section
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the program:
```bash
python app.py
```

## 10. Output
Expected output:
- Model trained successfully.
- ONNX model saved as `model.onnx`.
- Prediction printed from the ONNX model.

## 11. Explanation of Result
- The ONNX model gives the same kind of prediction as the original model.
- Interoperability means the model can work in different tools.
- This lab shows how to move a model from training to inference.

## 12. Advantages
- Model portability
- Framework independent
- Easy deployment

## 13. Limitations
- Conversion can fail for complex models
- Some operations are not supported in ONNX

## 14. Exam Notes
- Know the difference between training and inference.
- Know why ONNX saves a model to a file.
- Know how to load `model.onnx` with ONNX Runtime.

## 15. Conclusion
ONNX helps reuse models across platforms. It makes machine learning models easier to move from training to production.
