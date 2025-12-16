FROM python:3.12-slim

# ------------------------------------------------------------------
# Python & runtime behavior
# ------------------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ------------------------------------------------------------------
# System dependencies (GeoDjango + Postgres)
# ------------------------------------------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    gdal-bin \
    libgdal-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# GDAL is required by GeoDjango
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy backend source
COPY . .

# Django internal port
EXPOSE 8000
