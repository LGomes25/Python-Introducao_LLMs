from src.config import get_langchain_model
from rich import print


def main():

    chat = get_langchain_model()

    # Geração convencional (espera tudo ficar pronto)
    print("\nGeração convencional.")

    resposta = chat.invoke("Conte uma piada sobre tomates em uma frase")
    print(resposta.content)

    print("\nFim da Geração convencional.")
    print("---" * 30)

    # Geração convencional (espera tudo ficar pronto)
    print("\nGeração com Streaming.")

    for bloco in chat.stream("me conte uma piada sobre ovelhas"):
        print(bloco.content, end="", flush=True)

    print("\nFim da Geração convencional com Streaming.")


if __name__ == "__main__":
    main()
