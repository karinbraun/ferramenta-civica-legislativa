# Polo 2 — Entrega para validação

Etapa 2 (temas e rótulos), análise de conteúdo dos 14 programas de governo à Presidência protocolados no TSE em 2026. Livro de códigos v1.8. Documento gerado em 28/10/2026. Os números saem dos arquivos de codificação, lidos pelo script `etapa2/scripts/incidencia_polo2.py`; os dados brutos estão em `etapa2/codificacao/incidencia-polo2.json`.

Este documento não testa a hipótese dos 3 temas nem propõe rótulos. Isso fica para o Polo 3, depois da sua validação.

## Síntese

1. **Codificação concluída.** São 14 programas e 851 unidades nos 3 temas da hipótese: 714 propostas, 122 diagnósticos e 15 unidades de balanço de gestão. Os demais temas tiveram só a presença registrada, com as páginas.
2. **Os 3 temas da hipótese estão entre os mais frequentes.** Segurança (SEG) e saúde (SAU) aparecem nos 14 programas. Impostos e custo de vida (IMP) aparece em 13; está ausente só no DC. Os três estão nos dois programas do 2º turno (PT e PL).
3. **Aviso antes do Polo 3: o critério aprovado discrimina pouco.** O critério "8 ou mais programas e presença em PT e PL" é cumprido por 27 dos 31 temas presentes no corpus, e não só pelos 3 da hipótese. Ficam de fora apenas Direito Civil, Defesa do Consumidor, Processo Legislativo e Turismo. Outros 6 temas também chegam a 14 de 14: administração pública, economia, educação, energia, trabalho e transporte. Para escolher entre os temas, o Polo 3 precisa de critério adicional, como volume de propostas, competência ou volume de dados na Câmara. Isso é decisão sua (ver seção 7).
4. **Volume desigual.** São 329 propostas em SEG, 255 em SAU e 130 em IMP. Em IMP, o programa do MISSÃO tem só 2 propostas, ambas intenções genéricas ("redução de impostos"), e o do DC não tem nenhuma unidade.
5. **Dentro de cada tema, o conteúdo diverge mais do que a presença.** Em SEG, a mudança de lei penal (SEG.PENAL) aparece em 13 programas, mas em direções opostas: endurecer penas e classificar facções como terroristas em uns, descriminalizar e desencarcerar em outros. Em IMP, a estrutura tributária (IMP.TRIB) está em 13 programas, também em direções opostas: tributar grandes fortunas e altas rendas, ou reduzir e unificar tributos. Em SAU, a convergência é maior; filas e acesso (SAU.ACESSO) aparecem em 13 programas.
6. **Estabilidade da codificação.** Houve duas rodadas de reteste, com concordância de 0,90 e 0,92 (kappa 0,88 e 0,92). Não houve segundo codificador; essa limitação deve ser declarada no relatório.

Legenda dos programas, na ordem de codificação: PCO = Rui Costa Pimenta; DC = Clariana Barao; PCB = Edmilson Costa; Marçal = Pablo Marçal (PRTB); PSTU = Hertz Dias; DEM = Veterinário Wilson Grassi (DEMOCRATA); MISSÃO = Renan Santos; NOVO = Zema; UP = Samara; Avalanche = Leonardo Avalanche (PRTB); PL = Flavio Bolsonaro; PT = Lula; AVANTE = Escritor Augusto Cury; PSD = Ronaldo Caiado. A situação do registro de cada candidatura está no Polo 1 (`polo1-pre-analise.md`). Dois programas são do PRTB (Marçal e Avalanche), e os dois foram mantidos, conforme a decisão de incluir todos os programas protocolados.

## 1. Grade final

A grade completa, com definições, regras e histórico, está em `livro-de-codigos.md` (v1.8). Ela tem três camadas:

