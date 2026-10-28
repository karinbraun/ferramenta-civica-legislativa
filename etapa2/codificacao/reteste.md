# Reteste de estabilidade da codificação

Método decidido em 27/10/2026: reteste de estabilidade, sem segundo codificador. A mesma pessoa que codificou (Claude) recodifica uma amostra sem consultar o primeiro passe, usando só o livro de códigos e o trecho literal. Limitação declarada: quem recodifica conhece o material e pode lembrar das próprias decisões. Por isso o reteste mede estabilidade, e não confiabilidade entre codificadores.

## Rodada 1 — calibração (PCO, DC e PCB)

- Universo: 67 unidades dos temas da hipótese (PCO 19, DC 14, PCB 34).
- Amostra: 10 unidades (15%), sorteadas com `random.seed(2026)` e `random.sample`, em ordem embaralhada. Só os trechos foram mostrados, sem código nem identificação.
- Livro de códigos usado na recodificação: v1.2.

| Trecho | Unidade | 1º passe | Reteste | Concorda |
|---|---|---|---|---|
| R1 | PCB-I2 | IMP.PRECO | T52-PREV | **Não** |
| R2 | PCO-H4 | SAU.PROF | SAU.PROF | Sim |
| R3 | PCB-I3 | IMP.PRECO | IMP.PRECO | Sim |
| R4 | DC-S7 | SEG.PENAL | SEG.PENAL | Sim |
| R5 | PCB-I1 | IMP.TRIB | IMP.TRIB | Sim |
| R6 | PCO-I3 | IMP.TRIB | IMP.TRIB | Sim |
| R7 | DC-S2 | SEG.VIOL | SEG.VIOL | Sim |
| R8 | DC-S5 | SEG.CRIME | SEG.CRIME | Sim |
| R9 | DC-S6 | SEG.POL | SEG.POL | Sim |
| R10 | PCO-I4 | IMP.PRECO | IMP.PRECO | Sim |

Concordância simples: 9/10 (0,90). Kappa de Cohen: 0,88 (concordância esperada ao acaso 0,15). Ressalva: com 10 unidades, o kappa é instável e serve só como indicador de calibração.

### Divergência e resolução

R1 / PCB-I2: [LITERAL] "Criação de uma rede de restaurantes e mercados populares nos municípios [...] como forma de reduzir emergencialmente a fome e o preço dos alimentos" (PCB, p. 9).

O trecho declara dois objetivos: a fome (T52, assistência) e o preço dos alimentos (IMP.PRECO). O livro de códigos v1.2 não dizia o que fazer quando uma proposta de assistência declara a redução de preço como objetivo explícito.

Resolução (livro de códigos v1.3): quando a proposta declara de forma explícita o objetivo de reduzir ou controlar preços ao consumidor, a unidade recebe IMP.PRECO, e o outro tema é registrado só como presença. A unidade PCB-I2 mantém IMP.PRECO, e T52 já está presente no PCB por outras unidades. Nenhuma outra unidade da calibração muda de código.

Decisões de fronteira registradas nos arquivos de codificação e não sorteadas, a acompanhar na rodada 2: tarifa zero no transporte (PCB, p. 7, codificada em T61); legalização do aborto com atendimento na rede pública (PCB, p. 11, codificada em T44); atividade física como saúde (DC, p. 11, codificada em SAU.ESP).

## Rodada 2 — final (programas 4 a 14)

- Universo: 788 unidades dos temas da hipótese nos 11 programas (CAI 146, GRA 84, LUL 81, ZEM 80, FLA 73, CUR 71, AVA 60, SAM 56, PST 53, MIS 50, PMA 34). Repetições e unidades de balanço incluídas.
- Amostra: 79 unidades (10%), sorteadas com `random.seed(2026)` e `random.sample` (script `etapa2/scripts/reteste_r2_amostra.py`). Foram mostrados só os trechos literais, sem código, programa, página ou seção.
- Livro de códigos usado na recodificação: v1.7.
- Comparação: script `etapa2/scripts/reteste_r2_compara.py`. Compara o subcódigo (as marcas de repetição, fronteira e balanço não entram).

Limitação desta rodada, além da declarada no topo: a recodificação aconteceu logo depois da codificação de Caiado (CAI), que responde por 18 das 79 unidades da amostra. É provável que quem recodificou ainda se lembrasse dessas unidades, o que tende a inflar a concordância nelas. Fora de CAI, a concordância foi de 55/61 (0,90).

