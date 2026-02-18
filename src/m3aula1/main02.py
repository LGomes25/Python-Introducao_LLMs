from src.config import get_langchain_model
import streamlit as st


def main():
    llm = get_langchain_model()

    # Título da aplicação
    st.title("Chat com IA usando LangChain")

    # Entrada do usuário
    prompt = st.text_area("Digite sua Pergunta:")

    # Botão de envio
    if st.button("Enviar"):
        # só processa se houver texto, e retira os espaços em vazios...
        if prompt.strip():
            # Apresenta um spinner aguardando o processamento da llm
            with st.spinner("Pensando..."):
                # Chama a llm e passa a pergunta do usuário
                resposta = llm.invoke(prompt)
                # Reproduz a resposta na tela
                st.write("**Resposta::**", resposta.content)


if __name__ == "__main__":
    main()