| Camada | Categorias | Codificação |
|---|---|---|
| Temas da hipótese | SEG (8 subcódigos: CRIME, POL, PENAL, VIOL, ARMAS, FED, PREV, DIAG); IMP (4: TRIB, PRECO, JUROS, DIAG); SAU (7: ACESSO, FIN, PROF, PUBPRIV, ESP, TEC, DIAG) | Fina: trecho literal, página, seção, subcódigo |
| Temas da Câmara | 30 temas da classificação oficial (`codTema`). O tema 43 (Direito Penal) e a parte de segurança do tema 57 foram incorporados a SEG | Só presença, com páginas |
| Categoria emergente | E-CORR (combate à corrupção, integridade, privilégios), aberta no 2º programa | Só presença, com páginas |

Mudanças da v1.8, feitas depois do reteste da rodada 2 (detalhes em `reteste.md`):

- todo diagnóstico vai para DIAG, com o objeto anotado;
- a regra do preço passa a valer só para bens de consumo geral;
- SEG.PREV e SEG.PENAL deixam de se sobrepor;
- centrais integradas de segurança vão para SEG.PREV.

Mudaram de código 38 unidades. Nenhuma presença de tema mudou.

Correções feitas na preparação desta entrega:

- o total de temas declarado em 9 arquivos tinha erro de soma, e as tabelas de presença não mudaram;
- duas ausências não classificadas foram conferidas no texto: E-CORR no PCO e T51 no Avalanche.

## 2. Incidência tema × programa (N/14)

Presença = pelo menos uma unidade programática sobre o tema (proposta, diagnóstico ou balanço). Nenhuma candidatura recebe rótulo de campo; PT e PL aparecem em colunas próprias só porque o critério aprovado usa o 2º turno.

| Tema | Código | N/14 | PT | PL | Ausente em |
|---|---|---|---|---|---|
| Saúde pública (hipótese) | SAU | 14 | Sim | Sim |  |
| Segurança e combate ao crime (hipótese) | SEG | 14 | Sim | Sim |  |
| Administração Pública | T34-ADM | 14 | Sim | Sim |  |
| Economia | T40-ECO | 14 | Sim | Sim |  |
| Educação | T46-EDU | 14 | Sim | Sim |  |
| Energia, Recursos Hídricos e Minerais | T54-ENER | 14 | Sim | Sim |  |
| Trabalho e Emprego | T58-TRAB | 14 | Sim | Sim |  |
| Viação, Transporte e Mobilidade | T61-TRANS | 14 | Sim | Sim |  |
| Combate à corrupção (emergente) | E-CORR | 13 | Sim | Sim | PCO |
| Impostos e custo de vida (hipótese) | IMP | 13 | Sim | Sim | DC |
| Cidades e Desenvolvimento Urbano | T41-CID | 13 | Sim | Sim | DC |
| Previdência e Assistência Social | T52-PREV | 13 | Sim | Sim | DEM |
| Ciência, Tecnologia e Inovação | T62-CTI | 13 | Sim | Sim | PCO |
| Indústria, Comércio e Serviços | T66-IND | 13 | Sim | Sim | PCO |
| Finanças Públicas e Orçamento | T70-FIN | 13 | Sim | Sim | Avalanche |
| Comunicações | T37-COM | 12 | Sim | Sim | PSTU, DEM |
| Direitos Humanos e Minorias | T44-DH | 12 | Sim | Sim | PCO, DEM |
| Meio Ambiente | T48-AMB | 12 | Sim | Sim | PCO, DC |
| Estrutura Fundiária | T51-FUND | 12 | Sim | Sim | DC, Avalanche |
| Relações Internacionais | T55-RI | 12 | Sim | Sim | DC, Avalanche |
| Agricultura e Pecuária | T64-AGRO | 12 | Sim | Sim | PCO, DC |
| Arte, Cultura e Religião | T35-CULT | 10 | Sim | Sim | DC, PSTU, DEM, Avalanche |
| Esporte e Lazer | T39-ESP | 9 | Sim | Sim | DC, PCB, PSTU, MISSÃO, AVANTE |
| Defesa | T57-DEF | 9 | Sim | Sim | PCO, DC, PSTU, UP, AVANTE |
| Direito Constitucional | T68-CONST | 9 | Sim | Sim | PCO, Marçal, PSTU, UP, Avalanche |
| Política, Partidos e Eleições | T74-POL | 9 | Sim | Sim | DC, Marçal, PSTU, DEM, Avalanche |
| Direito e Justiça | T76-JUS | 9 | Sim | Sim | DC, Marçal, DEM, MISSÃO, PSD |
| Processo Legislativo | T53-PLEG | 7 | Sim | Sim | PCO, DC, PCB, Marçal, PSTU, Avalanche, AVANTE |
| Turismo | T60-TUR | 6 | Sim | Sim | PCO, DC, PCB, PSTU, DEM, MISSÃO, UP, Avalanche |
| Direito Civil | T42-CIV | 1 | Não | Não | PCO, DC, PCB, PSTU, DEM, MISSÃO, NOVO, UP, Avalanche, PL, PT, AVANTE, PSD |
| Defesa do Consumidor | T67-CONS | 1 | Não | Não | PCO, DC, PCB, Marçal, DEM, MISSÃO, NOVO, UP, Avalanche, PL, PT, AVANTE, PSD |
| (improvável em programas) | T72-HOM | 0 | Não | Não | todos |
| (improvável em programas) | T85-EXA | 0 | Não | Não | todos |
| (improvável em programas) | T86-HUM | 0 | Não | Não | todos |

