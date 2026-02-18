from src.config import get_langchain_model
from rich import print
from langchain_community.document_loaders import PyPDFLoader


def main():
    # Carregar o PDF
    loader = PyPDFLoader("data/bikes.pdf")
    paginas = loader.load()

    # Número de páginas
    print("\nNúmero de páginas:", len(paginas))

    # Mostrar metadados da primeira página
    print("\nMetadados da primeira página:", paginas[0].metadata)

    # Mostrar tamanho de cada página (em caracteres)
    for i, doc in enumerate(paginas, start=1):
        print(f"Página {i} → {len(doc.page_content)} caracteres")

    # Concatenar todo o texto e mostrar tamanho total
    texto_total = "\n\n".join([doc.page_content for doc in paginas])
    print("\nTamanho total do texto:", len(texto_total), "caracteres")

    # Exemplo: mostrar início da primeira página
    print("\nInício da primeira página:\n", paginas[0].page_content[:300], "...")

    # Concatenar todo o texto e mostrar na tela
    text = "\n\n".join([doc.page_content for doc in paginas])
    print(text)


if __name__ == "__main__":
    main()
