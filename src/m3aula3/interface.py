import streamlit as st
from langchain_core.documents import Document
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import PyMuPDFLoader
from chatbot import app, State


def main():

    # Configuração da página e título
    st.set_page_config(
        layout="wide", page_title="Chatbot de loja de bicicletas", page_icon="🚴"
    )
    st.title("Loja de Bicicletas - Assistente Virtual")

    # Inicializa histórico com mensagem de boas-vindas
    if "message_history" not in st.session_state:
        st.session_state["message_history"] = [
            AIMessage(
                content="Olá! 🚴 Sou seu assistente virtual da loja de bicicletas. Como posso ajudar você com bicicletas? Envie um PDF ou pergunte algo!"
            )
        ]

    # Upload e leitura de arquivo PDF
    uploaded_file = st.file_uploader(
        "Faça o upload de um PDF para análise", type=["pdf"]
    )
    pdf_text = ""

    if uploaded_file is not None:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        loader = PyMuPDFLoader("temp.pdf")
        docs = loader.load()
        pdf_text = "\n\n".join(doc.page_content for doc in docs)

    # Entrada do usuário
    user_input = st.chat_input("Digite aqui...")

    # Adiciona mensagem do usuário ao histórico
    if user_input:
        st.session_state["message_history"].append(HumanMessage(content=user_input))

    # Invoca o backend com pergunta e contexto
    state: State = {
        "pergunta": user_input or "",
        "contexto": [Document(page_content=pdf_text, metadata={})],
        "resposta": "",
    }
    response = app.invoke(state)

    # Atualiza histórico com a resposta do modelo
    st.session_state["message_history"].append(AIMessage(content=response["resposta"]))

    # Renderiza histórico na interface
    for msg in st.session_state["message_history"]:
        role = "assistant" if isinstance(msg, AIMessage) else "user"
        with st.chat_message(role):
            st.markdown(msg.content)


if __name__ == "__main__":
    main()
