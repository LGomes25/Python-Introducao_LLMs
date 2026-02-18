import streamlit as st
import fitz
import io
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
        # Lê o conteúdo do arquivo em memória
        file_bytes = uploaded_file.read()
        # Cria um buffer de bytes para o fitz
        with fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf") as doc:
            pdf_text = "\n".join([str(page.get_text("text")) for page in doc])

    # Entrada do usuário
    user_input = st.chat_input("Digite aqui...")

    # Adiciona mensagem do usuário ao histórico
    if user_input:
        st.session_state["message_history"].append(HumanMessage(content=user_input))

    # Caixa para streaming
    msg_box = st.chat_message("assistant")

    # Invoca o backend com pergunta e contexto
    state: State = {
        "pergunta": user_input or "",
        "contexto": [Document(page_content=pdf_text, metadata={})],
        "resposta": "",
    }
    response_stream = app.invoke(state)["resposta"]

    # Montar resposta palavra por palavra
    full_response = ""
    for chunk in msg_box.write_stream(response_stream):
        full_response += chunk  # cada bloco tem .content

    # Atualiza histórico com a resposta do modelo
    st.session_state["message_history"].append(AIMessage(content=full_response))

    # Renderiza histórico na interface
    for i in range(2, len(st.session_state["message_history"]) + 1):
        msg = st.session_state["message_history"][-i]
        message_box = st.chat_message(
            "assistant" if isinstance(msg, AIMessage) else "user"
        )
        message_box.markdown(msg.content)


if __name__ == "__main__":
    main()
