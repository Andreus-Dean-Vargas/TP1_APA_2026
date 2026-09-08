# TP1 — Método de Ordenação Autoral (Análise e Projeto de Algoritmos - ES)

Repositório do **Trabalho Prático 1**: conceber, formalizar, implementar e validar um método de
ordenação **autoral**, entregando uma **apresentação de slides** + código executável.

> **Ideia central da disciplina:** a nota não vem de um algoritmo rápido, e sim de **saber explicar,
> justificar e defender** a solução. Um algoritmo O(n²) com análise brilhante vale mais que um rápido
> que o autor não sabe explicar. Por isso este projeto foi montado para **maximizar aprendizado e
> domínio**, não para "produzir código".

---

## 1. O que é este projeto

| Objetivo | Entregável |
|----------|-----------|
| Base teórica sólida | Apostila de estudo (`apostila/`) ancorada em CLRS + complementares |
| Algoritmo autoral | Implementação em `TP1-Codigos-e-Benchmarks/python/student_template.py` |
| Prova de corretude | Invariante de laço + pseudocódigo (`design/`) |
| Análise de complexidade | O, Ω, Θ e espaço (`design/analise-assintotica.md`) |
| Validação empírica | Suíte de testes + benchmark comparativo |
| Entrega | Slides + declaração de IA (`entrega/`) |

---

## 2. Por que foi feito desta forma (a metodologia)

Este trabalho segue o mesmo fluxo com que trabalhamos IA em projetos reais: **Harness Engineering +
Spec-Driven Development (SDD) + TDD**. A motivação:

### O código é abundante; o escasso é o contexto e o domínio
A IA gera código sem esforço. O recurso raro é **pensar bem** e **dominar a solução** — que é
exatamente o que a disciplina avalia (e o que a arguição oral cobra). Então otimizamos para
aprendizado, não para velocidade de digitação.

### Evitar a "Dumb Zone"
Quando um único chat acumula histórico longo, correções ad-hoc e comandos rasos, a precisão da IA
despenca. A defesa é **separar planejamento de execução** e rodar **cada sprint em uma janela limpa**.

### O humano pilota, a IA executa
O aluno é o *Harness Engineer*: define as sprints e os critérios de aceite; a IA executa dentro
desses trilhos. Nas sprints teóricas/de código (invariante, implementação, análise), **o aluno
escreve** e a IA atua como **tutor socrático** — porque quem vai defender o trabalho é o aluno.

### Documentação viva como memória
O histórico do chat some; os arquivos primordiais não. Eles são a fonte de verdade entre sessões.

---

## 3. Como o fluxo funciona (a cada sprint)

```
┌─ janela limpa (chat novo) ────────────────────────────────┐
│ 1. IA lê ESTADO.md        → descobre a próxima sprint      │
│ 2. IA lê SPEC.json        → goal, critérios de aceite,     │
│                             edge cases, arquivos afetados  │
│ 3. IA apresenta o plano   → aluno REVISA e aprova          │
│ 4. IA executa (ou guia)   → conforme papel_do_aluno        │
│ 5. Fecha a sprint         → atualiza ESTADO.md + SPEC.json │
│                             + 1 commit                     │
└───────────────────────────────────────────────────────────┘
```

Para iniciar uma sprint, basta abrir um chat novo e dizer algo como:
*"Leia o ESTADO.md e o SPEC.json e conduza a próxima sprint."*

---

## 4. Arquivos primordiais (a "lista de tarefas" do harness)

| Arquivo | Papel |
|---------|-------|
| `README.md` | Este guia: visão geral + porquê da metodologia |
| `PRD.md` | Problema, objetivo, fora do escopo, user stories |
| `SPEC.json` | **A lista de tarefas**: sprints, features, critérios de aceite, edge cases |
| `ESTADO.md` | Estado atual e **ponteiro para a próxima sprint** (ler primeiro) |
| `CLAUDE.md` | Regras permanentes do projeto + garbage collection |

---

## 5. Estrutura de pastas

```text
tp1/
├── README.md, PRD.md, SPEC.json, ESTADO.md, CLAUDE.md   # harness
├── TP1.md                                               # enunciado oficial
├── especificacoes-tp1-claude.md                         # briefing de tutoria
├── apostila/            # (sprint-01) material de estudo M0–M9
├── design/              # (sprints 02,03,05) conceito, formalização, análise
├── entrega/             # (sprint-06) slides + declaração de IA
└── TP1-Codigos-e-Benchmarks/
    ├── python/          # student_template, classical, authorial(DPES), metrics, benchmark, test_suite
    └── cpp/             # baselines em C++ (referência)
```

> Os PDFs das aulas (`Aula1.pdf`, `Aula2.pdf`) **não** são versionados — não fazem parte do trabalho.

---

## 6. Sprints (resumo)

| # | Sprint | Executor | Papel do aluno |
|---|--------|----------|----------------|
| 0 | Setup do repo git | IA (infra) | revisa |
| 1 | Apostila de estudo (M0–M9) | Sonnet (janela limpa) | revisa/estuda |
| 2 | Brainstorming do conceito autoral | Colaborativo | decide |
| 3 | Formalização + invariante | Aluno escreve | escreve |
| 4 | Implementação + instrumentação (TDD) | Aluno coda | escreve |
| 5 | Análise assintótica formal | Aluno deduz | escreve |
| 6 | Slides + Declaração de IA | Aluno + IA | escreve/apresenta |

Detalhe completo e critérios de aceite: ver `SPEC.json`.

---

## 7. Referência bibliográfica oficial

CORMEN, T.; LEISERSON, C.; RIVEST, R.; STEIN, C. **Algoritmos: Teoria e Prática.** Campus, 2002.
(Cap. 2 — citado no slide 27 da Aula 2 da disciplina.) Complementares: Sedgewick & Wayne
(*Algorithms*, 4th ed.), Ziviani (*Projeto de Algoritmos*), Knuth (*TAOCP* Vol. 3).
