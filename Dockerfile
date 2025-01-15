# Base image
FROM python:3.9-slim

# Create working directory
WORKDIR /app

# install dependencies
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy Flask app
COPY app/ .

# start flask app
CMD ["python", "app.py"]
