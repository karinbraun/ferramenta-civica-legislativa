# Etapa 2 — Polo 1: pré-análise

Análise de conteúdo categorial (Bardin), aplicada aos programas de governo das candidaturas à Presidência em 2026. Data: 27/10/2026.

## 1. Objetivo

Responder a três perguntas, nesta ordem:

1. Quais temas aparecem nos programas de governo e com que incidência (em quantos dos 14 programas)?
2. Os 3 temas da hipótese do briefing (segurança e combate ao crime; impostos e custo de vida; saúde pública) estão presentes em programas de orientações diferentes?
3. Como cada candidatura nomeia esses temas? O vocabulário serve para propor rótulos que não pertençam a um campo político só.

Fora do escopo: avaliar a qualidade, a viabilidade ou o mérito das propostas.

## 2. Corpus

Fonte: TSE, dados abertos, conjunto "Candidatos - 2026", arquivo `proposta_governo_2026_BR.zip` (baixado em 27/10/2026, SHA-256 e URLs em `etapa2/corpus/manifesto.json`). A situação do registro vem de `consulta_cand_complementar_2026.zip`, campo `DS_SITUACAO_JULGAMENTO`, e o resultado vem de `consulta_cand_2026.zip`, campo `DS_SIT_TOT_TURNO`. Os dois estão transcritos literalmente.

| Candidatura (nome de urna) | Partido | Situação do registro | Resultado | Páginas | Caracteres | Arquivo |
|---|---|---|---|---|---|---|
| Samara | UP | DEFERIDO | 1º: NÃO ELEITO | 67 | 156.890 | `2026BR280002538811_01.pdf` |
| Zema | NOVO | DEFERIDO | 1º: NÃO ELEITO | 81 | 151.268 | `2026BR280002539826_01.pdf` |
| Renan Santos | MISSÃO | DEFERIDO | 1º: NÃO ELEITO | 51 | 147.376 | `2026BR280002540694_01.pdf` |
| Hertz Dias | PSTU | DEFERIDO | 1º: NÃO ELEITO | 33 | 114.529 | `2026BR280002541457_01.pdf` |
| Lula | PT | DEFERIDO | 1º: 2º TURNO / 2º: ELEITO | 84 | 180.970 | `2026BR280002542548_01.pdf` |
| Veterinário Wilson Grassi | DEMOCRATA | DEFERIDO | 1º: NÃO ELEITO | 58 | 125.726 | `2026BR280002548139_01.pdf` |
| Flavio Bolsonaro | PL | DEFERIDO | 1º: 2º TURNO / 2º: NÃO ELEITO | 76 | 178.710 | `2026BR280002551544_01.pdf` |
| Escritor Augusto Cury | AVANTE | DEFERIDO | 1º: NÃO ELEITO | 200 | 314.477 | `2026BR280002551547_01.pdf` |
| Ronaldo Caiado | PSD | DEFERIDO | 1º: NÃO ELEITO | 100 | 323.705 | `2026BR280002551932_01.pdf` |
| Edmilson Costa | PCB | DEFERIDO | 1º: NÃO ELEITO | 16 | 52.187 | `2026BR280002551975_01.pdf` |
| Clariana Barao | DC | DEFERIDO | 1º: NÃO ELEITO | 15 | 16.657 | `2026BR280002552484_01.pdf` |
| Rui Costa Pimenta | PCO | DEFERIDO | 1º: NÃO ELEITO | 7 | 17.406 | `2026BR280002552487_01.pdf` |
| Pablo Marçal | PRTB | INDEFERIDO | 1º: #NULO | 28 | 42.117 | `2026BR280002553884_01.pdf` |
| Leonardo Avalanche | PRTB | RENÚNCIA | 1º: NÃO ELEITO | 48 | 167.224 | `2026BR280002554479_01.pdf` |

O cadastro do TSE tem 14 candidaturas à Presidência e há 14 programas, um por candidatura (o 15º arquivo do zip é o `leiame.pdf` do TSE). Nenhuma candidatura ficou sem programa.

