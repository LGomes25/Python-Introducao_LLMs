from src.config import get_langchain_model
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langgraph.graph import StateGraph
from typing import TypedDict, List
from rich.markdown import Markdown


# ================= Definição de tipos ==================
class State(TypedDict):
    pergunta: str
    contexto: List[Document]
    resposta: str


# ================= Função de geração ==================
# Utiliza a class State para definir as variáveis
def generate(state: State) -> dict:
    # Limita tamanho do arquivo
    max_chars = 800

    # Cria o contexto referenciando o arquivo carregado e concatenado
    docsInfo_content = "\n\n".join(doc.page_content for doc in state["contexto"])
    docsInfo_content = docsInfo_content[:max_chars]

    # Guardar a pergunta em uma variável
    pergunta = state["pergunta"]

    # Invocar a cadeia com variáveis explícitas
    response = qna_chain.invoke({"pergunta": pergunta, "contexto": docsInfo_content})

    return {"resposta": response.content}


# ================= PromptTemplate Langchain ==================
template = """
Responda a pergunta apenas com base no contexto fornecido. 
Se a pergunta não puder ser respondida com o contexto, diga que não sabe. 
Seja amigável e útil.:

{contexto}

{pergunta}

Answer:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["pergunta", "contexto"],
)

# ================= Cadeia de resposta ==================
llm = get_langchain_model()
# qna = Question and Answers
qna_chain = prompt | llm

# ================= Definição do grafo ==================
graph_builder = StateGraph(State)
graph_builder.add_node("generate", generate)
graph_builder.set_entry_point("generate")
graph_builder.set_finish_point("generate")
app = graph_builder.compile()


# ================= Função principal ==================
def main():
    loader = PyPDFLoader("data/bikes.pdf")
    docs = loader.load()
    contexto = docs
    print("\nPergunte sobre o arquivo carregado")
    count = 0
    while True:
        count += 1
        pergunta = input(f"\nPergunta {count}: ")
        if pergunta.lower() in ["q", "sair", "exit", "quit"]:
            print("Bye!")
            print(f"")
            break
        response = app.invoke(
            {
                "contexto": contexto,
                "pergunta": pergunta,
                "resposta": "",
            }
        )
        print("\nLLM: ", response["resposta"])


if __name__ == "__main__":
    main()
