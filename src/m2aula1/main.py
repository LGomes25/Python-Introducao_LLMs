from src.config import MODEL_NAME, get_openai_client
from rich import print


def main():
    print("\nIniciando conexão com 'OpenAI'.")

    llm = get_openai_client()

    chat = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "Você é uma bactéria."},
            {"role": "user", "content": "Explique sua história de vida em uma frase."},
        ],
        temperature=0.2,
        stream=False,
    )
    print(chat.choices[0].message.content)

    print("\nTermino de conexão.")


if __name__ == "__main__":
    main()
