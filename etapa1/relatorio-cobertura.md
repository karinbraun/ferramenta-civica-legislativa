# Relatório de cobertura das fontes — Etapa 1

Status: concluído, com exceção da Parte IV (texto vigente dos regimentos). Ela depende de liberar os domínios `normas.leg.br` e `www2.camara.leg.br` neste ambiente (seção 9).

Convenções deste relatório:
- **Observado**: o que está nas respostas salvas em `etapa1/amostras/`. Cada arquivo traz a URL, a data/hora da requisição e a resposta bruta.
- **Inferência**: interpretação minha, ainda não confirmada em documentação oficial ou por um segundo teste.

## Síntese geral da Etapa 1

| Funcionalidade do briefing | Câmara | Senado | Legislação | Conclusão |
|---|---|---|---|---|
| 1–2. Itens por tema, com ementa oficial e link | Sustentado | Sustentado | Sustentado (API do Senado) | Viável. O vínculo ao tema exige curadoria (ver abaixo). |
| Temas oficiais como base | Parcial: 32 temas, sem "impostos" | Parcial: 179 classes, com "Tributos" | Parcial: classificação incompleta | Não há correspondência oficial entre as casas. Tabela própria na Etapa 2. |
| Situação oficial da tramitação | Sustentado | Sustentado | — | Viável. |
| 3. Autoria com partido e UF na data | Parcial: calculado pelo histórico | Sustentado | — | Viável, com validação de casos de troca de partido. |
| 4. Votos nominais por parlamentar e partido | Sustentado | Sustentado | — | Viável. O partido gravado é o da época. |
| 4. Votação simbólica | Sem voto e sem orientação | Sem registro estruturado | — | Decidido: só o resultado, com aviso. |
| 4. Votação secreta | — | Só presença | — | Decidido: só o resultado, com aviso e fundamento legal. |
| "Leis vigentes" | — | — | Parcial: revogação no todo estruturada; tácita, parcial e STF não | Decisão de texto pendente ("sem registro de revogação"). |
| 6. Nota de arquivamento | Parcial | Parcial | — | Exceções ligadas à autoria podem ser verificadas automaticamente; as ligadas a parecer, não. Texto vigente do regimento pendente. |
| Políticas públicas | — | — | — | Curadoria manual, como previsto no briefing. Não testado nesta etapa. |
| 5. Nota de competência | — | — | — | Conteúdo educativo próprio. Não depende das APIs. |

Decisões tomadas na Etapa 1 (registradas em `CLAUDE.md`, seção 8): tratamento das votações simbólicas e secretas; API do Senado como fonte de coleta das leis, com LexML e Planalto apenas como link.

Pendências que passam para as próximas etapas:
- **Etapa 2:** tabela de correspondência entre temas da Câmara, classes do Senado e os 3 temas do protótipo; texto de interface para leis sem registro de revogação.
- **Etapa 3:** validar o cálculo do partido da Câmara em trocas no meio da legislatura; usar a data da apresentação original no Senado; deduzir votações simbólicas no Senado; datas de efeito de revogações; carga incremental ano a ano.
- **Bloqueio de ambiente:** texto vigente do RICD art. 105, do RISF art. 332 e do fundamento do voto secreto (seção 9).

Execução: `python3 etapa1/scripts/sondagem_camara.py`, rodado em 26/10/2026. Foram 465 requisições, todas de leitura. O resumo está em `etapa1/amostras/camara/_resumo.json`.

Amostra: 5 projetos de lei por tema do protótipo, apresentados desde 01/02/2023, 15 no total. Também entraram as 100 votações do Plenário de novembro de 2025 e as 38 de 1º a 15 de julho de 2019.

# Parte I — Câmara dos Deputados

## 1. Síntese

