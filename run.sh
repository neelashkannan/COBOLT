ollama serve &
sleep 5
mesop ./test.py --port 32123 &
sleep 10
ollama create demo2 -f Modelfile2