Inconsistência observada nos dados do TSE, registrada sem interpretação: Leonardo Avalanche aparece com situação de julgamento "RENÚNCIA" e resultado "NÃO ELEITO" no 1º turno. Pelo campo `SQ_SUBSTITUIDO`, ele é o substituto de Pablo Marçal (registro "INDEFERIDO", `ST_SUBSTITUIDO = S`). Os dois programas ficam no corpus, conforme a decisão de 27/10.

## 3. As quatro regras de constituição do corpus

| Regra | Verificação | Resultado |
|---|---|---|
| **Exaustividade** | Todos os programas protocolados entram. 14 de 14 candidaturas do cadastro têm programa. | Atendida |
| **Representatividade** | Não há amostragem: o corpus é o universo dos programas à Presidência. Não representa candidaturas a governador, deputado ou senador, nem a opinião do eleitorado. | Atendida para o universo definido. Limite de generalização registrado. |
| **Homogeneidade** | Mesmo gênero documental (programa protocolado no TSE), mesmo cargo, mesma eleição. Mas a extensão varia de 7 páginas (PCO) a 200 (Avante), e o formato vai de lista de propostas a ensaio (Avante, p. 3–35) e infográfico (PRTB/Marçal). | Parcial. Por isso a incidência será medida por **presença no programa** (N de 14), e não por contagem bruta de trechos, que favoreceria os programas longos. |
| **Pertinência** | Os programas são a fonte indicada no briefing para os rótulos. | Atendida |

## 4. Qualidade do material

- Texto extraído com `pdftotext` por página, com marcador `===== PÁGINA n =====` (`etapa2/corpus/txt/`). A média é de 1.090 a 3.463 caracteres por página.
- Páginas sem texto extraível (menos de 100 caracteres): 50 no total. A maioria é capa ou separador. Algumas, porém, têm conteúdo substantivo em imagem. Exemplo: o programa de Pablo Marçal, p. 10, é um infográfico com diagnóstico e eixos de governo. Não há OCR no ambiente. Essas páginas serão lidas como imagem e transcritas, com a marca [TRANSCRIÇÃO DE IMAGEM], e só entram na codificação se tiverem conteúdo programático.
- O texto extraído de alguns PDFs tem espaçamento irregular em títulos (por exemplo, "PRO GRAMA DE G OVERNO"). Nos verbatins, a grafia será corrigida só nesses espaços, sem alterar palavras.

## 5. Regras de recorte e codificação (propostas para o Polo 2)

- **Unidade de registro:** o trecho mínimo com sentido programático. Pode ser uma proposta ("o que fazer") ou um diagnóstico ("o que está errado"). Na prática, é um item de lista ou um período.
- **Unidade de contexto:** a seção ou capítulo do programa onde o trecho está, registrada junto com a página.
- **Grade mista:**
  - categorias a priori: os 32 temas oficiais da Câmara (Etapa 1);
  - categorias emergentes: abertas para o que não couber nos 32 (por exemplo, "custo de vida" e "preços", que a Câmara não tem como tema);
  - os 3 temas da hipótese recebem subcódigos para registrar o vocabulário (como cada programa nomeia o problema).
- **Medidas:** presença do tema em cada programa (sim ou não); número de unidades por tema e programa, só como indicador secundário; e o vocabulário dos temas da hipótese, com verbatins identificados (candidatura e página).
- **Marcação:** [LITERAL] para o texto do programa, [PARÁFRASE] para resumo meu e [INFERÊNCIA] para interpretação minha.
- **Escopo de leitura:** para identificar a presença dos 32 temas, todos os programas são lidos por inteiro. A codificação fina, com verbatim e vocabulário, se concentra nos 3 temas da hipótese, além de qualquer tema emergente com incidência alta.

## 6. Questão em aberto antes do Polo 2

O critério do briefing pede temas que "mobilizem eleitores dos dois campos". Para verificar isso, cada programa precisaria de um rótulo de campo político. Atribuir esse rótulo é um juízo com risco de viés. Opções, a decidir com a responsável pelo projeto:

1. **Não atribuir campo.** Usar como critério a presença do tema na maioria dos programas e nos programas das duas candidaturas do 2º turno.
2. **Usar uma classificação externa e citável** de posicionamento partidário (por exemplo, um survey acadêmico de especialistas), com a fonte declarada.
3. **Usar a autodeclaração** dos programas, quando ela existe (por exemplo, "socialista"), deixando os demais sem rótulo.
