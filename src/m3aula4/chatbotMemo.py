from src.config import get_langchain_model
from typing import TypedDict, List
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph


# Inicializa modelo de linguagem
llm = get_langchain_model()


# Estado da aplicação
class State(TypedDict):
    pergunta: str
    contexto: List[Document]
    historico: str
    resposta: str


# Função de resposta
def generate(state: State) -> dict:
    # Limita tamanho do arquivo
    max_chars = 2000

    # Cria o contexto referenciando o arquivo carregado e concatenado
    docsInfo_content = "\n\n".join(doc.page_content for doc in state["contexto"])
    docsInfo_content = docsInfo_content[:max_chars]

    # Guardar a pergunta em uma variável
    pergunta = state["pergunta"]
    historico = state.get("historico", "")

    # Streaming: retorna o iterador diretamente
    return {
        "resposta": llm_prompt_template.stream(
            {"pergunta": pergunta, "contexto": docsInfo_content, "historico": historico}
        )
    }


# Prompt inicial (tom de voz e instruções do assistente)
template = """
Você é um assistente amigável e proativo. Use o contexto do PDF quando existir. Mantenha a continuidade da conversa com base no histórico. Se não souber a resposta, apenas informe que não sabe.

{historico}

{contexto}

{pergunta}

Answer:
"""

# Template de chat: organiza contexto e pergunta
chat_contexto_template = ChatPromptTemplate.from_template(template)

# Pipeline: aplica template e envia ao modelo
llm_prompt_template = chat_contexto_template | llm


# Define grafo de estados da conversa
grafo = StateGraph(State)
grafo.add_node("generate", generate)
grafo.set_entry_point("generate")
grafo.set_finish_point("generate")

# Compila aplicação para uso no frontend (Streamlit)
app = grafo.compile()
