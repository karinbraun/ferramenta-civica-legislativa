# Briefing do projeto — Ferramenta cívica legislativa

Documento de contexto para o Claude Code. Versão inicial para discussão; nada deve ser construído antes de validarmos juntos a arquitetura.

## 1. Propósito e público

Ferramenta web educativa e neutra que ajuda qualquer cidadão brasileiro, independentemente de orientação política, a entender o que já existe e o que está em discussão no Legislativo sobre os temas que importam para ele.

O cidadão informa seus desejos ou preocupações. A ferramenta mostra: (a) leis federais vigentes desde a Constituição de 1988 relacionadas ao tema; (b) políticas públicas federais implementadas, quando houver; (c) projetos em tramitação na Câmara e no Senado. Quando o tema for de competência estadual ou municipal, a ferramenta explica quem é responsável e como o cidadão pode se informar e cobrar.

O projeto começa como protótipo, testado com público misto (eleitores de diferentes campos políticos), e evolui gradualmente até abertura ao público geral. Não há pressa.

## 2. Princípios inegociáveis

- Neutralidade: nenhum texto da ferramenta pode valorar partidos, parlamentares ou propostas. A estrutura de temas não pode privilegiar a agenda de nenhum campo político.
- Conteúdo antes da autoria: autores, coautores, partidos e votações ficam ocultos por padrão e acessíveis por ação explícita do usuário (ex.: botão "Quem propôs?" e "Como votaram?").
- Rastreabilidade: todo item exibido traz a ementa oficial e o link para a fonte oficial (Câmara, Senado, Planalto, LexML).
- Status oficial: a ferramenta usa apenas a classificação de tramitação dos sistemas oficiais. Não cria rótulos próprios (ex.: não usar "em risco de arquivamento").
- Honestidade sobre limites: quando a relação entre o desejo do cidadão e uma lei for aproximada, isso deve ser sinalizado. Lei aprovada não equivale a política implementada, e a interface deve deixar essa diferença clara.
- Partido registrado na data da proposição (parlamentares mudam de partido).

## 3. Funcionalidades do protótipo

1. Entrada por temas pré-definidos (primeira fase). Campo de texto livre fica para fase posterior.
2. Para cada tema: lista de leis vigentes, políticas públicas (quando houver) e projetos em tramitação, cada um com resumo em linguagem cidadã, ementa oficial e link.
3. Camada de autoria sob demanda: autores e coautores, com partido e UF.
4. Camada de votação sob demanda: voto por partido e por parlamentar nas votações nominais. Nas votações simbólicas, apenas o resultado oficial (aprovado/rejeitado), com aviso explícito de que a votação foi simbólica e não há registro de voto individual nem de orientação de bancada (ver seção 8).
5. Nota educativa de competência: quando o tema depender de estado ou município, explicar a divisão de responsabilidades (União, estado, município) e indicar canais de informação e cobrança (Câmara de Vereadores, Assembleia Legislativa, ouvidorias, Fala.BR, portais de transparência).
6. Notas educativas sobre tramitação: abaixo do status oficial, explicar quando aplicável que o projeto pode ser arquivado e por quê (regra de arquivamento ao fim da legislatura, com exceções e possibilidade de desarquivamento), com link para a norma. A nota só aparece nos projetos aos quais a regra se aplica.

## 4. Fontes de dados e limitações conhecidas

- API de Dados Abertos da Câmara dos Deputados: proposições, autores, temas, tramitação, votações, orientações de bancada.
- API de Dados Abertos do Senado Federal: estrutura diferente da Câmara; verificar cobertura de votações e autoria.
- LexML e Portal da Legislação do Planalto: leis vigentes.
- Políticas públicas: não há base unificada. Exige curadoria manual no protótipo.

Limitações já identificadas: votações simbólicas não têm voto individual; o volume de leis desde 1988 é grande, por isso o protótipo cobre poucos temas; a regra de arquivamento (Regimento Interno da Câmara, art. 105) precisa ser confirmada na versão vigente, assim como a regra equivalente do Senado; a nova legislatura começa em fevereiro de 2027.

## 5. Temas do protótipo

Estrutura baseada na classificação temática oficial da Câmara, com rótulos reescritos em linguagem cidadã a partir dos programas de governo de todos os candidatos registrados no TSE em 2026. O protótipo começa com 3 temas: segurança e combate ao crime (competência majoritariamente estadual), impostos e custo de vida (federal) e saúde pública (compartilhada). Critérios de escolha: mobilizar eleitores dos dois campos, variar o tipo de competência e ter volume de dados na Câmara. Trabalho e emprego e educação entram numa segunda rodada. A correspondência entre esses temas e os programas de governo ainda é hipótese, a verificar na etapa 2.

## 6. Sequência de etapas

1. Validar fontes: testar as APIs da Câmara, do Senado e do LexML; mapear campos disponíveis (incluindo regime de tramitação e pareceres, necessários para a nota de arquivamento).
2. Definir os temas do protótipo e seus rótulos.
3. Montar a base de dados: leis, projetos, status, autoria, votações.
4. Construir o cruzamento entre tema e legislação, sempre com link à fonte.
5. Construir a interface com camadas ocultas de autoria e votação.
6. Testar com público misto e iterar.

## 7. Como trabalhar comigo

- Antes de escrever código, discuta a arquitetura proposta e as alternativas, com prós e contras.
- Faça uma pergunta por vez quando houver dúvida; não presuma decisões de produto.
- Avise antes de prosseguir se uma fonte de dados não sustentar uma funcionalidade.
- Valide comigo o plano de cada etapa antes de executá-la.
- Use português do Brasil em toda a interface e documentação.

## 8. Decisões já validadas

- Arquitetura: site estático gerado a partir de base curada, com atualização automática diária (GitHub Actions) e data da última atualização visível. Cada item exibe a data de extração e o aviso para consultar a fonte oficial.
- Atualização automática altera apenas campos oficiais (situação, tramitação, votações) de itens já aprovados.
- Itens novos entram em fila de revisão: Claude propõe vínculo ao tema, resumo cidadão e grau de aderência; a responsável aprova ou ajusta via pull request.
- Repositório público no GitHub desde o início, com aviso de protótipo no README.
- Votação simbólica (27/10/2026): mostrar só o resultado oficial, com aviso de que não há registro de voto individual nem de orientação de bancada. Motivo: a API da Câmara não registra orientação nas votações simbólicas (0 de 79 na amostra de novembro de 2025; ver `etapa1/relatorio-cobertura.md`, seção 2.1).
