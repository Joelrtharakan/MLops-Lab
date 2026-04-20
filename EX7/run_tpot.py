import os
os.environ["PYTHONWARNINGS"] = "ignore::UserWarning"
import warnings
warnings.filterwarnings("ignore")
warnings.showwarning = lambda *args, **kwargs: None
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tpot import TPOTClassifier


data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

automl = TPOTClassifier(
    generations=2,
    population_size=10,
    verbosity=2,
    n_jobs=1,
    random_state=42,
    disable_update_check=True,
)

print("Starting TPOT...")
automl.fit(X_train, y_train)

preds = automl.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"TPOT finished. Accuracy on test set: {acc:.4f}")
