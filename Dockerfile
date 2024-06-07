# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama (if required)
RUN curl -s https://ollama.ai/install.sh | sh

# Expose the port the app runs on
EXPOSE 8501

# Default command
CMD ["streamlit", "run", "test.py"]
