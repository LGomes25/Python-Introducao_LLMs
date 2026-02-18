import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from chatbot import app


def main():

    # Configuração da página e título
    st.set_page_config(
        layout="wide", page_title="Chatbot de loja de bicicletas", page_icon="🚴"
    )
    st.title("Loja de Bicicletas - Assistente Virtual")

    # Inicializa histórico de mensagens
    if "message_history" not in st.session_state:
        st.session_state["message_history"] = [
            AIMessage(
                content="Olá! 🚴 Sou seu assistente virtual da loja de bicicletas. Como posso te ajudar?"
            )
        ]

    # Entrada do usuário
    user_input = st.chat_input("Digite aqui...")

    # Adiciona mensagem do usuário ao histórico
    if user_input:
        st.session_state["message_history"].append(HumanMessage(content=user_input))

    # Invoca o backend com o histórico
    response = app.invoke({"messages": st.session_state["message_history"]})

    # Atualiza histórico com a resposta do modelo
    st.session_state["message_history"] = response["messages"]

    # Renderiza histórico na interface
    for msg in st.session_state["message_history"]:
        role = "assistant" if isinstance(msg, AIMessage) else "user"
        with st.chat_message(role):
            st.markdown(msg.content)


if __name__ == "__main__":
    main()
