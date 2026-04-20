# Configuring Continuous Integration with GitHub Actions

## 1. Title
Configuring Continuous Integration with GitHub Actions

## 2. Aim
To learn how to make GitHub run tests automatically using GitHub Actions.

## 3. Prerequisites
- A computer with Python installed
- Git installed
- A GitHub account
- Basic knowledge of files and folders

## 4. Theory
Continuous Integration (CI) means code is tested automatically when it is changed. GitHub Actions is a tool that can run tests when you push code to GitHub. This is useful because tests can run by themselves and show if the code is okay.

## 5. Implementation

### Step 1: Create GitHub repository
- Go to GitHub website.
- Click on "New repository".
- Give the repository a name.
- Choose public or private.
- Click "Create repository".

### Step 2: Clone repository
- Open a terminal.
- Run this command:

```bash
git clone git clone https://github.com/your-username/your-repo-name.git
```

### Step 3: Create Python file (app.py)
- In the repository folder, create a file named `app.py`.
- Put this code:

```python
# app.py
print("CI Lab Working")
```

### Step 4: Create test file (test_app.py using pytest)
- Create a file named `test_app.py`.
- Put this code:

```python
# test_app.py

def test_ci():
    assert True
```

### Step 5: Create requirements.txt
- Create a file named `requirements.txt`.
- Put this text:

```text
pytest
```

### Step 6: Create .github/workflows folder
- In the repository folder, make a folder named `.github`.
- Inside `.github`, make another folder named `workflows`.

### Step 7: Create ci.yml file
- Inside `.github/workflows`, create a file named `ci.yml`.
- Put the workflow code there.

## 6. GitHub Actions Workflow File

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
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
```

### Explain each part in simple terms
- `name`: The name of this workflow.
- `on`: When the workflow should run.
  - `push`: Run when code is pushed.
  - `pull_request`: Run when a pull request is opened.
- `jobs`: The list of tasks to run.
- `runs-on`: The computer type used to run the job.
- `steps`: The actions inside the job.

## 7. Git Commands Section

Use these commands to save and send your code to GitHub:

```bash
git add .
git commit -m "Configured CI"
git push
```

## 8. Output / Result
After pushing, GitHub starts the workflow automatically. The tests run on GitHub. If everything passes, you see a green tick on GitHub.

## 9. Conclusion
This lab shows how to set up a simple CI workflow with GitHub Actions. It makes tests run automatically and helps keep code working.
