# Use official Python image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run Flask using Gunicorn (production mode)

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

