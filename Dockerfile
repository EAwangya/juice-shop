FROM python:3

WORKDIR /app

# Copy requirements.txt into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Run the Python script
CMD ["python", "./upload-reports.py"]
