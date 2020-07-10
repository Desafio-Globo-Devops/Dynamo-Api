# Dynamo-Api
Api Rest feita para acessar os Logs do DynamoDB feito no Projeto Serveless. 

## Requisitos para rodar a aplicação:

- Setar as variáveis de ambiente ```TABLE```, ```AWS_DEFAULT_REGION```, ```AWS_ACCESS_KEY_ID```, ```AWS_SECRET_ACCESS_KEY```.
- Respectivamente com o nome da Table no qual foi o setado no projeto anterior:```'Event_Capture'```, sua Region, Acess key e Secret key da AWS Account.

### Executando a aplicação:
A aplicação é executada em container, então basta digitar no terminal: ```make build``` bara construir a image do docker e ```make run``` rodar o container. O mesmo subirá com o nome ***dynamo-api***.
A aplicação foi feita em Flask com documentação, interface swagger e está exposta pelo ```localhost:8100```.

### Endpoints

- ```GET /api/logs/```: endpoint para obter todos os Logs do Banco de Dados.

- ```GET /api/logs/{id}```: endpoint para obter Logs pelo {id}.

- ```PUT /api/logs/{id}```:  endpoint para alterar os campos disponíveis{id}.

- ```DELETE /api/logs/{id}```:  endpoint para obter deletar os campos disponíveis{id}.

### Ferramentas

 - Linguagem: **Python 3.7**
 - Interface e Documentação: **Swagger 2.0**
 - Biblioteca: **Flask & DynamoDB**

autor: **Daniel Nicácio**
