# Use a small Python image
FROM python:3.10-slim

# Set work directory inside the container
WORKDIR /app

# Copy dependency file and install packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY serve.py .
COPY iris.joblib .

# Run the Flask server
CMD ["python", "serve.py"]