| Trecho | Unidade | 1º passe | Reteste | Concorda |
|---|---|---|---|---|
| R1 | ZEM-H15 | SAU.ESP | SAU.ESP | Sim |
| R2 | GRA-S8 | SEG.PENAL | SEG.PENAL | Sim |
| R3 | CUR-I4 | IMP.TRIB | IMP.TRIB | Sim |
| R4 | CUR-H4 | SAU.FIN | SAU.FIN | Sim |
| R5 | CAI-H36 | SAU.ESP | SAU.ESP | Sim |
| R6 | ZEM-I23 | IMP.PRECO | IMP.PRECO | Sim |
| R7 | PST-H2 | SAU.DIAG | SAU.DIAG | Sim |
| R8 | CAI-I3 | IMP.DIAG | IMP.DIAG | Sim |
| R9 | CAI-H10 | SAU.DIAG | SAU.DIAG | Sim |
| R10 | CAI-S22 | SEG.PREV | SEG.PREV | Sim |
| R11 | FLA-S27 | SEG.CRIME (rep. de S24) | SEG.CRIME | Sim |
| R12 | CAI-S39 | SEG.VIOL | SEG.VIOL | Sim |
| R13 | CAI-S13 | SEG.PENAL | SEG.PENAL | Sim |
| R14 | AVA-S21 | SEG.VIOL | SEG.VIOL | Sim |
| R15 | AVA-H16 | SAU.ESP | SAU.DIAG | **Não** |
| R16 | CUR-S26 | SEG.PREV | SEG.PREV | Sim |
| R17 | AVA-I19 | IMP.TRIB [fronteira com T66] | IMP.TRIB | Sim |
| R18 | CAI-S53 | SEG.VIOL (rep. de S37) | SEG.VIOL | Sim |
| R19 | FLA-I21 | IMP.JUROS | IMP.JUROS | Sim |
| R20 | LUL-S7 | SEG.DIAG | SEG.DIAG | Sim |
| R21 | SAM-S3 | SEG.VIOL | SEG.VIOL | Sim |
| R22 | CAI-H2 | SAU.ACESSO (rep.) | SAU.ACESSO | Sim |
| R23 | ZEM-S27 | SEG.PENAL [fronteira] | SEG.PENAL | Sim |
| R24 | ZEM-H7 | SAU.TEC | SAU.TEC | Sim |
| R25 | LUL-H9 | SAU.ACESSO | SAU.ACESSO | Sim |
| R26 | ZEM-I18 | IMP.PRECO | IMP.PRECO | Sim |
| R27 | FLA-H2 | SAU.TEC (rep. de H6) | SAU.TEC | Sim |
| R28 | SAM-S12 | SEG.PENAL | SEG.DIAG | **Não** |
| R29 | PMA-S8 | SEG.PENAL | SEG.PENAL | Sim |
| R30 | PMA-S2 | SEG.CRIME | SEG.CRIME | Sim |
| R31 | GRA-S2 | SEG.FED | SEG.FED | Sim |
| R32 | PST-S30 | SEG.VIOL (rep.) | SEG.VIOL | Sim |
| R33 | FLA-S3 | SEG.PENAL | SEG.PENAL | Sim |
| R34 | LUL-S19 | SEG.PENAL | SEG.PENAL | Sim |
| R35 | GRA-S37 | SEG.FED | SEG.FED | Sim |
| R36 | GRA-I5 | IMP.TRIB | IMP.TRIB | Sim |
| R37 | GRA-H1 | SAU.DIAG | SAU.DIAG | Sim |
| R38 | AVA-I13 | IMP.PRECO [fronteira] | IMP.PRECO | Sim |
| R39 | CUR-H5 | SAU.TEC | SAU.TEC | Sim |
| R40 | CAI-H27 | SAU.ESP | SAU.ESP | Sim |
| R41 | ZEM-S23 | SEG.PREV | SEG.PREV | Sim |
| R42 | AVA-S13 | SEG.VIOL | SEG.VIOL | Sim |
| R43 | GRA-S29 | SEG.CRIME | SEG.PREV | **Não** |
| R44 | ZEM-I9 | IMP.JUROS | IMP.JUROS | Sim |
| R45 | CAI-S23 | SEG.PREV | SEG.PREV | Sim |
| R46 | CAI-S3 | SEG.DIAG | SEG.DIAG | Sim |
| R47 | LUL-H14 | SAU.TEC | SAU.TEC | Sim |
| R48 | FLA-H10 | SAU.ESP | SAU.ESP | Sim |
| R49 | MIS-S9 | SEG.CRIME | SEG.CRIME | Sim |
| R50 | CAI-H34 | SAU.ESP | SAU.ESP | Sim |
| R51 | PMA-H2 | SAU.TEC | SAU.TEC | Sim |
| R52 | AVA-S6 | SEG.PREV (rep. de S2 e S4) | SEG.PREV | Sim |
| R53 | CAI-S44 | SEG.VIOL | SEG.VIOL | Sim |
| R54 | LUL-H31 | SAU.ESP | SAU.ESP | Sim |
| R55 | SAM-S26 | SEG.PENAL | SEG.PREV | **Não** |
| R56 | PMA-H9 | SAU.ESP | SAU.ESP | Sim |
| R57 | GRA-I17 | IMP.TRIB | IMP.TRIB | Sim |
| R58 | GRA-I12 | IMP.TRIB | IMP.TRIB | Sim |
| R59 | FLA-H14 | SAU.TEC | SAU.TEC | Sim |
| R60 | FLA-I2 | IMP.TRIB (rep. de I10) | IMP.PRECO | **Não** |
| R61 | ZEM-I10 | IMP.JUROS | IMP.JUROS | Sim |
| R62 | FLA-S5 | SEG.POL | SEG.POL | Sim |
| R63 | CAI-S52 | SEG.VIOL | SEG.VIOL | Sim |
| R64 | CAI-S20 | SEG.CRIME | SEG.CRIME | Sim |
| R65 | CUR-S34 | SEG.FED | SEG.PREV | **Não** |
| R66 | ZEM-H13 | SAU.ESP | SAU.ESP | Sim |
| R67 | FLA-I5 | IMP.PRECO | IMP.PRECO | Sim |
| R68 | CUR-I8 | IMP.PRECO | IMP.PRECO | Sim |
| R69 | AVA-I18 | IMP.TRIB | IMP.TRIB | Sim |
| R70 | CAI-I2 | IMP.JUROS | IMP.JUROS | Sim |
| R71 | FLA-S4 | SEG.CRIME | SEG.CRIME | Sim |
| R72 | CUR-H17 | SAU.TEC | SAU.TEC | Sim |
| R73 | LUL-S26 | SEG.POL | SEG.POL | Sim |
| R74 | CAI-S30 | SEG.PENAL | SEG.PENAL | Sim |
| R75 | CUR-S14 | SEG.PENAL | SEG.PENAL | Sim |
| R76 | CUR-H10 | SAU.ESP | SAU.ESP | Sim |
| R77 | CAI-S42 | SEG.PREV | SEG.PREV | Sim |
| R78 | PST-H3 | SAU.PUBPRIV | SAU.PUBPRIV | Sim |
| R79 | AVA-H14 | SAU.ESP (rep. de H6 e H8) | SAU.ESP | Sim |

