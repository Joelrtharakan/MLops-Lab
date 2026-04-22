import logging, time
from prometheus_client import start_http_server, Counter, Gauge
import tensorflow as tf

# Logging
logging.basicConfig(filename='ml.log', level=logging.INFO)

# TensorBoard
writer = tf.summary.create_file_writer('logs')

# Prometheus
req = Counter('requests', 'Total steps')
acc_metric = Gauge('accuracy', 'Accuracy')

def train():
    for e in range(1, 6):
        loss = 1/e
        acc = 0.5 + 0.1*e

        logging.info(f"Epoch {e}: loss={loss:.2f}, acc={acc:.2f}")

        with writer.as_default():
            tf.summary.scalar('loss', loss, step=e)
            tf.summary.scalar('accuracy', acc, step=e)

        req.inc()
        acc_metric.set(acc)

        print(f"Epoch {e}: loss={loss:.2f}, acc={acc:.2f}")
        time.sleep(1)

start_http_server(8000)
print("Prometheus: http://localhost:8000")
print("TensorBoard: http://localhost:6006 (run: tensorboard --logdir=logs)")

train()