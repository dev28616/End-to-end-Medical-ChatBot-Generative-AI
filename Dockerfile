# Use a lightweight Python base image
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Set environment variables (optional for dev)
ENV PYTHONUNBUFFERED=1

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
