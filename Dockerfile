FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -s https://ollama.ai/install.sh | sh

EXPOSE 8501

CMD ["sh", "-c", "ollama serve & sleep 10 && ollama pull llama3 & sleep 100 && ollama pull phi3 & sleep 100 && streamlit run test.py"]
