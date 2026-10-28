# Livro de códigos — Etapa 2

Versão 1.8 (28/10/2026). As alterações feitas depois do reteste são registradas na seção "Histórico".

## Regras gerais

- **Unidade de registro:** o trecho mínimo com sentido programático. Pode ser uma proposta (o que fazer) ou um diagnóstico (o que está errado e por quê). Em geral é um item de lista ou um período.
- **Unidade de contexto:** a seção ou capítulo do programa, registrada junto com a página.
- **Lista fragmentária:** quando os itens de uma lista não têm sentido isolado (por exemplo, "Inteligência sobre rotas e redes"), a unidade de registro é a subseção inteira: o título e os itens.
- **Presença de um tema num programa:** pelo menos uma unidade programática sobre ele. Menção de passagem dentro de outra proposta, sem conteúdo próprio, não conta. Por exemplo, "destinar o petróleo à saúde e educação" conta para Energia, mas não para Saúde nem para Educação.
- **Criação ou revogação de lei penal** (criminalizar, descriminalizar, legalizar uma conduta hoje tipificada, mudar penas ou maioridade penal) vai para SEG.PENAL, mesmo quando a motivação é de outro tema. Exemplos: "Criminalização da misoginia"; "Legalização do aborto". Esses casos recebem a marca [fronteira], porque o mesmo conteúdo também se relaciona com T44 ou SAU. [INFERÊNCIA para o Polo 3] Como SEG incorpora o tema 43 da Câmara (Direito Penal), um rótulo como "segurança e combate ao crime" passa a abrigar temas de direitos e de saúde. Esse é um ponto a discutir na definição dos rótulos.
- **Saúde de grupos específicos:** uma proposta de serviço de saúde específico para um grupo (terapia hormonal, prevenção de ISTs, CAPS) vai para SAU. A menção genérica de "acesso à saúde" dentro de uma lista de direitos de um grupo vai para T44.
- **Objetivo explícito de preço:** quando uma proposta de outro tema (por exemplo, assistência ou abastecimento) declara de forma explícita o objetivo de reduzir ou controlar preços ao consumidor, a unidade recebe IMP.PRECO. O outro tema é registrado só como presença. A regra vale só para bens e serviços de consumo geral das famílias (alimentos, energia elétrica, combustíveis, gás de cozinha, tarifas públicas, inflação, custo de vida em geral). Preço de bem ou serviço setorial (moradia, telecomunicações, medicamentos, materiais para pessoas com deficiência, bens de capital, infraestrutura em geral) vai para o tema do setor (v1.8).
- **Diagnóstico:** toda unidade sem proposta (dados, constatações, críticas) recebe o subcódigo DIAG do tema, mesmo quando trata de um objeto específico. O objeto é anotado entre parênteses, por exemplo "SEG.DIAG (objeto: VIOL)". Assim, a contagem do Polo 3 separa propostas de diagnósticos sem perder o objeto (v1.8).
- **Incentivo tributário setorial:** isenções ou regimes tributários para um setor ou atividade específica (startups, datacenters, venture capital, games) vão para o tema do setor (T62, T66 etc.). Medidas tributárias gerais, ou para todos os pequenos e novos negócios, vão para IMP.TRIB.
- **Forças Armadas e fronteira:** uma ação das Forças Armadas (ou na fronteira) com finalidade declarada de combate ao crime (tráfico, contrabando, facções) vai para SEG, com subcódigo CRIME, PREV ou FED. A capacidade de defesa (orçamento, soldo, equipamento, indústria de defesa), ou a fronteira sem finalidade criminal declarada, vai para T57-DEF.
- **Balanço de gestão:** trecho que relata o que um governo já fez ("Recriamos", "Aprovamos", "No governo X, caiu...") é codificado pelo objeto, com subcódigo DIAG (ou o subcódigo do objeto, quando específico), e recebe a marca [balanço]. Conta para a presença do tema, mas é separado das propostas na contagem do Polo 3.
- **Repetição:** um conteúdo repetido no mesmo programa é codificado de novo e marcado "(rep.)". Conta para a contagem, mas não altera a presença.
- **Exclusão mútua:** cada unidade recebe **um** código principal, o do objeto central da proposta. Quando uma unidade cobre dois temas de forma substantiva, ela é dividida em duas unidades.
- **Codificação fina** (verbatim e subcódigo) só nos 3 temas da hipótese: SEG, IMP e SAU. Nos demais temas, registra-se só a presença, com as páginas.
- **Marcação:** [LITERAL] para texto do programa, [PARÁFRASE] para resumo meu, [INFERÊNCIA] para interpretação minha, [TRANSCRIÇÃO DE IMAGEM] para texto lido de página sem texto extraível.

