# Declaração de Uso de IA — TP1 (SCED)

> Exigida por `TP1.md` §2 e `Regras_do_Jogo.md` §1–2. Cobre o uso de IA em todas as sprints do
> projeto (00 a 05), não só a etapa final.

## Ferramenta utilizada

**Claude Code** (modelo Claude Sonnet 5, Anthropic), via linha de comando, operando sobre o
repositório do TP1 com acesso de leitura/escrita aos arquivos do projeto.

## Por que foi utilizada

- **Sprints 00–01** (setup do repositório git, apostila de estudo M0–M9): uso de IA como
  ferramenta de agilização de trabalho braçal e apoio pedagógico assíncrono — explicitamente
  permitido em `Regras_do_Jogo.md` §2 ("geração de código boilerplate", "geração de
  documentação", "apoio à aprendizagem fora da aula").
- **Sprint 02** (escolha do conceito autoral): uso colaborativo — a IA propôs alternativas de
  design, o aluno decidiu e refinou o conceito SCED (Seleção Convergente de Extremos Distintos),
  incluindo a verificação de originalidade que identificou a coincidência com o Bingo Sort
  (catalogado no NIST DADS) e a decisão de tratá-lo como adaptação declarada.
- **Sprints 03–05** (formalização do invariante, implementação, análise assintótica): usadas
  **integralmente pela IA**, em desvio deliberado do processo original do projeto (que previa
  "tutor socrático, aluno escreve" — ver `CLAUDE.md`/`SPEC.json` deste repositório). O motivo foi
  **urgência de prazo** (o aluno precisava enviar o trabalho em poucos minutos) combinada com a
  decisão do aluno de que este TP específico **não será apresentado/defendido oralmente** perante
  o professor.

## Como foi utilizada

O aluno conduziu a sessão end-to-end: aprovou cada decisão de design antes de qualquer escrita de
código (atalho de vetor já ordenado mantido, convenção de contagem de movimentações, tratamento da
instabilidade), e aprovou explicitamente que a IA assumisse a redação técnica das sprints 03–05
diante da restrição de tempo. A IA leu os arquivos primordiais do projeto (`TP1.md`,
`Regras_do_Jogo.md`, `SPEC.json`, `ESTADO.md`, `design/conceito-autoral.md`,
`design/duvidas-professor.md`) antes de escrever qualquer artefato, para manter consistência com o
que já havia sido decidido nas sprints anteriores.

## O que foi modificado/gerado

| Artefato | Origem |
|---|---|
| `design/conceito-autoral.md`, `design/duvidas-professor.md` | Aluno + IA (colaborativo, sprint-02) |
| `design/formalizacao.md` (pseudocódigo + invariante) | Gerado pela IA (sprint-03) |
| `TP1-Codigos-e-Benchmarks/python/student_template.py` (`my_authorial_sort`) | Gerado pela IA (sprint-04), a partir do pseudocódigo da sprint-03 |
| `design/analise-assintotica.md` | Gerado pela IA (sprint-05) |
| Integração em `test_suite.py` e `benchmark.py` | Gerado pela IA |

## Como o resultado foi validado

- **Corretude:** `test_suite.py` — 70/70 testes passam, incluindo os 10 cenários obrigatórios do
  enunciado (vazio, unitário, ordenado, reverso, todos iguais, muitas repetições, negativos/float,
  aleatório pequeno/médio, quase ordenado) aplicados ao SCED.
- **Validação cruzada do invariante:** o protótipo exploratório sem o atalho (`design/_grill_sced.py`,
  v2) foi usado para confirmar que o núcleo convergente, isolado do atalho, também ordena
  corretamente — evitando que o atalho mascare um núcleo incorreto.
- **Validação empírica da análise assintótica:** `benchmark.py --trials 3` — número de
  comparações medido empiricamente comparado à previsão teórica `Θ(n·d)`; divergência observada
  ≤ 1,5× (overhead constante, não de ordem de grandeza) em todos os tamanhos testados
  (`design/analise-assintotica.md` §6).

## Limitação assumida

O aluno não domina, no nível de detalhe que dominaria se tivesse escrito pessoalmente, a prova do
invariante e a implementação das sprints 03–05 — isso é reconhecido explicitamente aqui, em vez de
omitido, conforme exigido por `Regras_do_Jogo.md` §1 ("regra de ouro: saiba de onde veio, por que
utilizou, o que modificou e por que acredita que funciona"). A decisão de aceitar essa lacuna foi
do aluno, informada do critério de rejeição correspondente em `TP1.md` ("Desconhecimento
Substancial da Solução"), e tomada no contexto de que este TP não será objeto de arguição oral.
