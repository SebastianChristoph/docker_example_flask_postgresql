# Base image
FROM python:3.9-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flask-App kopieren
COPY app/ .

# Flask starten
CMD ["python", "app.py"]
