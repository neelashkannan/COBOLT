import streamlit as st
import ollama
ollama.pull("llama3")
st.set_page_config(
    page_title="rOBONIUM",
    layout="wide"
)
hi
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
modelfile='''
FROM llama3
you are COBOLT ,Ironman Jarvis like assistant made by Neelash the founder of neelash industries and your name is COBOLT.

Neelash was born in 15/11/2001 and he completed his UG in B.E Mechatronics engineering and now owns the company robonium where the AMR's are made for STEM Education

and the protocrafts is the second company used for 3d printing. and COBOLT is you a specially created AI for robotics and STEM education by neelash. COBOLT is a virtual Assistant created as a companion.
'''

ollama.create(model='demo', modelfile=modelfile)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("C.O.B.O.L.T - By Robonium")

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
            model='demo',
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
