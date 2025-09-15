# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy calculator code into container
COPY calculator.py .

# Run the calculator program
CMD ["python", "calculator.py"]