| Funcionalidade do briefing | Situação na API da Câmara | Observação principal |
|---|---|---|
| Temas oficiais como base da navegação | **Parcial** | Os temas existem, mas cada projeto pode ter vários e a classificação mistura assuntos distantes. "Impostos" não é um tema oficial. |
| Ementa oficial e link para a fonte | **Sustentado** | Campos `ementa` e `urlInteiroTeor`, mais a página pública do projeto. |
| Situação oficial da tramitação | **Sustentado** | Campo `descricaoSituacao`, com uma lista oficial de 99 situações. |
| Autoria (autores e coautores) | **Sustentado** | Nome, tipo de autor e ordem de assinatura. |
| Partido e UF do autor na data da proposição | **Parcial** | O endpoint de autores não traz partido. É possível calcular o partido pelo histórico do deputado. Projetos vindos do Senado não trazem partido nenhum. |
| Votos nominais por parlamentar e partido | **Sustentado** | O partido gravado no voto é o da época da votação (confirmado). |
| Orientação de bancada em votação simbólica | **Não sustentado** | Em 79 votações sem voto individual, nenhuma tinha orientação registrada. Funcionalidade ajustada (seção 2.1). |
| Dados para a nota de arquivamento | **Parcial** | Regime, forma de apreciação e autor estão disponíveis. Saber se houve parecer favorável exige ler o texto das tramitações. |

## 2. Achados por risco

### 2.1 Votação simbólica e orientação de bancada (risco 3) — não sustentado

Observado. Nas 100 votações do Plenário de novembro de 2025:

| Situação | Votações |
|---|---|
| Com votos individuais e com orientação de bancada | 21 |
| Sem votos individuais e sem orientação | 79 |
| Sem votos individuais, mas com orientação | **0** |

Nas 38 votações de julho de 2019, o padrão se repete: 34 com votos e orientação, 4 sem nenhum dos dois, nenhuma só com orientação.

Exemplo: o substitutivo ao PL 4.333/2025, aprovado sem contagem de votos (votação `2555110-36`), devolve lista vazia tanto em `/votos` quanto em `/orientacoes`. O destaque seguinte do mesmo projeto (`2555110-45`) teve votação nominal e devolve 386 votos e 12 orientações.

Inferência: a API só registra orientação de bancada quando há votação nominal. Nas votações simbólicas, as orientações dos líderes provavelmente ficam apenas nas notas taquigráficas ou no vídeo da sessão, sem dado estruturado. **Por isso, a funcionalidade 4 do briefing não pode mostrar a orientação de bancada nas votações simbólicas a partir desta fonte.**

Decisão (27/10/2026): nas votações simbólicas, a interface mostra apenas o resultado oficial, com aviso de que a votação foi simbólica e não há registro de voto individual nem de orientação de bancada.

Observado também: as orientações incluem lideranças que não são partidos ("Governo", "Maioria", "Minoria", "Oposição", blocos e federações). A interface vai precisar explicar o que cada uma significa sem atribuir valor a nenhuma.

Observado também: o texto oficial do campo `descricao` às vezes cita o relator com o partido, por exemplo "assinada pelo relator, Dep. Alencar Santana (PT/SP)". Como o princípio "conteúdo antes da autoria" manda esconder autoria e partido por padrão, esse texto não pode aparecer na camada visível sem tratamento.

### 2.2 Partido na data da proposição (risco 1) — parcial

Observado:
- `/proposicoes/{id}/autores` não traz partido nem UF. Isso valeu para os 15 projetos da amostra.
- `/deputados/{id}/historico` traz entradas datadas com partido e UF. Daí dá para calcular o partido vigente em qualquer data.
- Projetos de autoria do Senado aparecem na Câmara como "Senado Federal - Senadora Dra. Eudócia", do tipo órgão, sem partido. Para esses, a autoria terá de vir da API do Senado.

Validação do método:
- Em 86 deputados de votações de 2019, o partido calculado pelo histórico coincidiu com o partido gravado no voto em 100% dos casos.
- Em 43 de 85 desses deputados, o partido atual é diferente do partido de 2019. Exemplos: Carlos Sampaio, PSDB em 2019 e PSD hoje; Elmar Nascimento, DEM em 2019 e UNIÃO hoje. Isso confirma que o voto guarda o partido da época, e não o atual.

Limitação observada: o histórico tem entradas anômalas. Uma delas é datada de 01/02/2023 e atribuída à legislatura 55, com a descrição "Nome no início da legislatura / Partido no início da legislatura". Dependendo da data consultada, o cálculo pode escolher essa entrada por engano. Ainda não testei casos de mudança de partido no meio da legislatura (janela partidária). Isso fica para a Etapa 3, com casos conhecidos.

### 2.3 Temas oficiais (insumo para a Etapa 2) — parcial

