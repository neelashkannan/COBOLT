# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

COPY . .

RUN curl -s https://ollama.ai/install.sh | sh


RUN pip install --no-cache-dir -r requirements.txt




# Make port 8501 available to the world outside this container
EXPOSE 8501



# Run ollama serve when the container launches
CMD ["sh", "-c", "ollama serve & sleep 5 && ollama create demo1 -f Modelfile & sleep 10 && ollama create demo2 -f Modelfile2 & sleep 10 && streamlit run test.py"]
