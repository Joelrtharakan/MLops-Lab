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
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        features = data['features']
    else:
        features = [
            float(request.args.get('sepal_length', 0)),
            float(request.args.get('sepal_width', 0)),
            float(request.args.get('petal_length', 0)),
            float(request.args.get('petal_width', 0)),
        ]
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
