# [Escolha um tipo de assinatura](https://cloud.google.com/pubsub/docs/subscriber?hl=pt-br#push-subscription)

## Sobre assinaturas

- Somente as mensagens publicadas no tópico após a criação da assinatura ficam disponíveis para os clientes assinantes.
- Pode-se ativar a [retenção de tópicos](https://cloud.google.com/pubsub/docs/replay-overview?hl=pt-br) para permitir que uma assinatura anexada ao tópico volte no tempo e repita as mensagens publicadas anteriormente.
- Relacionamento NxM entre tópico e assinante, tendo a assinatura como entidade auxiliar.
  - Um tópico pode possuir várias assinaturas, portanto, vários serviços assinantes.
  - Um serviço pode possuir várias assinaturas, portanto, vários tópicos assinados.
  - Uma assinatura deve ter apenas um tópico, porém, múltiplos assinantes.

## Fluxo de trabalho de assinatura

- O inscrito possuir um tempo configurável para responder a mensagem (`ackDeadline`), afirmando que foi reconhecida.
- Mensagens possuem os seguintes status:
  - `outstanding` durante o `ackDeadline`.
  - `delivered` após a confirmação dentro do `ackDeadline`.
  - `undelivered` após o fim do `ackDeadline` sem confirmação.
- Para cada status, o Pub/Sub tem os seguintes comportamentos perante assinantes de uma mesma assinatura:
  - enquanto `outstanding`, não envia a mensagem para nenhum outro assinante.
  - quando `delivered`, envia a mensagem para o próximo assinante.
  - quando `undelivered`, continua o envio aos demais assinantes e tenta reenviar ao assinante que não reconheceu.

## [Assinaturas de Pull](https://cloud.google.com/pubsub/docs/pull?hl=pt-br)

### Fluxo

1. O consumidor é responsável por requisitar ao Pub/Sub o recebimento das mensagens (`PullRequest`).
2. O Pub/Sub retorna as mensagens presentes na fila (`PullResponse`), caso reconheça o consumidor como assinante.
3. O consumidor é responsável por informar o recebimento de cada mensagem (`AckRequest`).
   1. Caso a resposta seja negativa, o Pub/Sub entende que a mensagem deve ser reenviada.

Obs.: Entre um `PullRequest` e um `AckRequest` podem ser enviados vários `PullResponse`.
Obs.: Um `AckRequest` pode informar o recebimento de várias mensagens.

## [Assinaturas de Push](https://cloud.google.com/pubsub/docs/push?hl=pt-br)

### Fluxo

1. O Pub/Sub é responsável por enviar mensagens da fila para um endpoint HTTPS do assinante (`PushRequest`).
2. O consumidor é responsável por responder cada mensagem (`PushResponse`).
   1. Caso a resposta seja negativa, o Pub/Sub entende que a mensagem deve ser reenviada.

Obs.: O processo de `PushRequest` e `PushResponse` trabalham apenas uma mensagem por vez.
Obs.: O Pub/Sub ajusta dinamicamente a taxa de `PushRequest` com base na taxa em que recebe respostas bem-sucedidas.

### Propriedades da assinatura

- **URL do endpoint (obrigatório)**: endereço HTTPS público.
  - Requer que o servidor possua um certificado SSL válido.
  - A região do Google Cloud que efetua o envio é a mesma do recurso Pub/Sub.
- **Ativar autenticação**: quando ativado, envia-se um cabeçalho para autenticação.
  - Quando no mesmo projeto do Pub/Sub, App Engine Standard e Cloud Functions possuem autenticação eu autorização automáticos.

### Formato da mensagem

- A mensagem é enviada no corpo da requisição HTTP POST.
- O valor da mensagem está no atributo `message.data`.
- O valor da mensagem está criptografado em base64-encoded.
- Os demais dados são meta-dados do recurso de Pub/Sub.
- O atributo `message.attributes` possui um conjunto de propriedades personalizadas e passiveis de [filtros na assinatura](https://cloud.google.com/pubsub/docs/subscription-message-filter?hl=pt-br).

```json
{
    "message": {
        "attributes": {
            "key": "value"
        },
        "data": "SGVsbG8gQ2xvdWQgUHViL1N1YiEgSGVyZSBpcyBteSBtZXNzYWdlIQ==",
        "messageId": "2070443601311540",
        "message_id": "2070443601311540",
        "publishTime": "2021-02-26T19:13:55.749Z",
        "publish_time": "2021-02-26T19:13:55.749Z"
    },
   "subscription": "projects/myproject/subscriptions/mysubscription"
}
```

### Autenticação

- Uma vez ativada, o Pub/Sub envia um token JWT assinado no cabeçalho `Authorization` da requisição.
- O token possui uma descrição de usuário (`claims`) e uma assinatura.
- Para autenticar a requisição, deve-se verificar a assinatura do token por meio da lib do google oauth2.
