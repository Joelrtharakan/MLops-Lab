# Use a small Python image
FROM python:3.10-slim

# Set the working folder inside the container
WORKDIR /app

# Copy files from our computer into the container
COPY requirements.txt .
COPY ML.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python file when the container starts
CMD ["python", "ML.py"]