Concordância simples: 73/79 (0,92). Kappa de Cohen: 0,92 (concordância esperada ao acaso 0,08). Concordância no tema principal (SEG, IMP ou SAU): 79/79. Todas as divergências ficaram dentro do mesmo tema; nenhuma afeta a presença de tema em programa.

### Divergências e resolução

| Trecho | Unidade | Tipo de divergência | Resolução |
|---|---|---|---|
| R15 | AVA-H16 | Diagnóstico de objeto específico (saúde mental de jovens): ESP no 1º passe, DIAG no reteste | Regra nova (a). Passa a SAU.DIAG (objeto: ESP) |
| R28 | SAM-S12 | Diagnóstico de objeto específico (encarceramento): PENAL × DIAG | Regra nova (a). Passa a SEG.DIAG (objeto: PENAL) |
| R43 | GRA-S29 | Abigeato com cruzamento de dados: CRIME × PREV | Mantém o reteste: o abigeato não é crime organizado, e o instrumento é inteligência. Passa a SEG.PREV |
| R55 | SAM-S26 | Penitenciárias transformadas em unidades de reeducação: PENAL × PREV | Mantém o 1º passe. A definição de SEG.PREV incluía "ressocialização" e se sobrepunha a SEG.PENAL; a prática nos programas (DC-S7, PMA-S11, PMA-S12, CUR-S13, CAI-S32) sempre pôs a ressocialização dentro da prisão em PENAL. Regra nova (c) |
| R60 | FLA-I2 | Síntese do eixo "Brasil Mais Barato" (imposto, luz, transporte, crédito): TRIB (rep.) × PRECO | Mantém o reteste: o trecho declara o objetivo de custo de vida e abrange quatro subcódigos. Passa a IMP.PRECO (síntese), sem marca de repetição |
| R65 | CUR-S34 | Centro Integrado de Segurança municipal: FED × PREV | Mantém o reteste, por coerência com CAI-S22, DC-S3 e CUR-S26 (centrais e sistemas integrados em PREV). Regra nova (d) |

