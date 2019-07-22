![Build Status](https://travis-ci.org/joaojunior/crawler_tribunais.svg?branch=master)
![Test Coverage](https://codecov.io/gh/joaojunior/crawler_tribunais/branch/master/graph/badge.svg)

# Crawlers Tribunais
Esse repositório contém um exemplo de como fazer uma crawler para tribunais do Brasil.

A solução consiste de uma biblioteca python, responsável por fazer o download e o parser de um processo dos Tribunais de Justiça de Alagoas (TJAL) e do Mato Grosso do Sul (TJMS). Essa biblioteca é exposta por meio de uma api restful que recebe o número do processo como parâmetro. A api consulta o
banco de dados para verificar se o processo já foi baixado. Caso a resposta seja positiva, o processo é retornado a partir do banco de dados.
Caso a resposta seja negativa, uma tarefa assíncrona é disparada para fazer o download do processo e o parser desse arquivo. Após isso, podemos
consultar o processo a partir da mesma url.

Essa solução também fornece:
- Validação de número de processo: Caso o número do processo seja inválido ou não seja dos tribunais TJAL e TJMS a api vai responder com
uma mensagem de erro e `status_code=422`
- Geração de número de processos: É possível rodar o script para gerar números de processo e executar o download dos arquivos

# Como rodar os testes:
Para rodar os testes, precisamos executar o comando:

```
docker-compose -f docker-compose.yml -f docker-compose.tests.yml up --build --exit-code-from api
```

# Como rodar a solução:
Para rodar a solução, devemos executar o comando:

```
docker-compose up --build
```

# Exemplo de como executar a solução:
Depois de rodar a solução, como explicado anteriormente, para consultar o processo de número 0710802-55.2018.8.02.0001, nós precisamos fazer
um http get request no endereço http://127.0.0.1:4000/, utilizando o curl, podemos fazer assim:

```
curl http://127.0.0.1:4000/0710802-55.2018.8.02.0001
```

Depois, desse comando você vai receber a resposta:
```
{"grade1":null,"grade2":null,"process_number":"0710802-55.2018.8.02.0001"}
```
Essa resposta indica que o processo não está no banco de dados e uma tarefa assíncrona foi disparada para baixar e formatar esse processp.
Aguarde alguns segundos e efetue novamente o mesmo request e você receberá os dados do processo.

# Rodar o script para gerar números de processo e efetuar o download:
Para gerar números de processo e efetuar o download do processo. Podemos executar o commando:
```
sh scripts/crawler_generated_process_number.sh
```

Esse comando vai gerar 10 números de processos(a quantidade pode ser configurada) do TJAL e do TJMS e chamar a api para fazer o download.
