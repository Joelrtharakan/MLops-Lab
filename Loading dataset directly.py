# ...existing code...
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from joblib import dump

# Load dataset from Downloads
file_path = "/Users/joeltharakan/Downloads/your_dataset.csv"
df = pd.read_csv(file_path)

# Change "target" to your actual label column name
X = df.drop(columns=["target"]).values
y = df["target"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

new_data = [X_test[0]]
print("Prediction:", model.predict(new_data))

dump(model, "linear_regression_model.pkl")
# ...existing code...