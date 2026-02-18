### Descricao do arquivo

main01 ->
Esse código carrega um PDF com PyPDFLoader e transforma cada página em objetos Document. Ele imprime o número de páginas, metadados da primeira página, tamanho de cada página e do texto total, além de mostrar um trecho inicial da primeira página. Por fim, concatena e exibe todo o conteúdo do arquivo no console.

main02 ->
Esse código carrega um PDF e usa LangChain para montar um fluxo de perguntas e respostas. Ele define um estado com contexto, pergunta e resposta, gera um prompt e invoca o modelo para responder. Por fim, imprime no console a resposta baseada no conteúdo do documento.

main03 ->
Baseado no código anterior, este foi adaptado para criar uma interface interativa de perguntas e respostas sobre um PDF. Ele carrega o documento uma vez, mantém o contexto e permite que o usuário faça várias perguntas em sequência, exibindo as respostas do modelo até que o usuário encerre o programa.

### Para Rodar

python -m src.m2aula4.main01

python -m src.m2aula4.main02

python -m src.m2aula4.main03
