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

## Rodada 2 — final

A ser feita depois da codificação dos outros 11 programas, com 10% das unidades.
