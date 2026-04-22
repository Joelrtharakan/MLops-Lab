# Monitoring and Logging in Machine Learning with Python

## 1. Title
Monitoring and Logging in Machine Learning with Python

## 2. Objective
Learn how to track a simple ML training loop using logging, TensorBoard, and Prometheus.

## 3. Job Role
Machine Learning Engineer / Data Science student

## 4. Skills Required
- Basic Python: write and run a simple program
- Logging: save training messages to a file
- Monitoring: collect values and expose them
- TensorBoard: view charts from logs
- Prometheus: expose metrics through a web endpoint

## 5. Prerequisites
- Python 3 installed
- A terminal or command line
- Basic knowledge of running Python code

## 6. Theory
- Logging is saving messages about how the program runs.
- Monitoring is making values available so they can be watched live.
- Logging is like writing notes in a diary.
- Monitoring is like watching a meter or dashboard.
- TensorBoard can visualize loss and accuracy from log files.
- Prometheus can expose numeric metrics at an HTTP address.

## 7. Project Structure

EX8/
│
├── app.py
├── requirements.txt
└── venv/

## 8. Implementation

### Step 1: Install libraries
In the `EX8` folder run:
```bash
python3 -m venv venv
./venv/bin/python3 -m pip install --upgrade pip
./venv/bin/python3 -m pip install -r requirements.txt
```

### Step 2: Create logging system
- Use Python `logging` to write messages to `ml.log`.
- The script logs epoch, loss, and accuracy values.

### Step 3: Create TensorBoard logs
- Use TensorFlow summaries to write logs to `logs/`.
- These logs can be viewed in TensorBoard.

### Step 4: Create Prometheus metrics
- Use `prometheus_client` to start an HTTP metrics server.
- Expose metrics like request count and accuracy.

### Step 5: Run the app
- The app simulates 5 training epochs.
- Each epoch updates the log file, TensorBoard logs, and Prometheus metrics.

## 9. Implementation Code

```python
import logging
import os
import time
from prometheus_client import start_http_server, Counter, Gauge
import tensorflow as tf

# Logging
logging.basicConfig(filename='ml.log', level=logging.INFO)

# TensorBoard
os.makedirs('logs', exist_ok=True)
writer = tf.summary.create_file_writer('logs')

# Prometheus metrics
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

## 10. Commands Section

Install dependencies:
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

Open TensorBoard:
```bash
http://localhost:6006
```

Open Prometheus metrics:
```bash
http://localhost:8000
```

## 11. Output
- A file named `ml.log` is created.
- TensorBoard logs are written to `logs/`.
- Prometheus metrics are available at `http://localhost:8000`.
- The terminal prints epoch loss and accuracy values.

## 12. Explanation
- Logging saves step-by-step information to `ml.log`.
- TensorBoard reads the `logs/` folder and shows charts.
- Prometheus exposes metrics on a web endpoint.
- This setup helps track model training and monitor metrics.

## 13. Advantages
- Makes code behavior visible.
- Helps debug training loops.
- Lets you monitor progress in real time.
- Useful in real ML projects to watch model health.

## 14. Exam Tips
- Know the difference between logging and monitoring.
- Know how to open TensorBoard and Prometheus.
- Know the commands to install dependencies and run the app.

## 15. Conclusion
This lab shows how to use logging and monitoring in Python. It makes it easier to understand what happens during model training.