## 3. Matriz de rastreabilidade (tema × programa)

● = presente; · = ausente. As páginas e a justificativa de cada célula estão na tabela de presença do arquivo de cada programa, em `programas/`.

| Código | PCO | DC | PCB | Marçal | PSTU | DEM | MISSÃO | NOVO | UP | Avalanche | PL | PT | AVANTE | PSD | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SAU | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| SEG | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| T34-ADM | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| T40-ECO | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| T46-EDU | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| T54-ENER | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| T58-TRAB | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| T61-TRANS | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 14 |
| E-CORR | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 13 |
| IMP | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 13 |
| T41-CID | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 13 |
| T52-PREV | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | 13 |
| T62-CTI | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 13 |
| T66-IND | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 13 |
| T70-FIN | ● | ● | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | 13 |
| T37-COM | ● | ● | ● | ● | · | · | ● | ● | ● | ● | ● | ● | ● | ● | 12 |
| T44-DH | · | ● | ● | ● | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | 12 |
| T48-AMB | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 12 |
| T51-FUND | ● | · | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | 12 |
| T55-RI | ● | · | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | 12 |
| T64-AGRO | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 12 |
| T35-CULT | ● | · | ● | ● | · | · | ● | ● | ● | · | ● | ● | ● | ● | 10 |
| T39-ESP | ● | · | · | ● | · | ● | · | ● | ● | ● | ● | ● | · | ● | 9 |
| T57-DEF | · | · | ● | ● | · | ● | ● | ● | · | ● | ● | ● | · | ● | 9 |
| T68-CONST | · | ● | ● | · | · | ● | ● | ● | · | · | ● | ● | ● | ● | 9 |
| T74-POL | ● | · | ● | · | · | · | ● | ● | ● | · | ● | ● | ● | ● | 9 |
| T76-JUS | ● | · | ● | · | ● | · | · | ● | ● | ● | ● | ● | ● | · | 9 |
| T53-PLEG | · | · | · | · | · | ● | ● | ● | ● | · | ● | ● | · | ● | 7 |
| T60-TUR | · | · | · | ● | · | · | · | ● | · | · | ● | ● | ● | ● | 6 |
| T42-CIV | · | · | · | ● | · | · | · | · | · | · | · | · | · | · | 1 |
| T67-CONS | · | · | · | · | ● | · | · | · | · | · | · | · | · | · | 1 |
| T72-HOM | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 0 |
| T85-EXA | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 0 |
| T86-HUM | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 0 |
| Total de temas | 19 | 16 | 26 | 26 | 22 | 22 | 26 | 29 | 26 | 21 | 29 | 29 | 26 | 28 | — |

