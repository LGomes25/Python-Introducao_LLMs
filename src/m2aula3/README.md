### Descricao do arquivo

main01 ->
Esse código mostra como estruturar um fluxo simples de interação com uma LLM usando LangGraph. Ele cria um grafo de estados (StateGraph) que recebe mensagens do usuário, envia ao modelo (llm.invoke) e retorna a resposta, enquanto o MemorySaver garante que o histórico da conversa seja preservado entre chamadas. Assim, cada nova entrada do usuário é processada mantendo o contexto anterior, e o método pretty_print() exibe as mensagens de forma legível como um chat.

main02 ->
Baseado no código 01, este código implementa um loop interativo com LangGraph, onde cada mensagem digitada pelo usuário é enviada ao modelo e a resposta é exibida formatada. O uso de MemorySaver junto com um thread_id garante que o histórico da conversa seja preservado entre interações. O contador cont numera as mensagens, e o programa pode ser encerrado com comandos como “q”, “sair” ou “exit”.

### Para Rodar

python -m src.m2aula3.main01

python -m src.m2aula3.main02
