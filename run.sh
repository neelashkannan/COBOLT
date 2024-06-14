ollama serve &
sleep 5

ollama create demo2 -f Modelfile2 &

sleep 10
streamlit run test.py 
