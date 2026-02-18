### Descricao do arquivo

main01 ->
Esse código cria uma interface simples em Streamlit onde o usuário digita uma pergunta, envia para um modelo de linguagem (LLM) e recebe a resposta exibida diretamente na tela.

main02 ->
Baseado no código anterior, este foi adaptado para oferecer uma experiência mais robusta no Streamlit: além de permitir que o usuário insira uma pergunta e receba a resposta da LLM, ele valida entradas removendo espaços em branco e utiliza um spinner para indicar processamento, tornando a interação mais amigável e clara.

### Para Rodar

python -m streamlit run src/m3aula1/main01.py

python -m streamlit run src/m3aula1/main02.py
