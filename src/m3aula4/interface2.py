import streamlit as st
import fitz
import io
from langchain_core.documents import Document
from langchain_core.messages import AIMessage, HumanMessage
from chatbot import app, State


def main():
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
        file_bytes = uploaded_file.read()
        with fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf") as doc:
            pdf_text = "\n".join([str(page.get_text("text")) for page in doc])

    # Entrada do usuário
    user_input = st.chat_input("Digite aqui...")

    if user_input:
        st.session_state["message_history"].append(HumanMessage(content=user_input))

    # Renderiza histórico sempre (inclusive boas-vindas e mensagens anteriores)
    for msg in st.session_state["message_history"]:
        role = "assistant" if isinstance(msg, AIMessage) else "user"
        with st.chat_message(role):
            st.markdown(msg.content)

    # Se houver nova entrada, processa e mostra em tempo real
    if user_input:

        # Caixa para streaming da nova resposta
        msg_box = st.chat_message("assistant")

        state: State = {
            "pergunta": user_input,
            "contexto": [Document(page_content=pdf_text, metadata={})],
            "resposta": "",
        }
        response_stream = app.invoke(state)["resposta"]

        full_response = ""
        for chunk in msg_box.write_stream(response_stream):
            full_response += chunk

        # Depois que terminar o streaming, adiciona ao histórico
        st.session_state["message_history"].append(AIMessage(content=full_response))


if __name__ == "__main__":
    main()