Observado:
- A lista oficial tem 32 temas. Não existe tema de tributação ou impostos. Os mais próximos são "Economia" (40) e "Finanças Públicas e Orçamento" (70).
- "Segurança" se divide entre "Defesa e Segurança" (57) e "Direito Penal e Processual Penal" (43).
- Cada projeto tem de 1 a 3 temas. O campo `relevancia` foi 0 em todos os 15 projetos da amostra, então não indica qual é o tema principal.
- Há classificações distantes do conteúdo. Exemplos: "Cria o Selo Verde Café Amazônia" está classificado também em Saúde; "Institui o Registro Eletrônico de Vacinações dos Animais de Estimação" também em Saúde; um fundo para pessoas com deficiência em "Finanças Públicas e Orçamento".

Inferência: o tema oficial serve como filtro inicial, mas não como vínculo final com o tema do cidadão. Isso reforça a curadoria na fila de revisão e o campo `aderencia` (direta ou aproximada), já previstos no plano. Para impostos, a combinação de tema com palavra-chave funcionou em 4 dos 5 casos da amostra.

### 2.4 Dados para a nota de arquivamento (risco 4) — parcial

Observado. O campo `statusProposicao` traz:
- `regime`, com valores como "Ordinário (Art. 151, III, RICD)", "Urgência (Art. 155, RICD)", "Urgência (Art. 64, CF)" e "Especial";
- `apreciacao`, por exemplo "Sujeita à Apreciação do Plenário" ou "Conclusiva pelas Comissões - Art. 24 II";
- `descricaoSituacao`, com valores como "Arquivada", "Tramitando em Conjunto" e "Pronta para Pauta".

O tipo de autor (deputado, Senado, Poder Executivo) também vem em `/autores`. O endpoint de referência `/referencias/proposicoes/codRegime` respondeu HTTP 405 e não está disponível.

As tramitações registram pareceres. Na amostra, de 0 a 8 entradas por projeto mencionam "parecer". Mas saber se o parecer foi **favorável** e se veio de **todas** as comissões exige ler o texto do despacho ou do documento.

Inferência: as exceções do art. 105 do RICD que dependem da autoria ou da origem do projeto (por exemplo, vindo do Senado ou do Executivo) podem ser verificadas automaticamente. As que dependem de parecer favorável não podem. O texto vigente do artigo ainda será confirmado nas próximas seções, e só depois dá para fechar essa lista.

### 2.5 Outros achados

Observado:
- A numeração de alguns projetos não corresponde à data de apresentação. A busca com `ano=2023` devolveu o "PL 6064/2023", apresentado em 2015 e já transformado em lei. Ainda não sei se isso é renumeração ou outra regra. Na Etapa 3, a seleção deve se basear em `dataApresentacao`, e não em `ano`.
- Projetos que chegam do Senado mantêm a numeração do Senado e aparecem com situação "Aguardando Despacho do Presidente da Câmara dos Deputados (Chancela)".
- A paginação devolve no máximo 100 itens por página, mesmo quando se pedem mais.
- A coleta completa levou cerca de 10 minutos com pausa de 0,3 s entre requisições. Para a atualização diária isso é viável, mas uma carga histórica desde 1988 precisa ser feita de forma incremental.

## 3. Pendências desta seção

1. ~~Decidir o que fazer com a orientação de bancada em votações simbólicas (seção 2.1).~~ Decidido em 27/10/2026: mostrar só o resultado oficial, com aviso.
2. Validar o cálculo do partido em casos de mudança no meio da legislatura (seção 2.2).
3. Fechar as exceções do art. 105 do RICD que podem ser verificadas com os campos disponíveis, depois de confirmar o texto vigente (seção 2.4).

# Parte II — Senado Federal

Execução: `python3 etapa1/scripts/sondagem_senado.py`, rodado em 27/10/2026. Foram cerca de 70 requisições, todas de leitura. O resumo está em `etapa1/amostras/senado/_resumo.json`.

Amostra: 5 projetos de lei por tema do protótipo, apresentados em 2025, 15 no total. Também entraram as votações nominais do Plenário de novembro de 2025 (12) e de julho de 2019 (8), com as respectivas orientações de bancada.

## 4. Síntese

