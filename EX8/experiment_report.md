# Monitoring and Logging in Machine Learning with Python

## 1. Title
Monitoring and Logging in Machine Learning with Python

## 2. Objective
Learn how to track a simple ML training loop using logging, TensorBoard, and Prometheus.

## 3. Job Role
Machine Learning Engineer / Data Science student.

## 4. Skills Required
- Basic Python: write and run a simple program.
- Logging: save training messages to a file.
- Monitoring: collect values to watch later.
- TensorBoard: visualize loss and accuracy.
- Prometheus: expose metrics through a web endpoint.

## 5. Prerequisites
- Python 3 installed.
- A terminal or command line.
- Basic understanding of running Python code.

## 6. Theory
- Logging is saving messages about how the program runs.
- Monitoring is exposing values so we can watch them live.
- Difference:
  - Logging is like writing notes in a diary.
  - Monitoring is like watching a clock or meter while the program runs.

## 7. Implementation

### Step 1: Install libraries
Install the required libraries inside the `EX8` folder:
```bash
python3 -m venv venv
./venv/bin/python3 -m pip install --upgrade pip
./venv/bin/python3 -m pip install -r requirements.txt
```

### Step 2: Create logging system
The code uses Python `logging` to save training messages in `ml.log`.
It writes the epoch, loss, and accuracy values each step.

### Step 3: Train a simple ML model
The code simulates training for 5 epochs.
This keeps the lab simple and fast.

### Step 4: Log metrics (loss & accuracy)
For each epoch the app logs:
- epoch number
- loss value
- accuracy value

These values are also written to TensorBoard logs.

### Step 5: Use TensorBoard for visualization
TensorBoard reads the `logs/` folder and shows charts.
Use the browser at:
```bash
http://localhost:6006
```

### Step 6: Simple Prometheus monitoring
The app starts a Prometheus endpoint at:
```bash
http://localhost:8000
```
It tracks:
- request count
- accuracy value

## 8. Sample Code (FULL PROGRAM)
Use the full code in `app.py`.

```python
import logging
import os
import random
import time
from prometheus_client import start_http_server, Counter, Gauge
import tensorflow as tf

# Logging
logging.basicConfig(filename='ml.log', level=logging.INFO)

# TensorBoard
os.makedirs('logs', exist_ok=True)
writer = tf.summary.create_file_writer('logs')

# Prometheus
req = Counter('requests', 'Total steps')
acc_metric = Gauge('accuracy', 'Accuracy')

def train():
    for e in range(1, 6):
        loss = 1.0 / e
        acc = 0.5 + 0.1 * e

        logging.info(f"Epoch {e}: loss={loss:.2f}, acc={acc:.2f}")

        with writer.as_default():
            tf.summary.scalar('loss', loss, step=e)
            tf.summary.scalar('accuracy', acc, step=e)

        req.inc()
        acc_metric.set(acc)

        print(f"Epoch {e}: loss={loss:.2f}, acc={acc:.2f}")
        time.sleep(1)

start_http_server(8000)
print('Prometheus: http://localhost:8000')
print('TensorBoard: http://localhost:6006 (run: tensorboard --logdir=logs)')

train()
```

## 9. Commands Section
Install dependencies in the EX8 virtual environment:
```bash
cd "/Users/joeltharakan/Downloads/MLOPS LAB/EX8"
python3 -m venv venv
./venv/bin/python3 -m pip install --upgrade pip
./venv/bin/python3 -m pip install -r requirements.txt
```

Run the app:
```bash
./venv/bin/python3 app.py
```

Open TensorBoard in the browser:
```bash
http://localhost:6006
```

If `pip` or `python` is not found, use `python3` or the virtual environment commands above.

## 10. Output
Expected output:
- A file named `ml.log` is created.
- TensorBoard logs stored in `logs/`.
- Prometheus metrics available at `http://localhost:8000`.

## 11. Answer Questions Clearly
**Q1: Logging script explanation**
- The script runs 5 epochs.
- Each epoch logs: epoch, loss, accuracy.
- The log file saves these values for review.

**Q2: Monitoring system**
- Logging saves details to a file.
- TensorBoard shows charts from `logs/`.
- Prometheus exposes metrics at `http://localhost:8000`.

## 12. Advantages
- Helps debugging.
- Tracks performance.
- Detects issues early.

## 13. Conclusion
This lab shows how logging and monitoring help with machine learning.
It makes ML programs easier to understand and fix in real life.
