from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

def build_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "Você é um terapeuta empático que oferece apoio emocional sem julgamentos, sem diagnóstico, com acolhimento."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
