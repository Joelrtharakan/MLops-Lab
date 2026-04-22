from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load model
model = load("iris_api_model.pkl")

# Predict route (GET + POST)
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data = request.json["features"]
    else:
        # default input for browser
        data = [5.1, 3.5, 1.4, 0.2]

    result = model.predict([data])[0]
    return jsonify({"prediction": int(result)})

# Run app
if __name__ == "__main__":
    app.run()