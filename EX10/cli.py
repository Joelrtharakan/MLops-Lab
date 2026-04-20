import argparse
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

# Train and save model
def train():
    X, y = load_iris(return_X_y=True)
    model = RandomForestClassifier()
    model.fit(X, y)
    dump(model, "model.joblib")
    print("Model saved!")

# Predict or check accuracy
def predict(path, sample):
    model = load(path)

    if sample:
        values = list(map(float, sample.split(",")))
        result = model.predict([values])
        print("Prediction:", result[0])
    else:
        X, y = load_iris(return_X_y=True)
        acc = (model.predict(X) == y).mean()
        print("Accuracy:", acc)

# CLI setup
parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["train", "predict"])
parser.add_argument("--model", default="model.joblib")
parser.add_argument("--sample", help="e.g. 5.1,3.5,1.4,0.2")

args = parser.parse_args()

if args.mode == "train":
    train()
else:
    predict(args.model, args.sample)