| Funcionalidade do briefing | Situação na API do Senado | Observação principal |
|---|---|---|
| Endpoints vigentes | **Atenção** | Os endpoints antigos (`/materia/...`, `/plenario/lista/votacao`) foram desativados oficialmente em 01/02/2026, segundo os metadados da própria API, mas ainda respondem. A coleta deve usar só os novos (`/processo`, `/votacao`). |
| Classificação temática | **Parcial** | Taxonomia própria, diferente da Câmara. Há classe "Tributos", que a Câmara não tem. A classificação antiga por assunto só cobre projetos até 2021. |
| Ementa oficial e link | **Sustentado** | Campo `ementa` e link do documento. O link vem num domínio fora da lista liberada neste ambiente (ver 5.5). |
| Situação oficial da tramitação | **Sustentado** | Campo `situacaoAtual`, com uma lista oficial de 175 situações, além do campo `deliberacao`. |
| Partido e UF do autor na data | **Sustentado** | A autoria já traz partido, e é o da época da autoria. Senadores têm histórico de filiação com datas. Para deputados, o Senado não traz UF. |
| Votos nominais por parlamentar e partido | **Sustentado** | O partido gravado no voto é o da época da votação (confirmado). |
| Orientação de bancada | **Parcial** | Existe um endpoint próprio, mas só para votações nominais abertas. Em 2019 veio vazio. |
| Votação simbólica | **Não sustentado como dado estruturado** | Não aparece em `/votacao`. O resultado consta apenas no campo `deliberacao` e no texto da tramitação, sem marcar que foi simbólica. |
| Votação secreta | **Achado novo** | 11 das 12 votações nominais de novembro de 2025 foram secretas (indicação de autoridades). O voto individual aparece só como "Votou". |

## 5. Achados

### 5.1 Partido na data (risco 1) — sustentado

Observado:
- O detalhe do processo (`/processo/{id}`, bloco `autoriaIniciativa`) traz `siglaPartido` do autor, seja senador ou deputado.
- `/senador/{codigo}/filiacoes` traz o histórico de filiações com data de entrada e de saída.

Validação:
- Em 14 dos 15 projetos, o partido gravado na autoria coincide com o partido calculado pelo histórico na data de apresentação.
- A exceção confirma a regra. O PL 2810/2025 traz Margareth Buzetti como PSD, mas o histórico mostra PSD até 17/08/2025 e PP a partir de 21/08/2025. A data usada no cálculo (21/10/2025) era a do substitutivo da Câmara, e não a da apresentação original no Senado. O registro de autoria guardou o partido da época da autoria original, e não o atual.

Limitação observada: no detalhe do processo, `dataApresentacao` pode ser a data de uma etapa posterior, como um substitutivo. Para calcular o partido na data da proposição, é preciso usar a data da apresentação original.

Partido nos votos:
- Em novembro de 2025, 80 votos conferidos tiveram 0 divergências entre o partido gravado no voto e o histórico na data. Um dos casos é Alan Rick, que mudou de UNIÃO para REPUBLICANOS em 12/11/2025 e aparece como REPUBLICANOS na votação desse dia.
- Em julho de 2019, 19 de 43 senadores já estão em outro partido, e o voto continua mostrando o partido de 2019. Exemplos: Alessandro Vieira, CIDADANIA em 2019 e MDB hoje; Davi Alcolumbre, DEM em 2019 e UNIÃO hoje.

### 5.2 Votações simbólicas, secretas e orientação de bancada (risco 3)

Observado:
- `/votacao` traz apenas votações nominais. Em novembro de 2025 foram 12, das quais 11 secretas: escolha de autoridades e indicações para conselhos.
- Nas votações secretas, o voto individual aparece como "Votou" ou "SECRETO". Só a presença é pública.
- `/plenario/votacao/orientacaoBancada` devolveu as mesmas 12 votações. Só 1 tinha orientação preenchida: o PLP 185/2024, a única votação aberta, com 13 orientações. Entre elas aparecem partidos e lideranças como "Oposição".
- Em julho de 2019, nenhuma das 8 votações tinha orientação. Inferência: o registro estruturado de orientação no Senado pode ter começado depois de 2019. Isso ainda precisa ser confirmado com mais anos.
- Exemplo de votação simbólica: o PL 2810/2025 foi aprovado em Plenário em 11/11/2025 sem votação nominal. A API registra só `deliberacao` ("Aprovada pelo Plenário", destino "À sanção") e o texto "Aprovado o substitutivo da Câmara dos Deputados...", sem dizer que foi simbólica.

