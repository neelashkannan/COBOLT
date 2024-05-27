import streamlit as st
import ollama


st.title("Echo Bot")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages =[]
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message( message["role"]):
        st.markdown (message["content"])
# React to user input
if prompt := st.chat_input("What is up?"):
     # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown (prompt)
        stream = ollama.chat(
    model='example',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)
     # Add user message to chat history
    st.session_state.messages.append({"role": "robot", "content": prompt})
    
    response = f"Echo: {prompt}"
     # Display assistant response in chat message container
    with st. chat_message("assistant"):
        for chunk in stream:
            st.markdown (chunk['message']['content'])
    # Add assistant response to chat history
            st.session_state.messages.append ({"role": "assistant", "content": chunk['message']['content']})

