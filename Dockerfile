FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -s https://ollama.ai/install.sh | sh

#RUN pip install mesop

EXPOSE 8501


CMD ["sh", "-c", "ollama serve & sleep 10 && ollama create demo1 -f Modelfile & sleep 30 && ollama create demo2 -f Modelfile2 & sleep 100 && streamlit run test.py"]
