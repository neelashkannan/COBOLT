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
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)





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
    model_selection = st.selectbox("Choose the model", options=["Baby Cobolt", "Teenage Cobolt"])

# Determine the model name based on the selection
model_name = None
if model_selection == "Baby Cobolt":
    model_name = "demo"
elif model_selection == "Teenage Cobolt":
    model_name = "test"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(' '.join(message["content"].split('\n')), unsafe_allow_html=True)

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

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
    if model_selection == "Teenage Cobolt":
        uploaded_file = st.file_uploader("Upload your image here")
        if uploaded_file is not None:
    # Get the incremental filename
            incremental_filename = get_incremental_filename(UPLOAD_DIR, uploaded_file.name)
            file_path = os.path.join(UPLOAD_DIR, incremental_filename)
    
    # Save the uploaded file to the specified directory
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            with open('/app/uploads/' + incremental_filename, 'rb') as f:
                image_bytes = f.read()

    if prompt := st.chat_input("What is up?"):
        count = 0
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(' '.join(prompt.split('\n')), unsafe_allow_html=True)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate the response from the selected model
        if(model_name == "test") and uploaded_file is not None:
          
            stream = ollama.chat(
            model='demo2',  # replace 'llava' with your model name
             messages=[
            {
            'role': 'user',
            'content': 'Describe this image:',
            'images': [image_bytes],
            },
            ],
            stream=True,  # Enable response streaming
            )
            with st.chat_message("assistant"):
                response_text = st.empty()  # placeholder for the text
                full_response = ""
                if full_response =="" and count == 0:
                    st.warning("generating")
                    count = count +1
                   
                for chunk in stream:
                    count = 0
                    full_response += chunk['message']['content']  # concatenate each chunk to the existing text
                    response_text.markdown(f"<p style='word-wrap: break-word;'>{full_response}</p>", unsafe_allow_html=True)

        elif(model_name == "test"):
            stream = ollama.chat(
            model='demo2',  # replace 'llava' with your model name
             messages=[
            {
            'role': 'user',
            'content': 'Describe this image:',
            },
            ],
            stream=True,  # Enable response streaming
            )
            with st.chat_message("assistant"):
                response_text = st.empty()  # placeholder for the text
                full_response = ""
                for chunk in stream:
                    full_response += chunk['message']['content']  # concatenate each chunk to the existing text
                    response_text.markdown(f"<p style='word-wrap: break-word;'>{full_response}</p>", unsafe_allow_html=True)
        else:
            stream = ollama.chat(
            model='demo1',
            messages=[{'role': 'user', 'content': prompt }],
            stream=True,
        )
            with st.chat_message("assistant"):
                response_text = st.empty()  # placeholder for the text
                full_response = ""
                for chunk in stream:
                    full_response += chunk['message']['content']  # concatenate each chunk to the existing text
                    response_text.markdown(f"<p style='word-wrap: break-word;'>{full_response}</p>", unsafe_allow_html=True)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
