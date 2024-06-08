# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Copy only the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Ollama (if required)
RUN curl -s https://ollama.ai/install.sh | sh

# Expose the port the app runs on
EXPOSE 8501

# Default command to run the app
CMD ["sh", "-c", "ollama serve && ollama pull tinyllama && streamlit run test.py"]
