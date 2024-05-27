import ollama
import streamlit as st

# Initialize the Ollama model
#model = ollama.load_model('llama3')

# Streamlit app title
st.title("Streamlit Chatbot Interface")

# Function to handle sending messages and receiving responses
def send_message(message):
    stream = ollama.chat(
        model='example',
        messages=[{'role': 'user', 'content': message}],
        stream=True,
    )
    # Iterate through the stream and concatenate the content
    response = ''.join(chunk['message']['content'] for chunk in stream)
    return response

# Chat interface
st.title('Chat with AI')
user_input = st.text_input("Type your message here:")
if st.button('Send'):
    stream = ollama.chat(
        model='example',
        messages=[{'role': 'user', 'content': user_input}],
        stream=True,
    )
    # Process the input and get the response from the model
    #response = send_message(user_input)
    # Display the response
    for chunk in stream:
        st.write(chunk['message']['content'], end='', flush=True)
