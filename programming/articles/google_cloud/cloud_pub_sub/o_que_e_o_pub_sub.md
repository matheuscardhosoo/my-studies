# [O que é o Pub/Sub?](https://cloud.google.com/pubsub/docs/overview?hl=pt-br)

## Conceitos

- **Pub/Sub**: serviço de mensageria assíncrono e escalável que transmite mensagens de produtores até consumidores.
- **Produtor**/**Publisher**: serviço que cria e envia mensagens para um ou vários tópicos.
- **Consumidor**/**Subscriber**: serviço com uma assinatura de um ou vários tópicos para receber mensagens dele.
- **Tópico**: recurso nomeado para o qual os produtores enviam mensagens.
- **Assinatura**: recurso nomeado que representa o stream de mensagens de um único tópico ao ao consumidor.
- **Mensagem**: combinação de dados e atributos (opcional) que um produtor envia para um tópico e é entregue aos consumidores.
- **Confirmação**/**Ack**: Um sinal enviado por um assinante ao Pub/Sub depois de receber uma mensagem. As mensagens confirmadas são removidas da fila de mensagens de assinatura.
- **Push** e **Pull**: métodos de entrega de mensagem. Um assinante recebe as mensagens do Pub/Sub enviando-as para o endpoint escolhido ou o assinante as extraindo do serviço.
- **Fan-out**: relação de um único produtor para muitos consumidores.
- **Fan-in**: relação de muitos produtores para um único consumidor.

## Requisitos atendidos

- Latência de até `100 ms` para entrega de mensagens.
- Controle de fila.
- Estabilização de fluxo conforme capacidades dos consumidores (recebimento "irrestrito" e entrega cadenciada).
- Garantia de entrega.
- Garantia de ordem de entrega.

## Motivações

- Integrar produtores e consumidores de maneira assíncrona, segura e consistente.

## Casos de uso

### Ingestão de interações/eventos

"Eventos de interações de usuário/serviço" podem ser enviados para o Pub/Sub afim de serem distribuídos adequadamente entre diversos consumidores.

### Distribuição de eventos em "tempo real"

Uma vez que o requisito de "tempo real" é definido como `latência <= 100 ms`, o Pub/Sub torna-se uma solução viável.

### Replicação/Sincronização de base de dados

"Eventos de alteração de dados" podem ser enviados para o Pub/Sub afim de informa a bases réplicas, ou sincronizadas, que ouve uma alteração.

### Processamento e fluxos de trabalho paralelos

"Eventos de tarefas" podem ser enviados para o Pub/Sub afim de acionar os devidos atuadores.

### Barramento de eventos

Pode-se usar o Pub/Sub como um barramento de eventos para comunicação centralizada de serviços. 

### Atualizar caches distribuídos

"Eventos de controle de cache" podem ser enviados para o Pub/Sub afim atualizar os dados em cache.

## Tipos de Pub/Sub

- **Serviço do Pub/Sub**: opção padrão, cobrindo tudo que já foi comentado.
- [**Serviço do Pub/Sub Lite**](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite?hl=pt-br): opção mais barata, a qual abre mão de confiabilidade e automatizações operacionais em prol de menor custo. Demanda controle manual disponibilidade e armazenamento.

## Comparação entre o Pub/Sub e outras tecnologias de mensagens

- [Necessário entender demais ferramentas similares].

## Comparar a comunicação entre serviços e serviços

- Não indicado para comunicação cliente-servidor.
  - Considerar produtos que usam o [Firebase Realtime Database](https://firebase.google.com/docs/database?hl=pt-br) e o [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging?hl=pt-br).
- Não indicado para comunicação **IoT-client-service**.
  - Considerar [Cloud IoT Core](https://cloud.google.com/iot/docs/concepts/overview?hl=pt-br).
- Não indicado para comunicação **tarefas assíncronas** (invocação explicita).
  - Considerar [Cloud Tasks](https://cloud.google.com/tasks/docs/dual-overview?hl=pt-br).