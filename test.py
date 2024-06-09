import streamlit as st
import ollama
#ollama.pull("example")
st.set_page_config(
    page_title="Robonium",
    layout="wide"
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.title("C.O.B.O.L.T - By Robonium")
with col2:
    a = st.selectbox("Choose the model", options=["Baby Cobolt","Teenage Cobolt"])
    

if a == "Baby Cobolt":
    manme = "demo1"
elif a == "Teenage Cobolt":
    m = "llama3"
    manme = "demo2"



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(' '.join(message["content"].split('\n')), unsafe_allow_html=True)

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(' '.join(prompt.split('\n')), unsafe_allow_html=True)
        stream = ollama.chat(
            model=mname,
            messages=[{'role': 'user', 'content': ' '.join(prompt.split('\n'))}],
            stream=True,
        )
    # Add user message to chat history
    st.session_state.messages.append({"role": "robot", "content": ' '.join(prompt.split('\n'))})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response_text = st.empty()  # placeholder for the text
        full_response = ""
        for chunk in stream:
            full_response += chunk['message']['content']  # concatenate each chunk to the existing text
            response_text.markdown(f"<p style='word-wrap: break-word;'>{full_response}</p>", unsafe_allow_html=True)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": f"<p style='word-wrap: break-word;'>{full_response}</p>"})