Duas das seis divergências (R15 e R28) têm a mesma causa: o livro de códigos dizia "diagnóstico geral" e não orientava sobre o diagnóstico de um objeto específico. Na conferência retroativa, a prática do 1º passe estava dividida: 108 unidades estavam em DIAG (incluídas as de balanço), e outros 28 diagnósticos estavam no subcódigo do objeto (por exemplo, dados de feminicídio em SEG.VIOL e conta de luz cara em IMP.PRECO). Como o Polo 3 precisa separar propostas de diagnósticos, a regra (a) uniformiza: todo diagnóstico vai para DIAG, com o objeto anotado.

### Pendências do 1º passe resolvidas nesta rodada

1. **Alcance de IMP.PRECO** (anotado durante a codificação dos programas 8 a 13). Aplicada à letra, a regra do objetivo explícito de preço (v1.3) puxava para IMP qualquer proposta que mencionasse preço mais baixo, como materiais em braile e espectro de 5G. Regra nova (b): vale só para bens de consumo geral das famílias, coerente com a definição de IMP.PRECO. Saíram de IMP 7 unidades: ZEM-I14, I17 e I24; SAM-I9; AVA-I12; FLA-I27; CUR-I9. AVA-I13 (café) e SAM-I10 (alimento barato) continuam em IMP.PRECO, porque são alimentos.
2. **IMP.JUROS aplicado ao crédito de negócios (CUR-I1).** A unidade é diagnóstico e passou a IMP.DIAG (objeto: JUROS) pela regra (a). A pendência deixa de existir.
3. **Drogas: PCB e PSTU em SEG.PENAL, Samara em SEG.FED.** Conferido: não é inconsistência. PCB-S12 e PST-S9 propõem descriminalizar ou revogar a Lei Antidrogas, o que é mudança de lei penal (regra v1.5). SAM-S22 propõe a "transição do paradigma penal para o paradigma de saúde pública" sem propor mudança legal específica, o que é mudança de paradigma (SEG.FED, v1.2). Códigos mantidos. [INFERÊNCIA para o Polo 3] Os três programas convergem na crítica à "guerra às drogas", e isso deve aparecer na análise, mesmo com códigos diferentes.

### Conferência retroativa (livro de códigos v1.8)

38 unidades mudaram de código nos 14 programas:

- 28 diagnósticos passaram ao subcódigo DIAG, com o objeto anotado: SAM-S1, S8, S11, S12, S16, S17, S18, S25 e H13; ZEM-S24 e I18; LUL-S1; FLA-I5, I7, I13 e I16; CUR-S1, S20, I1 e H23; CAI-S51, I2 e I9; PCO-I5; AVA-S10, S16, H12 e H16.
- 7 unidades saíram de IMP.PRECO (pendência 1).
- 3 divergências do reteste resolvidas a favor do reteste: GRA-S29, FLA-I2 e CUR-S34.

Casos conferidos e mantidos: PCO-S1 (no texto completo, "É preciso acabar com [...] o massacre", portanto é reivindicação e não diagnóstico); GRA-S2 e GRA-S18 (premissas que sustentam a proposta de arquitetura federativa); FLA-I12 (declara o resultado pretendido de preço menor). As unidades de balanço mantêm a regra v1.7, porque a marca [balanço] já as separa das propostas.

Efeito nas contagens: IMP perde 7 unidades (ZEM 24→21, SAM 12→11, AVA 20→19, FLA 28→27, CUR 10→9); SAU ganha 2 (AVA 17→18, CUR 27→28). A presença dos temas não mudou em nenhum programa: os temas de destino (T37, T41, T44, T55, T61) já estavam presentes nos programas afetados, e todos os programas afetados mantêm outras unidades de IMP.