## A. Temas da hipótese (codificação fina)

### SEG — Segurança e combate ao crime
Correspondência na Câmara: 57 Defesa e Segurança (só a parte de segurança pública) e 43 Direito Penal e Processual Penal.
Inclui: crime, violência, polícias, sistema prisional, leis penais e o papel dos entes federativos na segurança.
Exclui: defesa nacional e Forças Armadas em função externa (vai para T57-DEF); corrupção como tema de gestão pública (vai para E-CORR, salvo quando a proposta é penal, como "tornar a corrupção crime hediondo", que fica em SEG.PENAL).

| Subcódigo | Definição |
|---|---|
| SEG.CRIME | Crime organizado, facções, milícias, tráfico, controle territorial, asfixia financeira do crime |
| SEG.POL | Polícias e forças de segurança: efetivo, carreira, equipamento, uso da força, estrutura (inclusive desmilitarização ou dissolução) |
| SEG.PENAL | Leis penais e processuais, penas, maioridade penal, sistema prisional, progressão de regime |
| SEG.VIOL | Violência contra grupos específicos (mulheres, crianças, população negra, juventude) e violência policial |
| SEG.ARMAS | Armas de fogo, porte, autodefesa |
| SEG.FED | Arquitetura institucional e paradigma da política de segurança: competências entre União, estados e municípios, ministérios, sistemas e fundos nacionais, propostas de substituir o modelo de segurança |
| SEG.PREV | Prevenção social do crime, inteligência, tecnologia de vigilância e centrais integradas, ressocialização de egressos e fora do sistema prisional (trabalho e educação dentro das prisões vão para SEG.PENAL) |
| SEG.DIAG | Diagnóstico da segurança, sem proposta (geral ou de objeto específico, com o objeto anotado) |

### IMP — Impostos e custo de vida
Não há tema correspondente na Câmara. Os mais próximos são 40 Economia e 70 Finanças Públicas e Orçamento.
Inclui: tributos, preços, inflação, juros ao consumidor e poder de compra.
Exclui: política industrial, comércio exterior e crescimento em geral (T40-ECO); gasto e dívida pública sem relação com a carga sobre o cidadão (T70-FIN); salário mínimo e direitos trabalhistas (T58-TRAB).

| Subcódigo | Definição |
|---|---|
| IMP.TRIB | Carga e estrutura tributária: reforma, tributos sobre consumo, renda, patrimônio, grandes fortunas, isenções, simplificação |
| IMP.PRECO | Preços e custo de vida: combustíveis, alimentos, energia, tarifas, inflação, preços administrados |
| IMP.JUROS | Juros, crédito, endividamento das famílias |
| IMP.DIAG | Diagnóstico de carga, preço, juros ou custo, sem proposta (geral ou de objeto específico, com o objeto anotado) |

### SAU — Saúde pública
Correspondência na Câmara: 56 Saúde.
Inclui: SUS, atendimento, financiamento da saúde, profissionais, saúde suplementar e agendas específicas de saúde.
Exclui: saneamento (T41-CID), esporte como saúde (T39-ESP), salvo quando a proposta é explicitamente de saúde.

