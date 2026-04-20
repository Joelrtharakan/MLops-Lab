# EX7 TPOT AutoML Experiment

## 1. Title
Simple TPOT AutoML experiment using the Iris dataset.

## 2. Objective
Train a small AutoML model with TPOT on the Iris dataset and see the model accuracy.

## 3. Prerequisites
- Python 3.11 installed
- A working Python virtual environment in `EX7/venv`
- Required packages installed from `requirements.txt`

## 4. Description
This project uses TPOT to automatically find a good machine learning pipeline for the Iris dataset.
It keeps the settings small so it runs quickly for a lab demonstration.

## 5. Project structure
EX7/
├── experiment_report.md
├── requirements.txt
├── run_tpot.py
└── venv/

## 6. Implementation
1. Create or activate the virtual environment in `EX7`.
2. Install the required Python packages.
3. Run the TPOT script.
4. Read the output to see the generated model accuracy.

## 7. Code explanation
- `load_iris()` loads the Iris dataset from scikit-learn.
- `train_test_split()` splits the data into training and test sets.
- `TPOTClassifier()` runs AutoML with:
  - `generations=2`
  - `population_size=10`
  - `verbosity=2`
  - `random_state=42`
- `fit()` trains the model.
- `predict()` makes predictions on the test set.
- `accuracy_score()` prints how often the model is correct.

## 8. Dependencies
The script only needs:
- `tpot`
- `scikit-learn`

## 9. Commands
Install dependencies:
```bash
cd "/Users/joeltharakan/Downloads/MLOPS LAB/EX7"
./venv/bin/python3 -m pip install -r requirements.txt
```

Run the script:
```bash
./venv/bin/python3 run_tpot.py
```

## 10. Expected output
The script should print:
- `Starting TPOT...`
- `Generation 1 - Current best internal CV score: ...`
- `Generation 2 - Current best internal CV score: ...`
- `Best pipeline: ...`
- `TPOT finished. Accuracy on test set: ...`

Example output:
```text
Starting TPOT...
Generation 1 - Current best internal CV score: 0.9583333333333334
Generation 2 - Current best internal CV score: 0.9583333333333334
Best pipeline: KNeighborsClassifier(...)
TPOT finished. Accuracy on test set: 1.0000
```

## 11. What this means
- TPOT automatically tests simple model options.
- `generations` is how many rounds of model search TPOT performs.
- `population_size` is how many candidate pipelines are tried each round.
- `accuracy` shows how often the model predicted the right Iris species.

## 12. Notes
- The code is kept simple for lab use.
- No extra files are exported in this version.
- If TPOT prints a warning about package updates, it is safe to ignore for this lab.
