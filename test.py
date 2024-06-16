import streamlit as st
import ollama
import os

# Set page configuration
st.set_page_config(
    page_title="Robonium",
    layout="wide"
)

UPLOAD_DIR = "uploads"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Hide Streamlit's default UI elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Layout the title and model selection in columns
col1, col2 = st.columns(2)
with col1:
    st.title("C.O.B.O.L.T - By Robonium")
with col2:
    model_selection = st.selectbox("Choose the model", options=["Baby Cobolt", "Teenage Cobolt","Cobolt Vision"])

# Determine the model name based on the selection
if model_selection == "Baby Cobolt":
    model_name = "demo1" 
elif model_selection == "Teenage Cobolt":
    model_name = "demo2"
elif model_selection == "Cobolt Vision":
    model_name = "demo3"
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(' '.join(message["content"].split('\n')), unsafe_allow_html=True)

def get_incremental_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = f"{counter}{extension}"
    while os.path.exists(os.path.join(directory, new_filename)):
        counter += 1
        new_filename = f"{counter}{extension}"
    return new_filename

# React to user input
if model_name:
    uploaded_file = st.file_uploader("Upload your image here") if model_selection == "Cobolt Vision" else None
    image_bytes = None

    if uploaded_file:
        incremental_filename = get_incremental_filename(UPLOAD_DIR, uploaded_file.name)
        file_path = os.path.join(UPLOAD_DIR, incremental_filename)
        
        # Save the uploaded file to the specified directory
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        with open(file_path, "rb") as f:
            image_bytes = f.read()

    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(' '.join(prompt.split('\n')), unsafe_allow_html=True)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate the response from the selected model
        if model_name == "demo3":
            if uploaded_file:
                stream = ollama.chat(
                    model='demo3',  # replace 'llava' with your model name
                    messages=[{'role': 'user', 'content': prompt, 'images': [image_bytes]}],
                    stream=True
                )
            else:
                stream = ollama.chat(
                    model='demo2',  # replace 'llava' with your model name
                    messages=[{'role': 'user', 'content': prompt}],
                    stream=True
                )
        elif model_name == "demo2" :
            stream = ollama.chat(
                model='demo2',
                messages=[{'role': 'user', 'content': prompt}],
                stream=True
            )
        else:
            stream = ollama.chat(
                model='demo1',
                messages=[{'role': 'user', 'content': prompt}],
                stream=True
            )

        full_response = ""

        with st.chat_message("assistant"):
            response_text = st.empty()  # placeholder for the text
            progress_bar = st.progress(0) if uploaded_file else None  # initialize the progress bar if needed
            
            for i, chunk in enumerate(stream):
                full_response += chunk['message']['content']  # concatenate each chunk to the existing text
                response_text.markdown(f"<p style='word-wrap: break-word;'>{full_response}</p>", unsafe_allow_html=True)
                
                if progress_bar:
                    progress_bar.progress(min((i + 1) / 100, 1.0))  # update the progress bar

            if progress_bar:
                progress_bar.empty()  # Remove the progress bar when done

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
