# [Escolha o Cloud Tasks ou o Pub/Sub](https://cloud.google.com/tasks/docs/comp-pub-sub?hl=pt-br)

## Conceitos

### Tipos de invocação

- **Invocação implícita**: um Produtor faz com que os Consumidores executem ações de maneira implícita, por meio de publicações de eventos sem Consumidor pré-definido.
- **Invocação explícita**: um Produtor retém o controle total da execução, assim, especificando o Consumidor para qual cada mensagem deve ser entregue.

## Semelhanças

- Ambos são serviços de fila auto-gerenciados usados para transferências de mensagens e integrações assíncronas.
- Possuem um caso de uso em comum: "Processamento e fluxos de trabalho paralelos".

## Diferenças

### Motivações distintas

O Pub/Sub tem o objetivo de dissociar Produtores de Consumidores.
- Produtores e Consumidores são fracamente acoplados.
  - O acoplamento se dá apenas pelo contrato do evento.
- Produtores não tem conhecimento sobre seus Consumidores.
- Produtores não possuem controle sobre a entrega de mensagens.

O Cloud Tasks tem como objetivo a invocação explícita.
- Produtores e Consumidores são fortemente acoplados.
- Produtores tem conhecimento e poder sobre os Consumidores.

### Funcionalidades específicas

O Pub/Sub tem um aspecto generalista, atendendo a diferentes casos de usos, dentro de um conjunto de requisitos funcionais.


O Cloud Tasks possui um aspecto especialista, tem como foco atender à entrega de eventos do tipo tarefa.
  - Permite configurações de envio e entrega (horário, taxa de entrega, tentativas, eliminação de duplicidade e tratativa individual).

### Requisitos técnicos

Como as ferramentas se propõe a solucionar problemas distintos, ambas possuem requisitos funcionais diferentes. Para mais informações, leia o artigo original.