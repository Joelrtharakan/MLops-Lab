# EX7 TPOT AutoML Experiment

## 1. Title
Simple TPOT AutoML experiment using the Iris dataset.

## 2. Objective
Train a small AutoML model with TPOT on the Iris dataset and check how accurate it is.

## 3. Prerequisites
- Python 3.11 installed
- A working virtual environment in `EX7/venv`
- Required packages installed from `requirements.txt`

## 4. Job Role
Machine Learning Engineer

## 5. Theory
- AutoML helps find the best model automatically.
- TPOT tests many pipelines and selects the best one.
- This saves time compared to choosing the model by hand.

## 6. Project Structure

EX7/
├── experiment_report.md
├── requirements.txt
├── run_tpot.py
└── venv/

## 7. Implementation

### Step 1: Activate virtual environment
```bash
cd "/Users/joeltharakan/Downloads/MLOPS LAB/EX7"
source venv/bin/activate
```

### Step 2: Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### Step 3: Run the TPOT script
```bash
python3 run_tpot.py
```

### Step 4: Read the output
- Look for the best pipeline.
- Check the accuracy on the test set.

## 8. Code explanation
- `load_iris()` loads the Iris dataset.
- `train_test_split()` divides data into train and test sets.
- `TPOTClassifier()` searches for the best model pipeline.
- `generations` controls how many search rounds are used.
- `population_size` controls how many pipelines are tested each round.
- `fit()` runs the AutoML search.
- `predict()` makes predictions on test data.
- `accuracy_score()` tells how often predictions are correct.

## 9. Dependencies
- `tpot`
- `scikit-learn`

## 10. Commands
Install dependencies:
```bash
cd "/Users/joeltharakan/Downloads/MLOPS LAB/EX7"
./venv/bin/python3 -m pip install -r requirements.txt
```

Run the experiment:
```bash
./venv/bin/python3 run_tpot.py
```

## 11. Expected Output
The script should print messages like:
- `Starting TPOT...`
- `Generation 1 - Current best internal CV score: ...`
- `Generation 2 - Current best internal CV score: ...`
- `Best pipeline: ...`
- `TPOT finished. Accuracy on test set: ...`

Example:
```text
Starting TPOT...
Generation 1 - Current best internal CV score: 0.9583
Generation 2 - Current best internal CV score: 0.9583
Best pipeline: KNeighborsClassifier(...)
TPOT finished. Accuracy on test set: 1.0000
```

## 12. Results
- TPOT automatically tests many models.
- The output shows which pipeline was best.
- Accuracy tells how good the model is on the test set.

## 13. Exam Notes
- Know that TPOT is AutoML.
- Know the meaning of `generations` and `population_size`.
- Know how to run the script in the virtual environment.

## 14. Conclusion
This lab shows how to use TPOT to automate model selection on Iris data. It helps compare models and check accuracy quickly.
