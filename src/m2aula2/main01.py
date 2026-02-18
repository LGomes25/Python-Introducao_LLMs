from src.config import get_langchain_model
from rich import print
from langchain_core.messages import HumanMessage, SystemMessage


def main():
    llm = get_langchain_model()

    messages = [
        SystemMessage(
            content="Apenas traduza o seguinte texto de Inglês para Portugues."
        ),
        HumanMessage(content="Hi!How are you fat man?"),
    ]

    response = llm.invoke(messages)
    print("\nResposta do modelo:\n")
    print(response.content)


if __name__ == "__main__":
    main()