Inferência: a decisão de 27/10 para as votações simbólicas se aplica também ao Senado. Mostrar o resultado oficial, com aviso, é viável pelo campo `deliberacao`. Para afirmar que foi simbólica, é preciso deduzir que não houve votação nominal correspondente. Essa dedução precisa ser validada.

As **votações secretas** são um caso que o briefing não prevê. No Senado, elas tratam sobretudo de autoridades, e não de projetos de lei. Mesmo assim, a interface precisará de um aviso próprio se alguma aparecer.

### 5.3 Classificação temática e correspondência com a Câmara (risco 5) — parcial

Observado:
- O Senado usa uma árvore de 179 classes com 10 raízes (por exemplo, "Política Social / Saúde / Saúde Pública", "Economia e Desenvolvimento / Tributos / Imposto de Renda (IR)", "Soberania, Defesa Nacional e Ordem Pública / ... / Segurança Pública").
- A classificação antiga por assunto (`/processo/assuntos`) ainda existe, mas em busca ela só devolve projetos apresentados entre 2018 e 2021. Os projetos novos usam as classes.
- Cada projeto tem de 1 a 4 classes. Há a mesma mistura vista na Câmara: um protocolo de proteção de crianças na internet aparece em "Saúde" e em "Segurança Pública".
- A classe "Tributos" separou bem os projetos sobre impostos. Os 5 da amostra tratam de tributação.

Inferência: não há correspondência oficial entre os temas da Câmara (32) e as classes do Senado (179). A tabela de correspondência terá de ser montada por curadoria na Etapa 2. Para "impostos", a classe do Senado é mais precisa que os temas da Câmara.

### 5.4 Dados para a nota de arquivamento (risco 4) — parcial

Observado:
- `tramitando` (Sim/Não), `situacaoAtual`, `siglaCasaIniciadora` e `identificacaoProcessoInicial` (por exemplo, "PL 7769/2017" na Câmara) vêm prontos. Isso permite saber se o projeto veio da Câmara, critério relevante para as exceções do regimento.
- Há o parâmetro `tramitouLegislaturaAtual` e o endpoint `/processo/prazo`, de prazos regimentais. Ainda não testei nenhum dos dois.
- Os pareceres aparecem como texto na tramitação, por exemplo "Parecer da CDH, favorável ao PL 2810/2025...". Saber se o parecer foi favorável exige ler o texto, como na Câmara.

### 5.5 Outros achados

- O link do documento (`urlDocumento`) usa o domínio `legis.senado.gov.br`, que não está liberado neste ambiente. O mesmo caminho em `legis.senado.leg.br` funcionou (HTTP 200). Para o usuário final, no navegador, isso não é problema.
- Para deputados autores, o Senado traz partido mas não traz UF. A UF terá de vir da Câmara.
- A busca por data de apresentação aceita janelas de até 1 ano. A carga histórica precisa ser feita ano a ano.
- A API responde em JSON quando se envia `Accept: application/json`. Alguns endpoints exigem o sufixo `.json`.

## 6. Pendências desta seção

1. ~~Decidir como tratar as votações secretas, caso apareçam em projetos de lei (seção 5.2).~~ Decidido em 27/10/2026: mostrar só o resultado oficial, com o aviso "votação secreta: os votos individuais não são públicos" e o fundamento legal.
2. Validar a dedução de que um projeto aprovado sem votação nominal correspondente foi votado de forma simbólica (seção 5.2).
3. Testar `tramitouLegislaturaAtual` e `/processo/prazo` depois de confirmar o texto do art. 332 do RISF (seção 5.4).
4. Montar a tabela de correspondência entre temas da Câmara e classes do Senado na Etapa 2 (seção 5.3).

# Parte III — Legislação federal e vigência

Execução: `python3 etapa1/scripts/sondagem_legislacao.py`, rodado em 27/10/2026. Foram 10 requisições, todas de leitura. O resumo está em `etapa1/amostras/legislacao/_resumo.json`.

## 7. Síntese

