ollama serve &
sleep 5

ollama pull tinyllama &

sleep 10

ollama pull llava &

sleep 50
streamlit run test.py 
