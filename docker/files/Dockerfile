# Basic Dockerfile (Python example)
# Edit this file to suit your project's runtime and build needs.

FROM python:3.11-slim

WORKDIR /app

# Install build requirements if present
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy application source
COPY . /app

# Default command — change to your app entrypoint
CMD ["python", "app.py"]
