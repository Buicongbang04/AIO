import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

st.title("Simple chatbox")

with st.sidebar:
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if not (email and password):
        st.warning("Email and password are required.")

    else:
        st.success("Login successful!")

if 'messages' not in st.session_state.keys():
    st.session_state['messages'] = [{"role": "assistant", "content": "How can I help you?"}]

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.write(message['content'])

def generate_response(input, email, password):
    sign = Login(email, password)
    cookies = sign.login()

    chatbot = hugchat.ChatBot(cookies.get_dict())
    return chatbot.chat(input)

if prompt := st.chat_input(disabled = not (email and password)):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message('user'):
        st.write(prompt)

if st.session_state['messages'][-1]['role'] != 'assistant':
    with st.chat_message('assistant'):
        with st.spinner("Responding..."):
            response = generate_response(prompt, email, password)
            st.write(response)
    message = {'role': "assistant", 'content': response}
    st.session_state.messages.append(message)
