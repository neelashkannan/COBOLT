# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Install and start Ollama (assuming it's necessary before running your app)
RUN curl -s https://ollama.ai/install.sh | sh

# Run app.py when the container launches
CMD ["sh", "-c", "ollama serve & streamlit run test.py"]
