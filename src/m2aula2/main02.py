from src.config import get_langchain_model
from rich import print
from langchain_core.prompts import ChatPromptTemplate


def main():
    llm = get_langchain_model()

    # Leitura da entrada de dados e armazenamento em variáveis
    idiomaEntrada = input("\nQual seu idioma?\n")
    idiomaSaida = input("\nPara qual idioma deve ser traduzido o texto?\n")
    texto = input("\nDigite o texto: ")

    # Definição da mensagem de sistema com placeholders
    system_message = "Faça a tradução idioma {idiomaEntrada} da frase do usuário para o idioma {idioma}"
    user_message = "{texto}"

    # Criação do template com mensagens de sistema e usuário
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("user", user_message),
        ]
    )

    # Envio das variáveis para o template
    prompt = prompt_template.invoke(
        (
            {
                "idioma": idiomaSaida,
                "idiomaEntrada": idiomaEntrada,
                "texto": texto,
            }
        )
    )

    # Chamada a llm
    response = llm.invoke(prompt)
    print("\nResposta do modelo:\n")
    print(response.content)


if __name__ == "__main__":
    main()