## 4. Unidades dos temas da hipótese

### 4.1 Propostas, diagnósticos e balanço por programa

"prop." = proposta; "diag." = diagnóstico sem proposta; "bal." = relato de gestão já realizada (marca [balanço], v1.7). As repetições estão incluídas (marca "(rep.)" nos arquivos). Unidades reclassificadas para fora de IMP pela v1.8 não entram na contagem.

| Programa | SEG prop. | SEG diag. | SEG bal. | IMP prop. | IMP diag. | IMP bal. | SAU prop. | SAU diag. | SAU bal. |
|---|---|---|---|---|---|---|---|---|---|
| PCO | 6 | 0 | 0 | 5 | 2 | 0 | 6 | 0 | 0 |
| DC | 7 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 |
| PCB | 14 | 0 | 0 | 6 | 0 | 0 | 15 | 0 | 0 |
| Marçal | 16 | 0 | 0 | 7 | 2 | 0 | 9 | 0 | 0 |
| PSTU | 27 | 3 | 0 | 7 | 4 | 0 | 10 | 2 | 0 |
| DEM | 37 | 4 | 0 | 20 | 4 | 0 | 16 | 3 | 0 |
| MISSÃO | 26 | 7 | 0 | 2 | 2 | 0 | 11 | 2 | 0 |
| NOVO | 21 | 6 | 0 | 17 | 4 | 0 | 24 | 5 | 0 |
| UP | 18 | 10 | 0 | 6 | 5 | 0 | 7 | 9 | 0 |
| Avalanche | 18 | 5 | 0 | 12 | 7 | 0 | 13 | 5 | 0 |
| PL | 25 | 2 | 0 | 19 | 7 | 1 | 17 | 1 | 0 |
| PT | 25 | 2 | 1 | 10 | 0 | 9 | 30 | 1 | 3 |
| AVANTE | 32 | 2 | 0 | 8 | 1 | 0 | 25 | 3 | 0 |
| PSD | 57 | 7 | 1 | 11 | 3 | 0 | 65 | 2 | 0 |
| Total | 329 | 48 | 2 | 130 | 41 | 10 | 255 | 33 | 3 |
| Programas com ao menos 1 proposta | 14 | | | 13 | | | 14 | | |

[INFERÊNCIA] O volume reflete também o tamanho e o formato dos documentos, e não só a ênfase temática. O programa do PSD tem 100 páginas e um capítulo de saúde com 15 ações; o do DC tem 15 páginas em lista fragmentária. Por isso, o volume serve para comparar temas dentro de um mesmo programa, e não para ordenar programas.

### 4.2 Propostas por subcódigo

N/14 = número de programas com pelo menos uma proposta no subcódigo (sem diagnósticos e balanço). As colunas PT e PL trazem o número de unidades.