| Necessidade do briefing | Fonte testada | Situação | Observação principal |
|---|---|---|---|
| Busca de leis federais | LexML (SRU) | **Inacessível para automação** | Devolve uma página de "Verificação de segurança" (desafio anti-robô), e não os dados. Não será contornado. |
| Busca de leis federais | Planalto | **Inacessível para automação** | O servidor encerra a conexão (teste de 26/10). |
| Lista de leis por ano, com ementa | Senado `/legislacao/lista` | **Sustentado** | 275 leis numeradas em 2023, cada uma com ementa e identificação. |
| Classificação temática das leis | Senado `/legislacao/{tipo}/{n}/{ano}` | **Parcial** | Usa a mesma "Classificação Temática Unificada" dos projetos do Senado, mas nem toda lei está classificada, e há classificações inesperadas. |
| Vigência ou revogação | Senado, campo `vides` | **Parcial, promissor** | Há declarações estruturadas como "Declaração de Revogação Permanente da Norma no Todo". Revogação parcial, revogação tácita e decisões do STF exigem cuidado. |
| Link para o texto oficial | Senado, campo `urlDocumento` | **Sustentado para o usuário** | Aponta para `normas.leg.br`, que abre no navegador. Esse domínio não está liberado neste ambiente. |

## 8. Achados

### 8.1 LexML e Planalto (fontes previstas no briefing)

Observado: a consulta SRU ao LexML de 27/10/2026 respondeu HTTP 200 com conteúdo `text/html`, mas o conteúdo é uma página intitulada "Verificação de segurança — Senado Federal", com um formulário de desafio, e não a resposta SRU (`lexml_sru_lei_8080.json`). No dia anterior, o mesmo domínio respondeu sem esse desafio a uma consulta simples. Inferência: o desafio foi ativado depois ou é aplicado conforme o padrão de acesso.

Contornar uma verificação anti-robô não é um caminho legítimo, então o LexML e o Planalto não podem ser fontes de **coleta automática** neste projeto. Ambos continuam válidos como **destino de link** para o usuário, que os abre no navegador.

### 8.2 API de legislação do Senado (alternativa)

Observado:
- `/legislacao/lista?tipo=LEI&ano=2023` devolveu 275 leis com os campos `numero`, `normaNome`, `ementa`, `dataassinatura` e `apelido`. A carga desde 1988 pode ser feita ano a ano.
- O detalhe de cada lei traz `ementa`, `classes`, `catalogo`, `indexacao`, `observacao`, `vides` (atos posteriores que afetam a lei), `edivs` (atos anteriores que a lei afeta) e `disps` (alterações por dispositivo).
- A Lei 8.080/1990 (Lei Orgânica da Saúde) está classificada em "Política Social / Saúde". Tem 43 declarações (31 de alteração permanente) e nenhuma de revogação no todo, o que é coerente com uma lei vigente e alterada.
- A Lei 8.666/1993 (licitações) tem a declaração "Revogação Permanente da Norma no Todo" pela Lei 14.133/2021, coerente com sua revogação.
- A Lei 13.675/2018 está em "Segurança Pública" e registra vetos.
- A Lei 12.741/2012, sobre a informação do valor dos tributos na nota fiscal, está classificada só em "Direito do Consumidor", e não em "Tributos". A Lei 8.666/1993 não tem classe nenhuma.

Limitações observadas e inferências:
- A data da declaração de revogação é a data de **assinatura** da norma revogadora (01/04/2021), e não a data em que a revogação produziu efeito. Pela Lei 14.133, a Lei 8.666 continuou aplicável por um período de transição. Inferência: datas de efeito precisam de curadoria.
- O campo `observacao` traz o autor do projeto com partido, por exemplo "AUTOR: DEPUTADO LUIZ ROBERTO PONTE (PMDB/RS)". Pelo princípio de conteúdo antes da autoria, esse campo não pode aparecer na camada visível.
- O campo `observacao` também registra decisões do STF em texto livre, por exemplo "interpretação conforme" na ADI 1923. Inferência: a inconstitucionalidade declarada pelo STF não aparece como dado estruturado de vigência.
- A ausência de declaração de revogação não prova que a lei esteja vigente, porque a revogação tácita (por incompatibilidade com lei posterior) não é declarada. A interface deveria dizer "sem registro de revogação no acervo do Senado", e não "vigente". Esta é uma proposta de texto, a validar.
- A consulta a `lei/5172/1966` (Código Tributário Nacional) respondeu HTTP 503 em 27/10/2026. Pode ser instabilidade pontual. Fica para novo teste.

