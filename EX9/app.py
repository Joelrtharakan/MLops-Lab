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
print("Model trained")

# Convert to ONNX
onnx_model = convert_sklearn(
    model,
    initial_types=[("input", FloatTensorType([None, 4]))]
)

# Save model
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

# Load ONNX model
session = ort.InferenceSession("model.onnx")
input_name = session.get_inputs()[0].name

# Test prediction
sample = X_test[:1].astype("float32")
prediction = session.run(None, {input_name: sample})[0]

print("Prediction:", prediction)
print("Actual:", y_test[0])