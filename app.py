import os
import streamlit as st
from config import PROVIDER, API_KEY, API_BASE, MODEL_NAME
from prompt_template import build_prompt
from memory_module import get_memory
from guardrails import check_guardrails
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# Configura UI
st.set_page_config(page_title="Chatbot Terapêutico", page_icon="💬")
st.title("💬 Chatbot Terapêutico (GPT / Groq)")

# Inicializa o LLM usando OpenAI connector (compatível com OpenAI e Groq)
llm = ChatOpenAI(
    openai_api_key=API_KEY,
    openai_api_base=API_BASE,
    model_name=MODEL_NAME,
    temperature=0.7,
    verbose=False,
)

# Monta a cadeia de conversação
memory = get_memory()
prompt = build_prompt()
chain = ConversationChain(llm=llm, memory=memory, prompt=prompt)

# Inicializa histórico
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Exibe histórico
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Entrada do usuário
user_input = st.chat_input("Como você está se sentindo hoje?")
if user_input:
    st.session_state.messages.append({ 'role': 'user', 'content': user_input })
    with st.chat_message('user'):
        st.markdown(user_input)

    # Verifica guardrails
    blocked = check_guardrails(user_input)
    if blocked:
        response = blocked
    else:
        response = chain.predict(input=user_input)

    st.session_state.messages.append({ 'role': 'assistant', 'content': response })
    with st.chat_message('assistant'):
        st.markdown(response)