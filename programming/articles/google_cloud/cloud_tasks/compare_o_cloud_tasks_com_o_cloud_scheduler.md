# [Compare o Cloud Tasks com o Cloud Scheduler](https://cloud.google.com/tasks/docs/comp-tasks-sched?hl=pt-br)

Ambas as ferramentas tem como foco **eventos do tipo tarefa** e **invocação explícita**, porém, atuações de perspectivas distintas.

- O Cloud Tasks foca em **tarefas individuais e não periódicas**. Portanto, cada tarefá um registro único na fila, tendo seu ciclo de vida pautado pela sua execução (morre em caso de sucesso e volta para fila em caso de falha).
  - Até permite configurações de agendamento, porém, apenas para definição do horário de entrega da tarefa.

- O Cloud Scheduler foca em **tarefas periódicas**. Portanto, cada agendamento tem um registro, o qual é compartilhado entre todas as execuções do `cron job`.
  - Re-tentativa devem ser explicitamente configuradas, caso contrário, o erro é apenas registrado.