| Subcódigo | Definição |
|---|---|
| SAU.ACESSO | Acesso e atendimento: filas, tempo de espera, cobertura, atenção primária, hospitais, unidades |
| SAU.FIN | Financiamento e gestão: verbas, pisos, modelo de gestão, regionalização |
| SAU.PROF | Profissionais de saúde: provimento, formação, salários |
| SAU.PUBPRIV | Relação público-privado: privatização, parcerias, planos de saúde, compra de serviços |
| SAU.ESP | Agendas específicas: saúde mental, doenças raras, câncer, saúde da mulher, medicamentos, vacinação |
| SAU.TEC | Tecnologia, pesquisa e produção em saúde: saúde digital, telessaúde, prontuário, avaliação e incorporação de tecnologias, complexo industrial da saúde (CEIS), institutos de pesquisa e produção |
| SAU.DIAG | Diagnóstico da saúde, sem proposta (geral ou de objeto específico, com o objeto anotado) |

## B. Demais temas da Câmara (só presença)

Código = T + código oficial da Câmara (Etapa 1, `/referencias/proposicoes/codTema`). Definição operacional resumida.

| Código | Tema da Câmara | Inclui (resumo operacional) |
|---|---|---|
| T34-ADM | Administração Pública | Estrutura e gestão do Estado, servidores, reforma administrativa, eficiência, governo digital |
| T35-CULT | Arte, Cultura e Religião | Cultura, patrimônio, liberdade religiosa |
| T37-COM | Comunicações | Mídia, concessões, internet, telecomunicações, liberdade de expressão nos meios |
| T39-ESP | Esporte e Lazer | Esporte, lazer. Atividade física apresentada explicitamente como política de saúde vai para SAU.ESP |
| T40-ECO | Economia | Macroeconomia: crescimento, política monetária e cambial, ambiente de negócios em geral, estatais e privatizações |
| T41-CID | Cidades e Desenvolvimento Urbano | Moradia, saneamento, urbanismo, favelas |
| T42-CIV | Direito Civil e Processual Civil | Família, contratos, propriedade (direito civil) |
| T44-DH | Direitos Humanos e Minorias | Direitos de grupos (mulheres, população negra, LGBT, indígenas, pessoas com deficiência), combate a discriminação |
| T46-EDU | Educação | Educação básica e superior |
| T48-AMB | Meio Ambiente e Desenvolvimento Sustentável | Ambiente, clima, Amazônia (dimensão ambiental) |
| T51-FUND | Estrutura Fundiária | Reforma agrária, terras indígenas, regularização fundiária |
| T52-PREV | Previdência e Assistência Social | Aposentadoria, transferência de renda, assistência |
| T53-PLEG | Processo Legislativo e Atuação Parlamentar | Funcionamento do Congresso, emendas parlamentares |
| T54-ENER | Energia, Recursos Hídricos e Minerais | Energia, petróleo, mineração, terras raras, água como recurso |
| T55-RI | Relações Internacionais e Comércio Exterior | Política externa, comércio exterior, soberania na relação com outros países |
| T57-DEF | Defesa (parte de Defesa e Segurança) | Forças Armadas, defesa nacional, fronteiras como defesa |
| T58-TRAB | Trabalho e Emprego | Direitos trabalhistas, jornada, salário mínimo, emprego, informalidade, aplicativos |
| T60-TUR | Turismo | Turismo |
| T61-TRANS | Viação, Transporte e Mobilidade | Transporte, rodovias, mobilidade urbana |
| T62-CTI | Ciência, Tecnologia e Inovação | Ciência, pesquisa, inteligência artificial, inovação |
| T64-AGRO | Agricultura, Pecuária, Pesca e Extrativismo | Agropecuária, agricultura familiar, segurança alimentar (produção) |
| T66-IND | Indústria, Comércio e Serviços | Setores (indústria, comércio, serviços), política industrial, empreendedorismo, micro e pequenas empresas |
| T67-CONS | Direito e Defesa do Consumidor | Consumidor |
| T68-CONST | Direito Constitucional | Reformas constitucionais, sistema de governo, pacto federativo |
| T70-FIN | Finanças Públicas e Orçamento | Gasto público, arcabouço fiscal, dívida pública, orçamento |
| T72-HOM | Homenagens e Datas Comemorativas | (improvável em programas) |
| T74-POL | Política, Partidos e Eleições | Sistema eleitoral e partidário, reforma política |
| T76-JUS | Direito e Justiça | Judiciário, STF, Ministério Público, acesso à Justiça |
| T85-EXA / T86-HUM | Ciências Exatas / Ciências Sociais e Humanas | (improvável em programas) |

