#Nimbus
Serviço que consulta a previsão do tempo por hora e indica janelas boas ou ruins para correr, com base em regras próprias sobre UV, sensação térmica e chance de chuva. Roda sozinho, dentro de um container Docker, com tratamento de falha de API.

Status: em desenvolvimento. 
A extração de dados da API ✅; 
Aplicação da regra; ❌
Agendamento; ❌
Containerização ainda estão em construção; ❌

Por que esse projeto existe

A maioria dos apps de clima dá uma resposta genérica pro dia inteiro. Na prática, um mesmo dia pode ter uma manhã ótima para correr e uma tarde péssima — e é isso que o Nimbus tenta responder: não "como está o tempo hoje", mas "em quais horas vale a pena sair pra correr".

O projeto também é um exercício prático de backend e DevOps: a lógica de negócio em si é propositalmente simples, e o peso do aprendizado está em fazer esse serviço rodar sozinho, se recuperar de falhas e ser configurável para qualquer cidade.

Como funciona
Extração: busca a previsão de 7 dias na API da Open-Meteo (aberta, sem necessidade de chave), já organizada em uma lista de horas, cada uma com horário, sensação térmica, índice UV e chance de chuva.
Classificação: cada hora é avaliada e marcada como boa ou ruim para correr, segundo uma regra em camadas (veja abaixo).
Saída: o resultado é registrado em log.
Repetição: o processo roda sozinho, periodicamente, dentro de um container Docker.
Regra de classificação

Avaliada hora a hora, apenas dentro de uma janela do dia (provisoriamente 5h às 20h):

Chance de chuva ≥ 50% → ruim
Índice UV ≥ 6 (nível "alto" na escala da OMS) → ruim
Sensação térmica ≥ 33 °C → ruim
Caso contrário → bom

A ordem importa: chuva e UV vetam a hora antes de a temperatura ser considerada.

Por que sensação térmica, e não temperatura do ar

Em testes com dados reais, a temperatura do ar sozinha produzia classificações contraditórias para horas com condições parecidas (mesma temperatura, sensação bem diferente por causa da umidade). A sensação térmica (apparent_temperature), combinada com o índice UV, explicou de forma consistente a percepção real de "bom" ou "ruim" para correr.

Todos os limites usados na regra (chuva, UV, temperatura, janela do dia) são valores de configuração, não estão fixos na lógica — podem ser ajustados sem alterar o código.

Tratamento de falha de API
Retry: até 5 tentativas em sequência, com 10 segundos de intervalo entre elas.
Cooldown: 10 minutos de espera entre uma rodada de tentativas e a próxima.
Limite: até 6 rodadas. Se todas falharem, o programa desiste daquela execução, registra o erro no log e segue ativo até o próximo horário agendado.

Uma falha nunca derruba o processo inteiro — apenas aquela tentativa de busca falha e é registrada.

Stack
Python — linguagem da lógica de extração e classificação
Docker — containerização, para o serviço rodar de forma isolada e reprodutível em qualquer máquina
Open-Meteo API — fonte de dados meteorológicos

Decisões descartadas conscientemente
PostgreSQL: avaliado e descartado — não há persistência de histórico na v1, então um banco de dados completo adicionaria infraestrutura sem necessidade real.
Kubernetes / microsserviços: avaliado e descartado — desproporcional para um serviço de responsabilidade única rodando para um usuário só. Docker sozinho resolve o problema real (consistência de ambiente), sem a complexidade de orquestração.

Roadmap
Vento, rajadas e condições de tempestade como critérios adicionais de veto
Nível intermediário ("aceitável") na classificação
Resumo diário (ex: pico de chance de chuva do dia)
API própria (FastAPI) expondo os resultados
Dashboard web
Notificações (Telegram/e-mail)
Testes automatizados em CI
Aprendizado

O backend (extração e regra de negócio) é escrito manualmente, sem geração de código por IA — é a parte do projeto voltada ao aprendizado de back-end e DevOps. O frontend, quando existir, será implementado com apoio de IA, supervisionado e revisado por mim.
