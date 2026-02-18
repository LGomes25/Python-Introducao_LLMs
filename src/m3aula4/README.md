### Descricao do arquivo

exemploStreamingTrue ->
Esse script é um exemplo prático de como utilizar um modelo de linguagem com e sem streaming. Na primeira parte, ele mostra a geração convencional, em que a resposta só aparece completa ao final. Na segunda parte, demonstra o modo streaming, imprimindo os tokens ou blocos de texto conforme são produzidos pelo modelo, permitindo acompanhar a resposta em tempo real no console. É útil para comparar os dois modos de interação e entender como o streaming pode enriquecer a experiência de uso.

chatbot (backend) ->
Esse código define um grafo de estados para um chatbot usando LangChain e LangGraph, conectando um prompt pré‑definido ao modelo de linguagem. Ele recebe uma pergunta e um contexto extraído de documentos PDF, aplica o template e retorna a resposta em modo streaming para integração com o Streamlit. Cada interação é independente, sem memória de conversa — ou seja, não há encadeamento entre respostas anteriores — e, quando há arquivo carregado, o conteúdo do PDF se torna o contexto usado pelo modelo.

chatbotMemo (backend) ->
Baseado no modelo anterior (chatbot), o código foi melhorado para utilizar o histórico como contexto de conversa, assim servindo de "memória" para o chat.

interface (frontend) ->
Esse código implementa a interface em Streamlit para um chatbot de loja de bicicletas. Ele configura a página, inicializa um histórico com mensagem de boas‑vindas, permite upload de PDF e extrai seu texto para servir de contexto. As mensagens do usuário são adicionadas ao histórico, o backend é invocado com pergunta e contexto, e a resposta é exibida em streaming e depois registrada no histórico. Importante: o histórico é usado apenas para exibição na interface, não como memória de conversa — cada interação é independente, e quando há PDF carregado, o conteúdo do arquivo se torna o contexto da resposta.

interface2 (frontend) ->
Baseado no modelo anterior (interface), o código foi melhorado para apresentar as mensagens de forma sequencial de cima para baixo, sendo mais próximo de um chat com IA convencional. Continua sem mem´roa agregada, cada iteração é única e não utiliza o histórico como contexto.

interfaceMemo (frontend) ->
Baseado no modelo anterior (interface2), o código foi melhorado para utilizar o histórico como contexto de conversa, assim servindo de "memória" para o chat.

### Para Rodar

python -m src.m3aula4.exemploStreamingTrue

python -m streamlit run src/m3aula4/interface.py

python -m streamlit run src/m3aula4/interface2.py

python -m streamlit run src/m3aula4/interfaceMemo.py
