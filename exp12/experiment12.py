from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from joblib import dump

# Load dataset
data = load_wine()
x, y = data.data, data.target

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Train models
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()

model1.fit(x_train, y_train)
model2.fit(x_train, y_train)

# Predict
pred1 = model1.predict(x_test)
pred2 = model2.predict(x_test)

# Evaluation (only Accuracy & F1)
print("Logistic Accuracy:", accuracy_score(y_test, pred1))
print("Decision Tree Accuracy:", accuracy_score(y_test, pred2))

print("Logistic F1:", f1_score(y_test, pred1, average="weighted"))
print("Decision Tree F1:", f1_score(y_test, pred2, average="weighted"))

# Save models
dump(model1, "logistic_wine.pkl")
dump(model2, "decision_tree_wine.pkl")