| Subcódigo | N/14 com proposta | Unidades | PT | PL | Ausente em |
|---|---|---|---|---|---|
| IMP.JUROS | 7 | 21 | 2 | 6 | DC, PCB, PSTU, DEM, MISSÃO, UP, Avalanche |
| IMP.PRECO | 11 | 42 | 5 | 10 | DC, PSTU, MISSÃO |
| IMP.TRIB | 13 | 67 | 3 | 3 | DC |
| SAU.ACESSO | 13 | 38 | 7 | 2 | UP |
| SAU.ESP | 13 | 105 | 14 | 8 | PCO |
| SAU.FIN | 10 | 24 | 1 | 1 | DC, DEM, UP, Avalanche |
| SAU.PROF | 10 | 14 | 1 | 0 | DC, Marçal, MISSÃO, PL |
| SAU.PUBPRIV | 9 | 16 | 1 | 1 | DC, Marçal, DEM, MISSÃO, PSD |
| SAU.TEC | 13 | 58 | 6 | 5 | PCO |
| SEG.ARMAS | 5 | 9 | 1 | 0 | DC, PCB, Marçal, MISSÃO, UP, Avalanche, PL, AVANTE, PSD |
| SEG.CRIME | 11 | 60 | 6 | 7 | PCO, UP, Avalanche |
| SEG.FED | 11 | 37 | 4 | 2 | PCO, DC, Marçal |
| SEG.PENAL | 13 | 77 | 3 | 9 | PCO |
| SEG.POL | 14 | 32 | 1 | 2 | — |
| SEG.PREV | 12 | 48 | 5 | 1 | PCO, PSTU |
| SEG.VIOL | 13 | 66 | 5 | 4 | MISSÃO |

Silêncios a registrar [observação sobre o dado]:

- **Armas de fogo (SEG.ARMAS):** só 5 programas têm proposta. O programa do PL não tem nenhuma; a única ocorrência de "armas" no texto é "armas de guerra" da tropa de fronteira (p. 13–14), codificada em SEG.CRIME. Busca de "armas", "arma de fogo", "porte" e "legítima defesa" feita em 28/10/2026.
- **Juros e endividamento (IMP.JUROS):** 7 programas.
- **IMP no DC:** nenhuma ocorrência de "impost", "tribut", "preç", "inflaç", "custo de vida" ou "juro" (conferido na codificação, 27/10/2026).

## 5. Verbatins

Todos os trechos são [LITERAL], com a unidade e a página. A seleção mostra a variação dentro de cada tema e inclui os dois programas do 2º turno. Não é amostra representativa.

### SEG — Segurança e combate ao crime

Convergência [PARÁFRASE]: todos os programas tratam o crime organizado ou a violência como problema nacional. A maioria pede mais atuação da União, embora a segurança seja competência majoritariamente estadual.

Divergência [PARÁFRASE]: há duas direções opostas. Uma é endurecer a lei penal e classificar facções como organizações terroristas (PL, PSD, NOVO). A outra é descriminalizar drogas, desencarcerar e desmilitarizar as polícias (PCB, PSTU, UP). Os demais programas combinam medidas de inteligência, integração e prevenção.

| Unidade | Pág. | Trecho [LITERAL] | Código |
|---|---|---|---|
| FLA-S3 (PL) | 13 | "Vamos declarar guerra ao crime organizado. PCC, CV, milícias e todas as outras facções serão declaradas como organizações narcoterroristas." | SEG.PENAL |
| LUL-S26 (PT) | 30 | "Construiremos, junto com os entes federados, programas no modelo de policiamento de proximidade [...]. Ampliaremos o programa de estímulos para uso de câmeras corporais [...]. Estimularemos o fortalecimento dos mecanismos de controle interno e externo da atividade policial." | SEG.POL |
| PCB-S12 (PCB) | 12 | "Descriminalização do uso de drogas, com legalização da maconha a curto prazo." | SEG.PENAL |
| SAM-S22 (UP) | 48 | "Fim da Política de “Guerra às Drogas”: Transição do paradigma penal para o paradigma de saúde pública e prevenção, atacando a lavagem de dinheiro das grandes organizações criminosas no sistema financeiro." | SEG.FED |
| GRA-S2 (DEM) | 4 | "Segurança pública é competência dividida com os estados." | SEG.FED |
| CAI-S1 (PSD) | 2 | "Segurança pública será responsabilidade direta da Presidência da República." | SEG.FED |

[INFERÊNCIA para o Polo 3] GRA-S2 e CAI-S1 tratam da mesma divisão de competências por ângulos opostos, um reconhecendo o limite e o outro centralizando. Isso é material para a nota educativa de competência (funcionalidade 5 do briefing).

