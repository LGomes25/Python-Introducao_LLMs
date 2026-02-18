### Descricao do arquivo

chatbot (backend) ->
Esse código implementa um backend de chat usando LangChain e LangGraph: ele inicializa um modelo de linguagem com instruções de sistema, organiza o histórico de mensagens em um grafo de estados e compila uma aplicação capaz de gerar respostas encadeadas e consistentes durante a conversa.

interface (frontend) ->
Esse código implementa um chatbot em Streamlit para uma loja de bicicletas, inicializando e mantendo o histórico de mensagens, capturando a entrada do usuário, invocando o backend de IA para gerar respostas e exibindo toda a conversa de forma encadeada na interface.

### Para Rodar

python -m streamlit run src/m3aula2/interface.py
