# Ferramenta cívica legislativa — plano de arquitetura e Etapa 1

Status: rascunho para discussão. Nenhum código será escrito antes da validação.

## Contexto

Diretório de trabalho vazio (`/home/user`), sem repositório. O briefing pede: (1) discutir arquitetura com alternativas antes de codificar; (2) começar pela validação das fontes (Etapa 1). Este plano cobre só essas duas coisas.

## 1. Arquitetura proposta (a validar)

Decisão (validada): **opção A — site estático gerado a partir de uma base curada offline, com atualização automática diária** e data da última atualização visível no site. Mecanismo proposto: agendamento diário no GitHub Actions, que coleta, regenera e publica o site sem depender de uma sessão minha aberta. Atualizam sozinhos apenas os campos oficiais (situação, tramitação, votações). Itens novos entram numa **fila de revisão**. Claude propõe o vínculo ao tema, o resumo cidadão e o grau de aderência; a usuária aprova ou ajusta por pull request antes da publicação. Como o fluxo de proposta automática será montado (ex.: rotina agendada) fica para a Etapa 3. Complemento proposto: cada item também exibe a data da extração e um aviso para consultar a fonte oficial e ver a situação atual, porque o status pode mudar entre uma atualização e outra.

Fluxo: scripts de coleta (APIs Câmara/Senado/LexML) → base intermediária versionada (SQLite + JSON) → camada de curadoria manual (vínculo tema↔item, resumo cidadão, grau de aderência, políticas públicas) → revisão de neutralidade → geração do site estático.

| Opção | Prós | Contras |
|---|---|---|
| A. Estático + base curada (recomendada) | Todo texto passa por revisão de neutralidade antes de publicar; base versionada = auditável (data de extração por item); sem dependência da disponibilidade das APIs; hospedagem gratuita | Dados envelhecem; exige rotina de atualização (ex.: semanal) |
| B. Backend consultando APIs ao vivo | Status sempre atual | Resumos cidadãos e vínculo tema↔lei não vêm das APIs (precisam de curadoria de qualquer forma); instabilidade das APIs vira falha da ferramenta; custo e manutenção maiores |
| C. Híbrido (base curada + status/tramitação ao vivo) | Conteúdo curado + status atual | Mais complexo; status ao vivo pode contradizer nota de arquivamento já revisada |

Princípios do briefing traduzidos em regras de dados: cada item guarda `fonte_url`, `ementa_oficial`, `data_extracao`; `situacao` armazenada literalmente como vem da fonte; autoria grava partido/UF **na data da proposição**; vínculo tema↔item tem campo `aderencia` (direta/aproximada) exibido na interface; leis e políticas são entidades separadas.

Stack (provisória, a discutir depois): Python para coleta; gerador estático simples para o site.

## 2. Etapa 1 — Validação das fontes (somente leitura)

Objetivo: produzir um **relatório de cobertura** (funcionalidade × fonte × campo × status: sustentado / parcial / não sustentado), com exemplos reais e links.

Testes por fonte (endpoints a confirmar na documentação vigente):
- Câmara (`dadosabertos.camara.leg.br/api/v2`): proposições por tema, autores, tramitações (regime, situação, pareceres), votações, votos nominais, orientações de bancada.
- Senado (`legis.senado.leg.br/dadosabertos`): matérias, autoria, tramitação, votações nominais; verificar endpoints migrados/descontinuados.
- LexML (SRU) e Planalto: busca de leis federais pós-1988; verificar se há indicação estruturada de vigência/revogação.

Riscos a verificar e reportar antes de seguir (hipóteses, não confirmadas):
1. Partido na data da proposição: o endpoint de autores pode retornar só o vínculo atual; pode exigir cruzar com histórico do parlamentar.
2. Vigência de leis: possivelmente não há campo estruturado de "vigente/revogada"; pode exigir curadoria manual.
3. Votação simbólica: confirmar se orientação de bancada é registrada nesses casos.
4. Regra de arquivamento: confirmar texto vigente do RICD art. 105 e do RISF (art. 332) e quais campos da API permitem aplicar as exceções.
5. Mapeamento entre temas da Câmara e do Senado (classificações diferentes).

Entregável: relatório em Markdown na pasta do projeto + scripts de teste reproduzíveis.

Passos de execução:
1. Criar o repositório público `ferramenta-civica-legislativa`. Primeiro tento pelo `gh`; se não houver permissão, peço que você crie o repositório e me informe o nome.
2. Montar a estrutura mínima: `README.md` (aviso de protótipo), `CLAUDE.md` (o briefing), `etapa1/scripts/` e `etapa1/relatorio-cobertura.md`.
3. Escrever scripts Python de sondagem, apenas com requisições de leitura e respostas salvas em `etapa1/amostras/`.
4. Testar cada risco listado acima com 5 proposições por tema, nos 3 temas.
5. Confirmar o texto vigente do RICD art. 105 e do RISF art. 332 nas fontes oficiais e citar os trechos literalmente.
6. Redigir o relatório. Nele, separar o que foi observado nas respostas da API do que é inferência.
7. Fazer commit e push, e apresentar o relatório para validação antes da Etapa 2.

## Verificação

Cada afirmação do relatório acompanhada da requisição feita, data/hora e trecho da resposta. Checagem manual por amostragem (5 proposições por tema) comparando API × página oficial.

## Perguntas em aberto (uma por vez)

1. ~~Arquitetura~~ → A, atualização semanal.
2. ~~Versionamento~~ → novo repositório GitHub **público**, nome sugerido `ferramenta-civica-legislativa`. O README deve avisar que é um protótipo e que os textos ainda não passaram pela revisão de neutralidade.
3. ~~Manutenção~~ → atualização diária automática, fila de revisão em que Claude propõe e a usuária aprova.
