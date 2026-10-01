# ESTADO — TP1 Ordenação Autoral

> Ponteiro de estado do projeto. **Leia este arquivo primeiro** ao abrir uma janela limpa.
> Ele diz qual é a próxima sprint. O detalhe de cada sprint está no `SPEC.json`.

**Última atualização:** 2026-10-01

---

## 🎯 Próxima sprint a executar

Nenhuma — todas as sprints fechadas. TP1 pronto para envio (ver "Pendências imediatas").

---

## 📊 Quadro de sprints

| Sprint | Objetivo | Executor | Papel do aluno | Status |
|--------|----------|----------|----------------|--------|
| sprint-00 | Setup do repo git | IA (infra) | revisa | 🟢 done |
| sprint-01 | Apostila de estudo (M0–M9) | Sonnet (janela limpa) | revisa/estuda | 🟢 done |
| sprint-02 | Brainstorming do conceito autoral | Colaborativo | decide | 🟢 done |
| sprint-03 | Formalização + invariante | Aluno escreve | escreve (⚠️ IA executou por urgência de prazo — ver declaração de IA) | 🟢 done |
| sprint-04 | Implementação (TDD) | Aluno coda | escreve (⚠️ IA executou por urgência de prazo — ver declaração de IA) | 🟢 done |
| sprint-05 | Análise assintótica | Aluno deduz | escreve (⚠️ IA executou por urgência de prazo — ver declaração de IA) | 🟢 done |
| sprint-06 | Declaração de IA (sem slides — aluno decidiu não apresentar este TP) | Aluno + IA | escreve | 🟢 done |
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

1. Nenhuma pendência de sprint. Antes de enviar: revisar `entrega/declaracao-ia.md` e confirmar que
   reflete a realidade (foi escrita de forma honesta, incluindo a parte desconfortável — IA
   escreveu sprints 03–05 integralmente).
2. **Sem slides nem relatório formal** — decisão do aluno, já que este TP não será apresentado/
   defendido oralmente. Nota: os arquivos `design/conceito-autoral.md` + `design/formalizacao.md`
   + `design/analise-assintotica.md`, juntos, já cobrem o conteúdo exigido pela "Opção A —
   Relatório Técnico" do `TP1.md` (ainda que não consolidados num único documento) — útil caso o
   professor pergunte pelo relatório.

---

## 📝 Decisões registradas

- Entrega final = **apresentação de slides** (+ código executável obrigatório).
- Algoritmo autoral = **brainstorming do zero** (não reaproveitar o DPES do professor).
- Idioma de todos os artefatos = **PT-BR**.
- Repo versiona **só o TP1** (git dentro de `tp1/`), sem os PDFs das aulas.
- **Conceito fechado na sprint-02: SCED** (Seleção Convergente de Extremos Distintos). Adaptação
  declarada do Bingo Sort (NIST DADS) com extensão bidirecional convergente. Risco de originalidade
  (dúvida 1 do professor) aceito sem consulta prévia — justificativa completa em
  `design/duvidas-professor.md` (seção "Fechamento da sprint-02").