### IMP — Impostos e custo de vida

Convergência [PARÁFRASE]: a crítica ao peso dos tributos sobre o consumo e sobre quem ganha pouco aparece em programas de orientações opostas (por exemplo, UP, SAM-I5, e DEM, GRA-I18). Não foi verificada nos 13.

Divergência [PARÁFRASE]: os remédios propostos são opostos. Um grupo propõe tributar grandes fortunas, lucros e altas rendas (PSTU, PCO, PCB, UP e, em balanço, PT). Outro propõe reduzir, unificar ou substituir tributos (Avalanche, DEM, PL, NOVO); o PSD se compromete a não aumentar a carga (CAI-I1). A UP combina as duas coisas: "Queremos redução de impostos, tributação das fortunas e redução da jornada de trabalho" (SAM-I6, p. 16). O preço ao consumidor (IMP.PRECO) aparece em 11 programas, sobretudo energia e alimentos.

| Unidade | Pág. | Trecho [LITERAL] | Código |
|---|---|---|---|
| FLA-I2 (PL) | 11 | "Brasil Mais Barato, para sobrar dinheiro no fim do mês: Menos imposto no que a família consome, conta de luz mais simples e mais barata, custo de transporte menor na prateleira do supermercado e crédito que não afunda o orçamento." | IMP.PRECO (síntese) |
| LUL-I8 (PT) | 49 | "A inflação baixa e a estabilidade de preços são pressupostos fundamentais do nosso governo. Manteremos a inflação sob controle de forma duradoura e sustentável, garantindo que a renda real da população cresça acima do custo de vida." | IMP.PRECO |
| LUL-I1 (PT) | 10 | "Sob a diretriz de “colocar o pobre no orçamento e o rico no Imposto de Renda”, a gestão realizou uma profunda reorganização fiscal [...]" | IMP.DIAG [balanço] |
| PST-I9 (PSTU) | 27 | "Imposto progressivo sobre as verdadeiras grandes fortunas, o topo da pirâmide, os que possuem de R$ 1 bilhão para cima." | IMP.TRIB |
| AVA-I1 (Avalanche) | 4 | "Nossa proposta é reduzir toda essa avalanche de impostos que pesa sobre o brasileiro pra uma alíquota única de 3,5%. Nada de ICMS, ISS, PIS, Cofins, IPI, INSS, Imposto de Renda separados — um imposto só, pra tudo." | IMP.TRIB |
| SAM-I5 (UP) | 16 | "quando um trabalhador compra arroz, feijão ou pão, paga o mesmo imposto que um rico ao comprar o mesmo produto." | IMP.DIAG |

Vocabulário [contagem no texto, com espaço normalizado, 28/10/2026]:

| Expressão | Programas em que aparece |
|---|---|
| "custo de vida" | 6 (PCO, PSTU, UP, PT, AVANTE, PSD); ausente no PL |
| "mais barato(a)" | 5 (NOVO, PSTU, PL 15 vezes, PSD, Avalanche 12 vezes); ausente no PT |
| "carga tributária" | 7 (Marçal, MISSÃO, NOVO, DEM, AVANTE, PSD, Avalanche 7 vezes); ausente em PT e PL |
| "justiça tributária" | 2 (PT 4 vezes, MISSÃO) |
| "grandes fortunas" | 4 (PCO, PCB, PSTU, UP) |

[INFERÊNCIA para o Polo 3] Nenhuma dessas expressões aparece nos dois programas do 2º turno. Isso pesa contra usar qualquer uma delas, isoladamente, como rótulo. O rótulo atual do briefing, "impostos e custo de vida", combina um termo transversal ("impostos") com um termo ausente no PL.

### SAU — Saúde pública

