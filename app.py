import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

from prompt_template import build_prompt
from memory_module import get_memory
from guardrails import check_guardrails
from config import API_KEY, API_BASE, MODEL_NAME

st.set_page_config(page_title="Chatbot Terapêutico", page_icon="💬")
st.title("💬 Chatbot Terapêutico (GPT / Groq)")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chain = None

if st.session_state.chain is None:
    llm = ChatOpenAI(
        openai_api_key=API_KEY,
        openai_api_base=API_BASE,
        model_name=MODEL_NAME,
        temperature=0.7
    )
    memory = get_memory()
    prompt = build_prompt()

    st.session_state.chain = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=False
    )

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Como você está se sentindo hoje?")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    blocked = check_guardrails(user_input)
    if blocked:
        bot_response = blocked
    else:
        bot_response = st.session_state.chain.predict(input=user_input)

    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
