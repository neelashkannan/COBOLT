FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -s https://ollama.ai/install.sh | sh

RUN pip install mesop

EXPOSE 32123

CMD ["sh", "-c", "ollama serve & sleep 5 && ollama create demo2 -f Modelfile2 & sleep 10 && mesop .\test.py --port 32123"]