Convergência [PARÁFRASE]: a fila e o tempo de espera são o problema mais compartilhado. A palavra "fila(s)" aparece em 13 dos 14 programas (ausente no PCO), com maior frequência no PL (29 vezes), PSD (21), DEM (16) e NOVO (15) [contagem no texto, 28/10/2026].

Divergência [PARÁFRASE]: a relação público-privado divide os programas. Uns defendem um sistema inteiramente público. PSTU e UP usam a expressão "SUS 100% estatal" (PST-H3; SAM-H9, que pede também o fim das organizações sociais). O PCB diz que "tornará público todo o sistema de saúde" (PCB-H1, p. 6). No PCB e no PCO, "100% estatal" se refere à Petrobras. Outros propõem usar a capacidade do setor privado (NOVO, PSD).

| Unidade | Pág. | Trecho [LITERAL] | Código |
|---|---|---|---|
| ZEM-H1 (NOVO) | 57 | "Três em cada quatro brasileiros dependem exclusivamente do SUS e, muitas vezes, o que encontram é fila: fila para consultas, exames e cirurgias que não podem esperar." | SAU.DIAG |
| GRA-H13 (DEM) | 34 | "Fila nacional única e pública por procedimento, com critério clínico de prioridade e posição consultável pelo próprio paciente." | SAU.ACESSO |
| FLA-H14 (PL) | 38 | "Com a telessaúde e o teleatendimento por aplicativo, médicos de regiões com baixa demanda poderão atender pacientes onde as filas são longas" | SAU.TEC |
| LUL-H9 (PT) | 34–35 | "Seguiremos mantendo o apoio à expansão e qualificação das equipes de saúde da família, em especial as equipes multiprofissionais [...]" | SAU.ACESSO |
| PST-H3 (PSTU) | 11 | "Defesa do sus público, universal, gratuito e 100% estatal" | SAU.PUBPRIV |
| ZEM-H5 (NOVO) | 57 | "O setor privado, que tem estrutura e capacidade ociosa, é subutilizado para desafogar o sistema público" | SAU.DIAG |

## 6. Limitações

- **Um só codificador.** O reteste mede estabilidade, não confiabilidade entre codificadores. Na rodada 2, a amostra incluiu 18 unidades de Caiado, codificadas pouco antes; fora delas, a concordância foi de 0,90.
- **Codificação fina só em 3 temas.** Os outros 28 temas têm só presença, o que basta para o critério de incidência, mas não permite comparar volume entre eles e os 3 da hipótese.
- **Presença é binária.** Uma única unidade conta tanto quanto um capítulo inteiro. O IMP do MISSÃO ("Sim (fraco)") ilustra isso.
- **Formato dos documentos.** Os programas vão de 15 a mais de 190 páginas e misturam lista, prosa e infográfico (com páginas em imagem transcritas). O volume de unidades depende disso.
- **Fronteiras de codificação.** As regras v1.1 a v1.8 resolvem casos de fronteira (lei penal, preço, Forças Armadas, diagnóstico), mas outra pessoa poderia decidir de outro modo. Os casos estão marcados [fronteira] nos arquivos.
- **SEG abriga temas de direitos.** Pela regra da lei penal, criminalização da misoginia, aborto e drogas entram em SEG.PENAL. Isso afeta o rótulo e deve ser discutido no Polo 3.
- **Corpus restrito à Presidência.** Os programas falam de competências federais e estaduais misturadas, e não refletem a agenda de governadores e prefeitos.

## 7. Decisões pendentes para o Polo 3

1. **Critério adicional de escolha dos temas**, porque o critério aprovado é cumprido por 27 temas (síntese, item 3).
2. Se a regra da lei penal (aborto, drogas e misoginia em SEG) se mantém para fins de rótulo ou se esses itens devem ser tratados à parte na interface.
3. Se o protótipo deve considerar os 6 outros temas com 14 de 14 (administração, economia, educação, energia, trabalho e transporte) como alternativas ou como segunda rodada. Trabalho e educação já estão previstos para a segunda rodada no briefing.
