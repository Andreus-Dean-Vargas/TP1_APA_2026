# CLAUDE.md — TP1: Método de Ordenação Autoral

> Breadcrumb de contexto permanente do projeto. Regras aqui sobrevivem entre sessões — o histórico do chat não.

## Contexto

Trabalho Prático 1 da disciplina *Análise e Projeto de Algoritmos (ES)*. O aluno deve conceber e
defender um **método de ordenação autoral**. Trabalhamos no fluxo **Harness + SDD + TDD**: cada sprint
roda em janela limpa, guiada por `SPEC.json` + `ESTADO.md`. A avaliação premia **domínio teórico e
defesa oral**, não performance bruta.

---

## Padrões obrigatórios deste projeto

- **Tutor socrático, não entregador de solução.** Em sprints com `papel_do_aluno: escreve`, a IA guia
  por perguntas, revisa e explica — o ALUNO redige o código/prova. Nunca colar solução pronta.
- **Janela limpa por sprint.** Nunca iniciar uma nova sprint no mesmo chat da anterior. Ler `ESTADO.md`
  primeiro; consultar a sprint no `SPEC.json`; apresentar critérios de aceite e aguardar aprovação.
- **PT-BR** em todos os artefatos.
- **Contrato de sort:** toda função retorna `(lista_ordenada, comparacoes, movimentacoes)`.
- **`authorial.py` (DPES) é exemplo do professor** — usar só como estudo de caso, nunca como solução.
- **Ancorar teoria no CLRS** (bibliografia oficial, Cap. 2 citado no slide 27 da Aula2); validar
  afirmações de complexidade em ≥2 fontes.
- **TDD** na implementação (skill `tdd-workflow`): testes antes/junto, nunca depois.
- Docs `.md` não excedem ~350 linhas — dividir quando necessário.
- **Um commit por sprint fechada** (Fase F), com atualização de `ESTADO.md` e `SPEC.json`.

## Anti-nota-0 (checklist crítico)

- Passar em 100% da suíte (`test_suite.py`) — falha em qualquer cenário = 0,0.
- Declaração de IA presente e transparente = obrigatória; ausência = 0,0.
- Autoria genuína (não variação cosmética de clássico) = obrigatória.
- Aluno deve saber defender invariante, complexidade e originalidade na arguição.

---

## Regras aprendidas (Garbage Collection)

> Toda correção manual vira uma regra aqui. Formato: [data] regra — erro que a originou.

- [2026-09-08] Não executar sprints automaticamente; o valor está em produzir o artefato de harness
  (SPEC/ESTADO) e executar cada sprint em janela limpa sob revisão do aluno — o erro foi começar a
  rodar a Sprint 0 inteira sem antes montar a lista de tarefas.

---

## Comandos úteis

| Comando | O que faz |
|---------|-----------|
| `python student_template.py` | roda os testes de sanidade do autoral |
| `python test_suite.py` | suíte obrigatória (10 cenários) |
| `python benchmark.py --trials 3 --plot benchmark_results.png` | benchmark + gráficos |
| `git add -A && git commit -m "..."` | fechar sprint |
| `git push` | enviar ao repo (sem re-login, via gh) |

> Comandos Python rodam em `TP1-Codigos-e-Benchmarks/python/`.

---

## Referências

- `README.md` — visão geral do projeto e da metodologia (por que trabalhamos assim)
- `PRD.md` — problema, objetivo, fora do escopo, user stories
- `SPEC.json` — sprints, features, critérios de aceite, edge cases
- `ESTADO.md` — estado atual e próxima sprint
- `TP1.md` — enunciado oficial
