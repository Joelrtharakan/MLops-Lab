# Define CLI Commands for Machine Learning Model

## 1. Title
Define CLI Commands for Machine Learning Model

## 2. Objective
Learn how to make a simple command line tool for training and predicting with a machine learning model.

## 3. Job Role
Machine Learning Engineer / Python Developer

## 4. Skills Required
- Python basics: run a script and use simple code.
- ML basics: know what train and predict mean.
- CLI basics: use the command line.

## 5. Prerequisites
- Python installed on your computer.
- Know how to open a terminal.
- Know how to run `python` commands.

## 6. Theory
- CLI means Command Line Interface. It is a way to use a program by typing commands in a terminal.
- CLI is useful in ML projects because you can run training and prediction without opening a full program.
- The `train` command means build the model from data.
- The `predict` command means use the saved model to make a result.

## 7. Project Structure

cli-project/
│
├── cli.py
└── requirements.txt

## 8. Implementation

Step 1: Install libraries
- Install the required packages with pip.

Step 2: Create cli.py file
- Create `cli.py` and add a simple CLI using `argparse`.
- Use the iris dataset from scikit-learn.
- Use `RandomForestClassifier` to train the model.
- Use `joblib` to save and load the model.

Step 3: Write train command
- Add a `train` command in `cli.py`.
- Load iris data, split it, train the model, and save it as `iris_model.joblib`.
- Print a message when the model is saved.

Step 4: Write predict command
- Add a `predict` command in `cli.py`.
- Load the saved model using `joblib`.
- If no sample input is given, show accuracy on the iris data.
- If sample input is given, predict one sample and print the result.

Step 5: Run CLI commands
- Use the terminal to run training and prediction commands.

## 9. Commands Section

Train:
```bash
python cli.py train
```

Predict accuracy:
```bash
python cli.py predict --model iris_model.joblib
```

Predict sample:
```bash
python cli.py predict --model iris_model.joblib --samples "5.1,3.5,1.4,0.2"
```

## 10. Output
- The `train` command prints `Model saved as iris_model.joblib`.
- The `predict` command without samples prints `Accuracy: ...`.
- The `predict` command with samples prints `Prediction: ...`.

## 11. Answer Questions Clearly

- Explain train command:
  - It trains a random forest model on iris data and saves the model file.
- Explain predict command:
  - It loads the saved model and either shows accuracy or predicts a sample.
- Explain inputs and outputs:
  - Input for train: no extra input, just run the command.
  - Input for predict: the model file path and optional sample values.
  - Output for train: model saved message.
  - Output for predict: accuracy or prediction value.
- Explain error handling:
  - If no command is given, the CLI shows help.
  - If model file is missing, the program will show a file error.

## 12. Advantages
- Easy to automate with scripts.
- The same steps can be repeated.
- It is useful for pipelines and simple ML tasks.

## 13. Conclusion
- CLI helps automate ML tasks.
- This lab shows how to train and predict with a simple command line tool.
- The CLI makes the model workflow easy and repeatable.