### 8.3 Consequência para a funcionalidade "leis vigentes"

Inferência: a API do Senado sustenta a lista de leis, com ementa e um indicador estruturado de revogação no todo. Classificação temática e vigência precisam de curadoria, coerente com a fila de revisão já decidida. A mudança de fonte, do LexML e do Planalto para a API do Senado na coleta, com LexML e Planalto mantidos como link, é uma decisão a validar.

# Parte IV — Regimentos e nota de arquivamento

## 9. Situação

| Item | Situação | Observação |
|---|---|---|
| RICD art. 105 (texto vigente) | **Não confirmado** | O único texto acessível é um PDF do site da Câmara, com metadado "RICD 2004 com atualizações até res. 23-2004", gerado em 2005. Não serve como versão vigente. |
| Alterações do RICD art. 105 | **Não verificável por esta via** | O acervo do Senado não registra alterações de dispositivos da Resolução da Câmara 17/1989 (0 dispositivos com referência). |
| RISF art. 332 (texto vigente) | **Não confirmado** | O texto compilado está em `normas.leg.br`, não liberado neste ambiente. |
| Alterações do RISF art. 332 | **Observado** | Última alteração registrada: Resolução do Senado nº 17/2002. Regulamentado pelo Ato da Mesa nº 2/2014. |
| Fundamento do voto secreto | **Pendente** | Será confirmado no texto oficial da Constituição e do RISF. |

Para concluir esta parte, é preciso liberar dois domínios na política de rede do ambiente:
- `normas.leg.br`: textos compilados oficiais do RICD, do RISF e das leis;
- `www2.camara.leg.br`: página da Câmara com o RICD atualizado.

## 10. Texto de referência (edição de 2004, não confirmada como vigente)

Citação literal do PDF `regInterno.pdf` (site da Câmara, consultado em 27/10/2026), que **não** deve ser usada na interface até a confirmação:

> "Art. 105. Finda a legislatura, arquivar-se-ão todas as proposições que no seu decurso tenham sido submetidas à deliberação da Câmara e ainda se encontrem em tramitação, bem como as que abram crédito suplementar, com pareceres ou sem eles, salvo as: I - com pareceres favoráveis de todas as Comissões; II - já aprovadas em turno único, em primeiro ou segundo turno; III - que tenham tramitado pelo Senado, ou dele originárias; IV - de iniciativa popular; V - de iniciativa de outro Poder ou do Procurador-Geral da República. Parágrafo único. A proposição poderá ser desarquivada mediante requerimento do Autor, ou Autores, dentro dos primeiros cento e oitenta dias da primeira sessão legislativa ordinária da legislatura subseqüente, retomando a tramitação desde o estágio em que se encontrava."

Cruzamento preliminar das exceções desta edição com os campos da API da Câmara (inferência, a refazer com o texto vigente):

| Exceção (edição 2004) | Campo disponível | Verificação automática? |
|---|---|---|
| I. Pareceres favoráveis de todas as comissões | Tramitações com "parecer" em texto | Não, exige leitura do texto |
| II. Já aprovadas em turno único, 1º ou 2º turno | Votações e tramitações | Parcial |
| III. Tramitaram pelo Senado ou vieram dele | Tipo de autor ("Órgão do Poder Legislativo – Senado") e numeração | Sim, em boa parte |
| IV. Iniciativa popular | Tipo de autor | Provável, ainda não testado |
| V. Iniciativa de outro Poder ou do PGR | Tipo de autor ("Órgão do Poder Executivo") | Sim |

## 11. Pendências das Partes III e IV

1. ~~Validar a troca da fonte de coleta de leis (seção 8.3).~~ Decidido em 27/10/2026: coleta pela API do Senado; LexML e Planalto apenas como link.
2. Validar o texto de interface "sem registro de revogação no acervo do Senado" no lugar de "vigente" (seção 8.2).
3. Liberar `normas.leg.br` e `www2.camara.leg.br` e então confirmar o texto vigente do RICD art. 105, do RISF art. 332 e o fundamento do voto secreto (seção 9).
