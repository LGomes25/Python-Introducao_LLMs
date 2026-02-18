import uuid
from src.config import get_langchain_model
from rich import print
from rich.markdown import Markdown
from typing import Dict, cast
from langchain_core.messages import HumanMessage, BaseMessage, AnyMessage
from langgraph.graph import START, END, MessagesState, StateGraph
from langgraph.graph.state import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver


def main():
    llm = get_langchain_model()

    # Definir o grafo de estados (StateGraph) que coordena o fluxo de mensagens
    builder = StateGraph(state_schema=MessagesState)

    # Como chamar o modelo com as mensagens
    def call_llm(state: MessagesState) -> Dict[str, list[BaseMessage]]:
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    # Definir nós e arestas
    builder.add_node("llm", call_llm)
    builder.add_edge(START, "llm")
    builder.add_edge("llm", END)

    # Configuração do checkpointer de memória (MemorySaver)
    app = builder.compile(checkpointer=MemorySaver())

    # Criação de identificador único (thread_id) para sequenciar a conversa
    thread_id = str(uuid.uuid4())
    config = RunnableConfig(configurable={"thread_id": thread_id})

    # Iteração 1
    # Entrada de usuário + armazenamento + chamada a llm + resposta
    human_message = input("\nUser message 1: ")
    input_message = cast(list[AnyMessage], [HumanMessage(human_message)])
    state = MessagesState(messages=input_message)
    response = app.invoke(state, config=config)
    response["messages"][-1].pretty_print()

    # Iteração 2
    # Entrada de usuário + armazenamento + chamada a llm + resposta
    human_message = input("\nUser message 2: ")
    input_message = cast(list[AnyMessage], [HumanMessage(human_message)])
    state = MessagesState(messages=input_message)
    response = app.invoke(state, config=config)
    response["messages"][-1].pretty_print()

    # Iteração 3
    # Entrada de usuário + armazenamento + chamada a llm + resposta
    human_message = input("\nUser message 3: ")
    input_message = cast(list[AnyMessage], [HumanMessage(human_message)])
    state = MessagesState(messages=input_message)
    response = app.invoke(state, config=config)
    response["messages"][-1].pretty_print()


if __name__ == "__main__":
    main()
