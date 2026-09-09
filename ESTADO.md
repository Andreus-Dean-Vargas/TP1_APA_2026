# ESTADO — TP1 Ordenação Autoral

> Ponteiro de estado do projeto. **Leia este arquivo primeiro** ao abrir uma janela limpa.
> Ele diz qual é a próxima sprint. O detalhe de cada sprint está no `SPEC.json`.

**Última atualização:** 2026-09-08

---

## 🎯 Próxima sprint a executar

**`sprint-02` — Brainstorming do conceito autoral** (status: `pending`)

Executor: **Colaborativo (IA propõe, aluno decide)**. Abra um chat novo e peça para conduzir
a `sprint-02` lendo este `ESTADO.md` + `SPEC.json`. Papel do aluno: decidir e refinar.

---

## 📊 Quadro de sprints

| Sprint | Objetivo | Executor | Papel do aluno | Status |
|--------|----------|----------|----------------|--------|
| sprint-00 | Setup do repo git | IA (infra) | revisa | 🟢 done |
| sprint-01 | Apostila de estudo (M0–M9) | Sonnet (janela limpa) | revisa/estuda | 🟢 done |
| sprint-02 | Brainstorming do conceito autoral | Colaborativo | decide | ⚪ pending |
| sprint-03 | Formalização + invariante | Aluno escreve | escreve | ⚪ pending |
| sprint-04 | Implementação + instrumentação (TDD) | Aluno coda | escreve | ⚪ pending |
| sprint-05 | Análise assintótica formal | Aluno deduz | escreve | ⚪ pending |
| sprint-06 | Slides + Declaração de IA | Aluno + IA | escreve/apresenta | ⚪ pending |

Legenda: 🟢 done · 🟡 in_progress · ⚪ pending

---

## ✅ O que já foi feito

- **Pesquisa & Discovery:** lidos o enunciado (`TP1.md`), as `Regras_do_Jogo.md`, o briefing
  (`especificacoes-tp1-claude.md`), todo o código Python fornecido e os PDFs das aulas.
- **Achado-chave:** bibliografia oficial = **CLRS, Cap. 2** (slide 27 da Aula2).
- **Arquivos primordiais criados:** `PRD.md`, `SPEC.json`, `ESTADO.md`, `CLAUDE.md`, `README.md`.
- **Infra git:** `git init` em `tp1/`, branch `main`, remote `origin`, `.gitignore` (PDFs fora),
  `gh auth setup-git` (push sem re-login). **Commit inicial + push feitos → `sprint-00` fechada.**
- **Apostila criada:** `apostila/` com 10 módulos M0–M9 (PT-BR, ≤108 linhas cada). Números
  empíricos extraídos rodando o benchmark (seed=42). **`sprint-01` fechada.**

---

## ⏭️ Pendências imediatas

1. Estudar os módulos M0–M9 da `apostila/` antes de iniciar a sprint-02.
2. Abrir janela limpa → iniciar `sprint-02` (Brainstorming): "leia ESTADO.md + SPEC.json e conduza a sprint-02".

---

## 📝 Decisões registradas

- Entrega final = **apresentação de slides** (+ código executável obrigatório).
- Algoritmo autoral = **brainstorming do zero** (não reaproveitar o DPES do professor).
- Idioma de todos os artefatos = **PT-BR**.
- Repo versiona **só o TP1** (git dentro de `tp1/`), sem os PDFs das aulas.
