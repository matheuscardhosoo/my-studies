# [Orquestração vs Coreografia em microsserviços](https://medium.com/@crisaltmann/orquestra%C3%A7%C3%A3o-vs-coreografia-em-eda-8c14db455892)

## Citações interessantes

### Interfaces de microsserviços

> Normalmente, os microsserviços possuem interfaces de comunicação de entrada e saída. Como exemplo podemos REST APIs (síncronas) ou o processamento e geração de eventos (assíncronas).

É interessante sempre pensar em um serviço como um escopo delimitado de processos, os quais são acessados por meio de APIs pré-definidas. Dessa forma, o processamento de eventos se torna apenas mais uma interface de acesso, assim podendo ser instrumentalizado para compor serviços mais facilmente.

### Microserviço como parte de um todo

> [...] Quando temos este tipo de arquitetura é comum que um processo complexo seja dividido e composto por diversos serviços. Além disso estes serviços podem fazer parte de mais de um workflow, dependendo do domínio que este represente.

Uma vez que um serviço delimita o seu escopo a uma instância "micro", sendo responsável por apenas parte do conjunto de processos necessários para uma ação, vê-se necessário a criação de workflows mais complexos e dependentes de múltiplos serviços.

### Produção de eventos

> O serviço produtor está produzindo um resultado de processamento ou uma alteração de estado interno. Este evento pode ser consumido por diferentes serviços.

Assim como em uma API RESTFUL, torna-se necessário padronizar as interfaces para eventos, definindo uma estrutura comum e entendível por todos na arquitetura. Além disso, assim como na documentação de APIs via swagger, é necessário documentar os eventos conforme seus tipos, conteúdos, metadados, etc. 

### Coreografia de eventos

> Na coreografia o processo se dá pela comunicação direta entre os serviços.

O processamento de eventos é visto como apenas mais um canal de comunicação direta com o serviço, tendo apenas a peculiaridade de usufruir do assincronismo.

> Cada serviço, então, está interessado apenas em sua etapa, não sendo necessária a criação de serviços acessórios para controle de fluxo.

Uma vez que a orquestração dá ao microserviço a responsabilidade de gerir inteiramente a sua própria interface de eventos, esse passa a ter que conhecer o fluxo que faz parte para que possa dar continuidade ao processo. Esse comportamento acaba sendo um problema, pois cria acoplamentos entre os serviços.

> - [...] Se precisarmos alterar este workflow, adicionando uma etapa de formalização por exemplo, teríamos que alterar o serviço seguinte da cadeia pois temos um acoplamento entre a responsabilidade de negócio do serviço e o processamento do workflow.
> - [...] É muito mais difícil conseguirmos encontrar problemas dado que não existe um controle neste fluxo [...]. Você precisa de um bom sistema de tracing para conseguir identificar erros do fluxo, buscando em logs ou outras ferramentas os pontos de falha.
> - [...] Há uma dificuldade maior para reexecutar uma etapa ou tratar erros. [...] temos dificuldade em reprocessar algo pois regerar eventos de domínio podem causar impactos. Os serviços então além de controlar a sua lógica de negócio do seu domínio, precisam ter um bom controle de erro, salvando eventos com erro em cada etapa do workflow para poder gerir de maneira eficiente.

### Orquestração de eventos

> Na orquestração, temos diferentes microsserviços responsáveis por realizar uma parte de um processo de negócio. Cada microserviço então realiza esta etapa e não tem conhecimento dos demais componentes do sistema.

O processamento de eventos é visto como uma "lógica de fluxos complexos", aonde uma entidade é responsável por exercer o papel do mediador e conhecer o fluxo, enquanto os demais exercem apenas o papel de atuadores sobre um escopo pré-determinado.

> Há neste caso, um serviço responsável por gerenciar o fluxo. A este serviço se dá o nome de orquestrador.

Remove-se o acoplamento entre serviços de domínio e, então, terceiriza-se a execução do fluxo para um serviço mediador (orquestrador). Dessa forma, as etapas do processo passam a desconhecer o todo.

> - [...] facilita mudanças no fluxo, acompanhamento de erros;
> - [...] facilita o uso de diferentes protocolos de comunicação entre os diferentes serviços;
> - [...] sistemas coreografados são pouco resilientes e suscetíveis a falhas. No orquestrador isso pode ser melhor gerenciado;
> - [...] visualização da execução do workflow;
> - [...] é muito mais simples reprocessarmos ou executarmos uma etapa novamente visto que os comandos de execução substituem a reatividade.