Observação: o tema 43 (Direito Penal) e a parte de segurança do tema 57 foram incorporados a SEG.

## C. Categorias emergentes

Abertas durante a codificação. Cada uma traz a definição, o motivo de não caber na grade da Câmara e o primeiro exemplo.

| Código | Definição | Por que não cabe na grade | Primeiro exemplo |
|---|---|---|---|
| E-CORR | Combate à corrupção, integridade, transparência e privilégios da elite política (quando tratados como tema próprio) | A Câmara distribui o tema entre Administração Pública e Direito Penal | DC, p. 13, "6.3 Integridade e transparência" |

## Histórico

- v1 (27/10/2026): versão inicial.
- v1.1 (27/10/2026), durante a calibração com DC: regra da lista fragmentária; fronteira entre T40 (macroeconomia) e T66 (setores e empreendedorismo); atividade física como saúde vai para SAU.ESP. O programa do PCO, codificado em v1, não foi afetado por essas mudanças (verificado: não tem lista fragmentária nem unidades em T40/T66 ou T39 que mudem de código).
- v1.2 (27/10/2026), durante a calibração com PCB: SEG.FED passa a incluir o paradigma e a arquitetura institucional; SAU.TEC passa a incluir pesquisa e produção (CEIS); regras de lei penal e de repetição. PCO e DC conferidos: nenhuma unidade muda de código.
- v1.3 (27/10/2026), depois do reteste da rodada 1 (`reteste.md`): regra do objetivo explícito de preço.
- v1.4 (27/10/2026), durante a codificação de PRTB/Marçal: regra do incentivo tributário setorial. Programas anteriores conferidos: nenhuma unidade muda de código.
- v1.5 (27/10/2026), durante a codificação do PSTU: a regra da lei penal passa a incluir explicitamente a legalização de condutas, com marca de fronteira; nova regra para saúde de grupos específicos. Revisão no PCB: o aborto passou de T44 para SEG.PENAL (PCB-S14). PCO, DC e Marçal conferidos, sem mudanças.
- v1.6 (27/10/2026), durante a codificação do DEMOCRATA: regra das Forças Armadas e da fronteira. Programas anteriores conferidos: PCB p. 13 (Forças Armadas nas fronteiras, sem finalidade criminal declarada) continua em T57; Marçal e DC (fronteira sob segurança, sem Forças Armadas) continuam em SEG.PREV.
- v1.7 (28/10/2026), durante a codificação do PT: marca [balanço] para relatos de gestão. Aplicada também ao PL (FLA-I8, balanço do governo Bolsonaro). Nos programas 1 a 10 não há balanço de gestão federal codificado (o relato de Zema sobre Minas Gerais, p. 3, ficou fora da codificação por ser biográfico).
- v1.8 (28/10/2026), depois do reteste da rodada 2 (`reteste.md`): (a) regra do diagnóstico, que passa a receber sempre o subcódigo DIAG, com o objeto anotado; (b) a regra do objetivo explícito de preço fica restrita aos bens de consumo geral; (c) SEG.PREV e SEG.PENAL deixam de se sobrepor em ressocialização; (d) centrais integradas de segurança vão para SEG.PREV. Conferência retroativa nos 14 programas: 38 unidades mudaram de código (lista em `reteste.md`). A presença dos temas não mudou em nenhum programa.
