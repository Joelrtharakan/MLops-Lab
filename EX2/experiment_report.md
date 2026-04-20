# Configuring Continuous Integration with GitHub Actions

## 1. Title
Configuring Continuous Integration with GitHub Actions

## 2. Aim
To learn how to make GitHub run tests automatically when code changes.

## 3. Prerequisites
- A computer with Python installed
- Git installed
- A GitHub account
- Basic knowledge of files and folders

## 4. Theory
Continuous Integration (CI) means code is tested automatically when it changes. GitHub Actions is a tool that runs these tests in the cloud. This helps catch mistakes early and keeps code working when many people work together.

## 5. Project Structure

CI-project/
│
├── app.py
├── test_app.py
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml

## 6. Implementation

### Step 1: Create GitHub repository
- Open GitHub in a browser.
- Click "New repository".
- Give the repository a name.
- Click "Create repository".

### Step 2: Clone repository
- Open a terminal.
- Run this command:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

### Step 3: Create Python file (`app.py`)
- Create `app.py` in the repository.
- Add this simple code:

```python
# app.py
print("CI Lab Working")
```

### Step 4: Create test file (`test_app.py`)
- Create `test_app.py`.
- Add a simple test with pytest:

```python
# test_app.py

def test_ci():
    assert True
```

### Step 5: Create `requirements.txt`
- Add this line:

```text
pytest
```

### Step 6: Create GitHub Actions workflow
- Make folders: `.github/workflows`.
- Create `ci.yml` inside that folder.
- Add the workflow content below.

## 7. GitHub Actions Workflow File

This is the exact workflow file content:

```yaml
name: Continuous Integration Lab

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout source code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
```

### Explain each part in simple terms
- `name`: The workflow name.
- `on`: When the workflow runs.
  - `push`: when code is pushed to GitHub.
  - `pull_request`: when someone opens a pull request.
- `jobs`: The tasks the workflow does.
- `runs-on`: The virtual machine used for testing.
- `steps`: Each action in the workflow.
- `uses: actions/checkout@v3`: Get the repository code.
- `uses: actions/setup-python@v4`: Install Python.
- `pip install -r requirements.txt`: Install the test library.
- `pytest`: Run the tests.

## 8. Commands Section

Install dependencies locally:
```bash
python -m pip install -r requirements.txt
```

Run the test locally:
```bash
pytest
```

Save and push changes to GitHub:
```bash
git add .
git commit -m "Add CI workflow"
git push
```

## 9. Output / Result
- On GitHub, the workflow starts automatically.
- The test result shows pass or fail.
- A green check mark means the workflow passed.

## 10. Notes for Exam
- Know what CI means.
- Know that GitHub Actions runs workflow files in `.github/workflows`.
- Know the difference between `push` and `pull_request`.
- Know that `pytest` is a test tool.

## 11. Conclusion
This lab shows how to set up CI with GitHub Actions. It keeps code tested automatically and helps developers find errors early.
