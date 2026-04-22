from pathlib import Path

base = Path(__file__).resolve().parent
experiments = {
    'exp1': {
        'title': 'Linear Regression + Diabetes',
        'objective': 'Train and evaluate a linear regression model on the diabetes dataset, then save the trained model.',
        'skills': ['Python', 'scikit-learn', 'linear regression', 'model evaluation', 'joblib model persistence'],
        'description': 'This experiment uses the diabetes regression dataset to demonstrate an end-to-end regression workflow. The model is trained, evaluated with MAE, MSE, and RMSE, and saved for reuse.',
        'implementation': [
            'Load the diabetes dataset with load_diabetes().',
            'Split the data into training and test sets with train_test_split.',
            'Train a LinearRegression model on the training data.',
            'Predict on the test set and calculate MAE, MSE, and RMSE.',
            'Make a single-sample prediction using the trained model.',
            'Save the trained model to disk with joblib.dump().'
        ],
        'commands': ['python experiment1.py'],
        'result': 'A trained linear regression model, evaluation metrics for the diabetes dataset, and a saved model file for reuse.',
        'learning': ['How to build a regression model', 'How to evaluate regression performance', 'How to save a model for later use'],
        'tips': ['Always check model assumptions for regression.', 'Use a test split for reliable evaluation.', 'Save the model after training so you can reuse it later.']
    },
    'exp2': {
        'title': 'Logistic Regression + Breast Cancer',
        'objective': 'Train and evaluate a logistic regression classifier on the breast cancer dataset and save the final model.',
        'skills': ['Python', 'scikit-learn', 'logistic regression', 'stratified splitting', 'joblib'],
        'description': 'This experiment builds a binary classification pipeline for breast cancer prediction. It trains a logistic regression model with stratified splitting and saves the trained classifier.',
        'implementation': [
            'Load the breast cancer dataset with load_breast_cancer().',
            'Split the data into train/test using stratify=y.',
            'Scale the data with StandardScaler to improve convergence.',
            'Train LogisticRegression with max_iter=1000.',
            'Evaluate performance with accuracy, confusion matrix, precision, and recall.',
            'Save the trained model to disk with joblib.dump().'
        ],
        'commands': ['python experiment2.py'],
        'result': 'A trained and saved logistic regression classifier for breast cancer prediction and evaluation metrics.',
        'learning': ['How to preprocess data before classification', 'Why scaling helps logistic regression', 'How to save and reuse a trained model'],
        'tips': ['Use stratified split to preserve label distribution.', 'Scale data before training logistic regression.', 'Check model convergence warnings and increase max_iter if needed.']
    },
    'exp3': {
        'title': 'Decision Tree + Iris',
        'objective': 'Train and evaluate a decision tree classifier on the Iris dataset and save the trained model.',
        'skills': ['Python', 'scikit-learn', 'decision trees', 'classification metrics', 'joblib'],
        'description': 'This experiment trains a decision tree on the Iris dataset, evaluates test accuracy and classification metrics, and persists the model for future use.',
        'implementation': [
            'Load the Iris dataset with load_iris().',
            'Split the data into training and testing sets.',
            'Train DecisionTreeClassifier on the training data.',
            'Predict on the test set and evaluate accuracy and classification report.',
            'Save the trained model using joblib.dump().'
        ],
        'commands': ['python experiment3.py'],
        'result': 'A trained decision tree model for Iris classification, evaluation output, and a saved model file.',
        'learning': ['How decision trees work for classification', 'How to evaluate class-level metrics', 'How to save a scikit-learn model'],
        'tips': ['Use classification_report to understand per-class behavior.', 'Decision trees are easy to interpret but can overfit.', 'Save trained models to avoid retraining.']
    },
    'exp4': {
        'title': 'Random Forest + Wine',
        'objective': 'Train and evaluate a random forest classifier on the Wine dataset and save the trained model.',
        'skills': ['Python', 'scikit-learn', 'random forest', 'ensemble learning', 'model persistence'],
        'description': 'This experiment uses the Wine dataset to demonstrate an ensemble classification model. The random forest is trained, evaluated with accuracy and F1 score, and saved for reuse.',
        'implementation': [
            'Load the Wine dataset with load_wine().',
            'Split the data into training and test sets.',
            'Train RandomForestClassifier with n_estimators=100.',
            'Evaluate test accuracy and weighted F1 score.',
            'Save the trained model with joblib.dump().'
        ],
        'commands': ['python experiment4.py'],
        'result': 'A saved random forest model for wine classification and evaluation metrics.',
        'learning': ['Why ensemble methods improve stability', 'How to use weighted F1 score', 'How to persist trained models'],
        'tips': ['Random forests reduce overfitting compared to single trees.', 'Check both accuracy and F1 for multi-class problems.', 'Save models when training is expensive.']
    },
    'exp5': {
        'title': 'KNN + Iris',
        'objective': 'Train and evaluate a K-Nearest Neighbors classifier on the Iris dataset and save the model.',
        'skills': ['Python', 'scikit-learn', 'KNN', 'classification', 'joblib'],
        'description': 'This experiment uses KNN to classify Iris flowers, evaluates accuracy, makes a sample prediction, and saves the classifier.',
        'implementation': [
            'Load the Iris dataset with load_iris().',
            'Split the data into training and test sets.',
            'Train KNeighborsClassifier with n_neighbors=5.',
            'Predict and print test accuracy.',
            'Make a single-sample prediction and save the model using joblib.dump().'
        ],
        'commands': ['python experiment5.py'],
        'result': 'A trained KNN classifier for Iris and a saved model file ready for reuse.',
        'learning': ['How KNN works for classification', 'How to evaluate KNN accuracy', 'How to persist a trained model'],
        'tips': ['KNN is simple but can be slow on large datasets.', 'Use a test split to verify performance.', 'Save the model for inference without retraining.']
    },
    'exp6': {
        'title': 'SVM + Breast Cancer',
        'objective': 'Train and evaluate an SVM classifier on the breast cancer dataset and save the trained model.',
        'skills': ['Python', 'scikit-learn', 'SVM', 'binary classification', 'joblib'],
        'description': 'This experiment trains an SVM model for breast cancer classification, evaluates key metrics, and saves the model to disk.',
        'implementation': [
            'Load the breast cancer dataset with load_breast_cancer().',
            'Split the data into training and testing sets.',
            'Train SVC on the training data.',
            'Evaluate accuracy, precision, recall, and F1 score.',
            'Save the trained SVM model with joblib.dump().'
        ],
        'commands': ['python experiment6.py'],
        'result': 'A saved SVM classifier for breast cancer with evaluation metrics.',
        'learning': ['How SVM works for binary classification', 'How to interpret precision and recall', 'How to persist a machine learning model'],
        'tips': ['SVM can be sensitive to feature scaling.', 'Use test data to validate model performance.', 'Save the trained model for future inference.']
    },
    'exp7': {
        'title': 'Naive Bayes + Wine',
        'objective': 'Train and evaluate a Gaussian Naive Bayes classifier on the Wine dataset and save the model.',
        'skills': ['Python', 'scikit-learn', 'Naive Bayes', 'classification', 'joblib'],
        'description': 'This experiment trains a Gaussian Naive Bayes classifier on the Wine dataset, evaluates accuracy and classification metrics, and saves the model.',
        'implementation': [
            'Load the Wine dataset with load_wine().',
            'Split the data into training and test sets.',
            'Train GaussianNB on the training data.',
            'Evaluate accuracy and classification report.',
            'Save the trained model using joblib.dump().'
        ],
        'commands': ['python experiment7.py'],
        'result': 'A saved Naive Bayes model for Wine classification and its evaluation output.',
        'learning': ['How Gaussian Naive Bayes works', 'How to evaluate a multi-class classifier', 'How to save models for reuse'],
        'tips': ['Naive Bayes assumes feature independence.', 'Use classification_report for detailed metrics.', 'Persist models to avoid retraining.']
    },
    'exp8': {
        'title': 'Gradient Boosting + Breast Cancer',
        'objective': 'Train and evaluate a gradient boosting classifier on the breast cancer dataset and save the trained model.',
        'skills': ['Python', 'scikit-learn', 'gradient boosting', 'ensemble learning', 'model saving'],
        'description': 'This experiment uses gradient boosting on the breast cancer dataset, evaluates test accuracy, and persists the model.',
        'implementation': [
            'Load the breast cancer dataset with load_breast_cancer().',
            'Split into training and testing sets.',
            'Train GradientBoostingClassifier on the training data.',
            'Evaluate accuracy and confusion matrix.',
            'Save the model using joblib.dump().'
        ],
        'commands': ['python experiment8.py'],
        'result': 'A trained gradient boosting model saved to disk and evaluation metrics for breast cancer classification.',
        'learning': ['How gradient boosting works', 'How to evaluate binary classification', 'How to save scikit-learn models'],
        'tips': ['Gradient boosting is powerful for structured data.', 'Check performance using accuracy and confusion matrix.', 'Save trained models after training.']
    },
    'exp9': {
        'title': 'AdaBoost + Iris',
        'objective': 'Train and evaluate an AdaBoost classifier on the Iris dataset and save the model.',
        'skills': ['Python', 'scikit-learn', 'AdaBoost', 'ensemble methods', 'joblib'],
        'description': 'This experiment trains an AdaBoost ensemble on the Iris dataset, evaluates accuracy and weighted F1 score, and saves the trained model.',
        'implementation': [
            'Load the Iris dataset with load_iris().',
            'Split data into training and test sets.',
            'Train AdaBoostClassifier with n_estimators=50.',
            'Evaluate test accuracy and weighted F1 score.',
            'Save the trained model with joblib.dump().'
        ],
        'commands': ['python experiment9.py'],
        'result': 'A saved AdaBoost model for Iris classification and evaluation metrics.',
        'learning': ['How boosting improves weak learners', 'How to evaluate multi-class models', 'How to persist trained models'],
        'tips': ['AdaBoost builds a strong model from weak learners.', 'Check weighted F1 for class-balanced evaluation.', 'Save models after training.']
    },
    'exp10': {
        'title': 'MLP Classifier + Digits',
        'objective': 'Train and evaluate an MLP neural network on the Digits dataset and save the trained model.',
        'skills': ['Python', 'scikit-learn', 'neural networks', 'MLP', 'joblib'],
        'description': 'This experiment uses a multi-layer perceptron to classify handwritten digits, evaluates accuracy, and saves the trained model.',
        'implementation': [
            'Load the Digits dataset with load_digits().',
            'Split into training and testing sets.',
            'Train MLPClassifier with max_iter=300.',
            'Evaluate test accuracy and confusion matrix.',
            'Save the trained model with joblib.dump().'
        ],
        'commands': ['python experiment10.py'],
        'result': 'A saved neural network model for digit classification and evaluation output.',
        'learning': ['How to train an MLP classifier', 'How to evaluate digit recognition models', 'How to persist a neural network model'],
        'tips': ['MLPs may require tuning max_iter for convergence.', 'Use confusion matrix to see digit-level performance.', 'Save the model so it can be reused.']
    },
    'exp11': {
        'title': 'Complete ML Pipeline + Iris',
        'objective': 'Build a complete preprocessing and modeling pipeline for Iris classification and save the pipeline.',
        'skills': ['Python', 'scikit-learn', 'pipelines', 'scaling', 'logistic regression', 'joblib'],
        'description': 'This experiment demonstrates an end-to-end ML pipeline with preprocessing and modeling in one object, then saves the pipeline for inference.',
        'implementation': [
            'Load the Iris dataset with load_iris().',
            'Split into training and testing sets.',
            'Build a pipeline with StandardScaler and LogisticRegression.',
            'Train the pipeline on the training data.',
            'Predict test labels and evaluate accuracy.',
            'Save the pipeline using joblib.dump().'
        ],
        'commands': ['python experiment11.py'],
        'result': 'A saved ML pipeline for Iris classification and the ability to reuse preprocessing and model steps together.',
        'learning': ['How to use scikit-learn pipelines', 'Why scaling belongs inside a pipeline', 'How to save a pipeline for inference'],
        'tips': ['Pipelines keep preprocessing and modeling consistent.', 'Always save the full pipeline, not just the model.', 'Use pipelines to reduce inference-time errors.']
    },
    'exp12': {
        'title': 'Compare Two Algorithms + Wine',
        'objective': 'Compare Logistic Regression and Decision Tree performance on the Wine dataset and save both models.',
        'skills': ['Python', 'scikit-learn', 'model comparison', 'evaluation metrics', 'joblib'],
        'description': 'This experiment trains two different classifiers on the Wine dataset, compares their accuracy and weighted F1 scores, and saves both models for later use.',
        'implementation': [
            'Load the Wine dataset with load_wine().',
            'Split into training and testing sets.',
            'Train LogisticRegression and DecisionTreeClassifier.',
            'Predict on the test set for both models.',
            'Evaluate and compare accuracy and weighted F1 scores.',
            'Save both trained models with joblib.dump().'
        ],
        'commands': ['python experiment12.py'],
        'result': 'Two saved models and a direct comparison of their Wine classification performance.',
        'learning': ['How to compare different classifiers', 'How to use weighted F1 for multi-class problems', 'How to save multiple models'],
        'tips': ['Compare models on the same test set.', 'Look at multiple metrics, not just accuracy.', 'Save each model separately for future analysis.']
    },
    'exp13': {
        'title': 'Saved Model Prediction System + Breast Cancer',
        'objective': 'Train a breast cancer classifier, save it, reload it, and make a prediction with the loaded model.',
        'skills': ['Python', 'scikit-learn', 'joblib', 'model persistence', 'inference'],
        'description': 'This experiment shows how to save a trained model to disk and load it back later for prediction, demonstrating model persistence and reuse.',
        'implementation': [
            'Load the breast cancer dataset with load_breast_cancer().',
            'Split into training and testing sets.',
            'Train a LogisticRegression model.',
            'Save the trained model to disk.',
            'Reload the model using joblib.load().',
            'Make a prediction on a test sample with the loaded model.'
        ],
        'commands': ['python experiment13.py'],
        'result': 'A saved logistic regression model that can be loaded and used for inference without retraining.',
        'learning': ['How to persist and reload scikit-learn models', 'How to separate training from inference', 'Why model persistence is useful in production workflows'],
        'tips': ['Keep model file names consistent.', 'Load the saved model before making predictions.', 'Use joblib for efficient scikit-learn serialization.']
    },
    'exp14': {
        'title': 'Flask Model Serving + Iris',
        'objective': 'Serve a saved Iris model through a Flask API endpoint for real-time prediction.',
        'skills': ['Python', 'Flask', 'scikit-learn', 'model serving', 'joblib'],
        'description': 'This experiment saves a trained Iris decision tree model and then loads it to demonstrate how a saved model can support API-based predictions.',
        'implementation': [
            'Load the Iris dataset with load_iris().',
            'Train a DecisionTreeClassifier on the full dataset.',
            'Save the trained model to iris_api_model.pkl.',
            'Reload the model from disk.',
            'Make a test prediction using the loaded model.'
        ],
        'commands': ['python experiment14.py'],
        'result': 'A saved Iris model that can be loaded for inference, demonstrating steps for API-ready model persistence.',
        'learning': ['How to save and reload a model for serving', 'Why model persistence is important for APIs', 'How to test saved model predictions'],
        'tips': ['Save the trained model before deployment.', 'Reload the saved model to verify persistence.', 'Use saved models to avoid retraining in production.']
    },
    'exp15': {
        'title': 'Simple Flask App',
        'objective': 'Expose a saved Iris model as a simple Flask web API with GET and POST prediction routes.',
        'skills': ['Python', 'Flask', 'scikit-learn', 'API development', 'model serving'],
        'description': 'This experiment loads a saved Iris model and builds a lightweight Flask application to serve predictions through a /predict endpoint.',
        'implementation': [
            'Load a saved model from iris_api_model.pkl with joblib.load().',
            'Create a Flask app with a /predict route.',
            'Accept default GET input or feature arrays via POST.',
            'Predict the class label and return JSON output.',
            'Run the Flask app locally.'
        ],
        'commands': ['python experiment15.py'],
        'result': 'A running Flask application that serves machine learning predictions through an API endpoint.',
        'learning': ['How to build a simple Flask API', 'How to serve model predictions over HTTP', 'How to handle GET and POST requests for inference'],
        'tips': ['Verify the saved model file exists before starting the app.', 'Use JSON POST requests for new input data.', 'Test the endpoint with curl or a browser.']
    },
    'exp16': {
        'title': 'End-to-End Project + Any Inbuilt Dataset',
        'objective': 'Complete a full machine learning workflow from training to saving a model on an inbuilt dataset.',
        'skills': ['Python', 'scikit-learn', 'end-to-end ML workflow', 'model persistence', 'evaluation'],
        'description': 'This experiment demonstrates a full machine learning project cycle using a built-in dataset, training a model, evaluating it, making a sample prediction, and saving the final model.',
        'implementation': [
            'Load an inbuilt dataset with load_iris().',
            'Split into training and testing sets.',
            'Train a RandomForestClassifier.',
            'Evaluate the model on the test set.',
            'Make a single-sample prediction.',
            'Save the trained model using joblib.dump().'
        ],
        'commands': ['python experiment16.py'],
        'result': 'A complete saved ML model ready for reuse and a demonstration of a full training-to-deployment workflow.',
        'learning': ['How to execute an end-to-end ML project', 'How to evaluate and save a model', 'How to make predictions with a trained model'],
        'tips': ['Treat each experiment as a full project pipeline.', 'Save your final model after training and validation.', 'Test model predictions on sample inputs.']
    },
}

for exp, meta in experiments.items():
    exp_dir = base / exp
    if not exp_dir.exists():
        print(f'Missing folder: {exp}')
        continue
    readme_path = exp_dir / 'README.md'
    lines = [f'# {meta["title"]}', '', '## Objective', '', meta['objective'], '', '## Job Role', '', 'Data Scientist and ML Engineer', '', '## Skills Required', '']
    lines += [f'- {skill}' for skill in meta['skills']]
    lines += ['', '## Prerequisites', '', '- Python installed on your computer', '- pip available to install packages', '- Basic familiarity with running Python scripts', '', '## Description', '', meta['description'], '', '## Implementation', '']
    lines += [f'{i+1}. {step}' for i, step in enumerate(meta['implementation'])]
    lines += ['', '## Commands', '']
    for cmd in meta['commands']:
        lines += ['```bash', cmd, '```', '']
    lines += ['## Result', '', meta['result'], '', '## Learning Outcome', '']
    lines += [f'- {item}' for item in meta['learning']]
    lines += ['', '## Exam Tips', '']
    lines += [f'- {tip}' for tip in meta['tips']]
    lines.append('')
    readme_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {readme_path}')
