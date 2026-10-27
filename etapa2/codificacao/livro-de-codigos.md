# Livro de códigos — Etapa 2

Versão 1 (27/10/2026), antes da calibração. As alterações feitas depois do reteste são registradas na seção "Histórico".

## Regras gerais

- **Unidade de registro:** o trecho mínimo com sentido programático. Pode ser uma proposta (o que fazer) ou um diagnóstico (o que está errado e por quê). Em geral é um item de lista ou um período.
- **Unidade de contexto:** a seção ou capítulo do programa, registrada junto com a página.
- **Presença de um tema num programa:** pelo menos uma unidade programática sobre ele. Menção de passagem dentro de outra proposta, sem conteúdo próprio, não conta. Por exemplo, "destinar o petróleo à saúde e educação" conta para Energia, mas não para Saúde nem para Educação.
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
| SEG.CRIME | Crime organizado, facções, milícias, tráfico, controle territorial |
| SEG.POL | Polícias e forças de segurança: efetivo, carreira, equipamento, uso da força, estrutura (inclusive desmilitarização ou dissolução) |
| SEG.PENAL | Leis penais e processuais, penas, maioridade penal, sistema prisional, progressão de regime |
| SEG.VIOL | Violência contra grupos específicos (mulheres, crianças, população negra, juventude) e violência policial |
| SEG.ARMAS | Armas de fogo, porte, autodefesa |
| SEG.FED | Competências e cooperação entre União, estados e municípios na segurança; sistemas nacionais e fundos |
| SEG.PREV | Prevenção social do crime, inteligência, tecnologia de vigilância, ressocialização |
| SEG.DIAG | Diagnóstico geral da segurança, sem proposta específica |

### IMP — Impostos e custo de vida
Não há tema correspondente na Câmara. Os mais próximos são 40 Economia e 70 Finanças Públicas e Orçamento.
Inclui: tributos, preços, inflação, juros ao consumidor e poder de compra.
Exclui: política industrial, comércio exterior e crescimento em geral (T40-ECO); gasto e dívida pública sem relação com a carga sobre o cidadão (T70-FIN); salário mínimo e direitos trabalhistas (T58-TRAB).

| Subcódigo | Definição |
|---|---|
| IMP.TRIB | Carga e estrutura tributária: reforma, tributos sobre consumo, renda, patrimônio, grandes fortunas, isenções, simplificação |
| IMP.PRECO | Preços e custo de vida: combustíveis, alimentos, energia, tarifas, inflação, preços administrados |
| IMP.JUROS | Juros, crédito, endividamento das famílias |
| IMP.DIAG | Diagnóstico geral de carga ou custo, sem proposta específica |

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
| SAU.TEC | Saúde digital, telessaúde, prontuário, tecnologia |
| SAU.DIAG | Diagnóstico geral da saúde, sem proposta específica |

## B. Demais temas da Câmara (só presença)

Código = T + código oficial da Câmara (Etapa 1, `/referencias/proposicoes/codTema`). Definição operacional resumida.

| Código | Tema da Câmara | Inclui (resumo operacional) |
|---|---|---|
| T34-ADM | Administração Pública | Estrutura e gestão do Estado, servidores, reforma administrativa, eficiência, governo digital |
| T35-CULT | Arte, Cultura e Religião | Cultura, patrimônio, liberdade religiosa |
| T37-COM | Comunicações | Mídia, concessões, internet, telecomunicações, liberdade de expressão nos meios |
| T39-ESP | Esporte e Lazer | Esporte, lazer |
| T40-ECO | Economia | Crescimento, emprego macro, indústria, política monetária, privatizações, estatais |
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
| T66-IND | Indústria, Comércio e Serviços | Política industrial setorial, comércio, empreendedorismo, pequenas empresas |
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
| E-CORR | Combate à corrupção, transparência e privilégios da elite política (quando tratados como tema próprio) | A Câmara distribui o tema entre Administração Pública e Direito Penal | (a preencher) |

## Histórico

- v1 (27/10/2026): versão inicial.
