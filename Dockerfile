FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -s https://ollama.ai/install.sh | sh

RUN pip install mesop

EXPOSE 32123

CMD ["sh", "run.sh"]
