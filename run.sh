ollama serve &
sleep 5

ollama create demo1 -f Modelfile &

sleep 10

ollama create demo2 -f Modelfile2 &

sleep 10

ollama create demo3 -f Modelfile3 &

sleep 5
streamlit run test.py 
