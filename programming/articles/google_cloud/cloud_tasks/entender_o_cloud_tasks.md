# [Entender o Cloud Tasks](https://cloud.google.com/tasks/docs/dual-overview?hl=pt-br)

## Conceitos

- **Fila**: conjunto de tarefas com o mesmo tipo de destino gerenciado por uma única configuração.
- **Tipo de destino**: como e o local em que uma tarefa é processada.
- **Workers**: serviço que processa tarefas.
- **Tarefas**/**Tasks**: trabalhos que podem ser executados de maneira independente e assíncrona, fora do fluxo principal.
- **Tentativa de execução**: tentativa de executar uma tarefa.
- **Tentativa de despacho**: momento em que o Cloud Tasks enviou a tarefa ao seu destino.
- **Tentativa de resposta**: resposta de um worker que indica que o trabalho associado à tarefa foi concluído com sucesso ou falhou.

### Tarefas

- **Nome**: nome exclusivo para identificação do recurso.
- **Configurações**: descrição do processo de execução.
- **Dados da solicitação**/**Payload**: dados enviados juntos da tarefa e necessários para sua execução.

## Requisitos atendidos

- Controle de fila de tarefas.
- Controle de fluxo de envio.
- Garante a execução "confiável"das tarefas pelos workers.
- Permite que o serviço de origem determine controles a serem aplicados ao envio, afim de definir seu conceito de "confiável".
  - Agendar horários de entrega específicos.
  - Gerenciar taxas de envio.
  - Configurar o comportamento de repetição.
  - Acessar e gerenciar tarefas individuais em uma fila.
  - Ativar a eliminação de duplicação de tarefas
- Auto-gerenciamento dos recursos utilizados para prover o serviço.
  - Ex.: custos de latência do usuário, falhas do servidor, limitações de consumo de recursos e gerenciamento de novas tentativas.

Obs.: Não oferece garantias fortes em relação ao tempo de entrega da tarefa e, portanto, não é adequado para aplicativos interativos em que um usuário aguarda o resultado.

## Fluxo de trabalho

1. Cria-se um worker para processar as tarefas.
2. Cria-se uma fila no Cloud Tasks.
3. Cria-se tarefas de maneira programática e as adiciona à fila.
4. O Cloud Tasks retorna um OK para o aplicativo de origem quando registra uma tarefa com sucesso em sua fila.
5. As tarefas são transmitidas para o worker.
6. O worker processa a tarefa.
7. O worker retorna um código de status de sucesso 2xx para o serviço Cloud Tasks.

## Motivações

- Proporcionar uma fila para execução de tarefas com foco nas demandas da origem (invocação explicita).

## Casos de uso

### Processamento e fluxos de trabalho paralelos

"Eventos de tarefas" podem ser enviados para o Cloud Task afim de acionar os devidos atuadores. Diferente do Pub/Sub, o foco aqui é na visão da origem do evento, a qual conhece o worker de destino, assim, definindo configurações específicas para essa execução.