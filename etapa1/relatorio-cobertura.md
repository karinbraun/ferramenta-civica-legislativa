# Relatório de cobertura das fontes — Etapa 1

Status: parcial. Esta versão cobre apenas a **API de Dados Abertos da Câmara dos Deputados**. Senado, LexML e regimentos entram nas próximas seções.

Convenções deste relatório:
- **Observado**: o que está nas respostas da API salvas em `etapa1/amostras/camara/`. Cada arquivo traz a URL, a data/hora da requisição e a resposta bruta.
- **Inferência**: interpretação minha, ainda não confirmada em documentação oficial ou por um segundo teste.

Execução: `python3 etapa1/scripts/sondagem_camara.py`, rodado em 26/10/2026. Foram 465 requisições, todas de leitura. O resumo está em `etapa1/amostras/camara/_resumo.json`.

Amostra: 5 projetos de lei por tema do protótipo, apresentados desde 01/02/2023, 15 no total. Também entraram as 100 votações do Plenário de novembro de 2025 e as 38 de 1º a 15 de julho de 2019.

## 1. Síntese

| Funcionalidade do briefing | Situação na API da Câmara | Observação principal |
|---|---|---|
| Temas oficiais como base da navegação | **Parcial** | Os temas existem, mas cada projeto pode ter vários e a classificação mistura assuntos distantes. "Impostos" não é um tema oficial. |
| Ementa oficial e link para a fonte | **Sustentado** | Campos `ementa` e `urlInteiroTeor`, mais a página pública do projeto. |
| Situação oficial da tramitação | **Sustentado** | Campo `descricaoSituacao`, com uma lista oficial de 99 situações. |
| Autoria (autores e coautores) | **Sustentado** | Nome, tipo de autor e ordem de assinatura. |
| Partido e UF do autor na data da proposição | **Parcial** | O endpoint de autores não traz partido. É possível calcular o partido pelo histórico do deputado. Projetos vindos do Senado não trazem partido nenhum. |
| Votos nominais por parlamentar e partido | **Sustentado** | O partido gravado no voto é o da época da votação (confirmado). |
| Orientação de bancada em votação simbólica | **Não sustentado** | Em 79 votações sem voto individual, nenhuma tinha orientação registrada. |
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

Inferência: a API só registra orientação de bancada quando há votação nominal. Nas votações simbólicas, as orientações dos líderes provavelmente ficam apenas nas notas taquigráficas ou no vídeo da sessão, sem dado estruturado. **Por isso, a funcionalidade 4 do briefing não pode mostrar a orientação de bancada nas votações simbólicas a partir desta fonte.** Essa decisão de produto está pendente.

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

1. Decidir o que fazer com a orientação de bancada em votações simbólicas (seção 2.1).
2. Validar o cálculo do partido em casos de mudança no meio da legislatura (seção 2.2).
3. Fechar as exceções do art. 105 do RICD que podem ser verificadas com os campos disponíveis, depois de confirmar o texto vigente (seção 2.4).
