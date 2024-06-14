import os
import streamlit as st
import ollama

# Constants
UPLOAD_DIR = "uploads"
PAGE_CONFIG = {"page_title": "Robonium", "layout": "wide"}
MODEL_OPTIONS = ["Baby Cobolt", "Teenage Cobolt"]
MODEL_NAMES = {"Baby Cobolt": "demo", "Teenage Cobolt": "test"}

# Set page configuration
st.set_page_config(**PAGE_CONFIG)

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Hide Streamlit's default UI elements
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Layout the title and model selection in columns
col1, col2 = st.columns(2)
with col1:
    st.title("C.O.B.O.L.T - By Robonium")
with col2:
    model_selection = st.selectbox("Choose the model", options=MODEL_OPTIONS)

# Determine the model name based on the selection
model_name = MODEL_NAMES.get(model_selection)

# Initialize chat history
st.session_state.setdefault("messages", [])

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(' '.join(message["content"].split('\n')), unsafe_allow_html=True)

# React to user input
if model_name:
    uploaded_file = st.file_uploader("Upload your image here")
    image_bytes = None
    if uploaded_file is not None:
        # Save the uploaded file to the specified directory
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        with open(file_path, 'rb') as f:
            image_bytes = f.read()

    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(' '.join(prompt.split('\n')), unsafe_allow_html=True)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate the response from the selected model
        messages = [{'role': 'user', 'content': 'Describe this image:', 'images': [image_bytes]}] if image_bytes else [{'role': 'user', 'content': prompt}]
        stream = ollama.chat(model=model_name, messages=messages, stream=True)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response_text = st.empty()  # placeholder for the text
            full_response = ""
            for chunk in stream:
                full_response += chunk['message']['content']  # concatenate each chunk to the existing text
                response_text.markdown(f"<p style='word-wrap: break-word;'>{full_response}</p>", unsafe_allow_html=True)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
