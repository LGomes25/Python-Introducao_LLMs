### Descricao do arquivo

main01 ->
Utilização de langchain para encadear mensagem e chamada com método "invoke" para a resposda da llm
Código baseado em módulo de mensagem (langchain_core.messages)
SystemMessage - instruções para a llm (prompt)
HumanMessage - mensagem do usuário

main02 ->
Utilização de LangChain para estruturar mensagens e enviar ao modelo com o método invoke.
O código usa o módulo ChatPromptTemplate (langchain_core.prompts) para definir um prompt com mensagens de sistema e usuário.
O método invoke substitui os placeholders do template ({idiomaEntrada}, {idiomaSaida}, {texto}) pelos valores fornecidos pelo usuário, e o resultado é enviado para a LLM.

### Para Rodar

python -m src.m2aula2.main01

python -m src.m2aula2.main02
