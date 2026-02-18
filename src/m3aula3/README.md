### Descricao do arquivo

chatbot (backend) ->
Esse código implementa um backend de chatbot com LangChain e LangGraph: ele inicializa um modelo de linguagem, define uma estrutura de estado (State) que contém a pergunta do usuário, o contexto extraído de documentos e a resposta, cria uma função (generate) que concatena o conteúdo dos documentos, aplica um template de prompt com instruções de como responder e invoca o modelo, e por fim organiza tudo em um grafo de estados que é compilado em uma aplicação (app) pronta para ser usada no frontend (como o Streamlit).

interface (frontend) ->
Esse código implementa o frontend em Streamlit para o chatbot da loja de bicicletas: ele configura a página e título, inicializa o histórico de mensagens com uma saudação do assistente, permite o upload de arquivos PDF e extrai seu conteúdo, captura a entrada do usuário pelo campo de chat, adiciona essa entrada ao histórico, monta o estado (State) com pergunta, contexto e resposta inicial, invoca o backend para obter a resposta do modelo, atualiza o histórico com essa resposta e, por fim, renderiza toda a conversa (usuário e assistente) na interface gráfica

### Para Rodar

python -m streamlit run src/m3aula3/interface.py
