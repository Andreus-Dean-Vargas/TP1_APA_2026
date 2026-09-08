# PRD — TP1: Método de Ordenação Autoral

> Documento de produto/objetivo do trabalho. Foco no "o quê" e no "por quê".
> O "como" técnico está no `SPEC.json`.

---

## Problema

A disciplina *Análise e Projeto de Algoritmos (ES)* exige que o aluno **conceba, formalize,
implemente e valide um método de ordenação autoral** — e, principalmente, **saiba defendê-lo
oralmente**. O risco central não é o algoritmo ser lento (performance bruta não é o foco), e sim:

- não saber deduzir/justificar a complexidade (O, Ω, Θ);
- não conseguir provar corretude (invariante de laço);
- entregar algo que pareça cópia/variação trivial de um clássico;
- não dominar a própria solução na arguição.

Qualquer um desses leva a **nota 0,0** (rejeição sumária). Logo, o problema real é
**construir domínio genuíno**, não apenas "código que ordena".

---

## Objetivo

Chegar à entrega com o aluno tendo **pleno domínio** da solução, produzindo:

1. Uma **apostila de estudo** que dê a base teórica (ancorada em CLRS e complementares).
2. Um **algoritmo de ordenação autoral** defensável (não-trivial, com invariante e análise).
3. **Validação empírica** na suíte obrigatória + benchmark comparativo.
4. **Slides** de apresentação + **declaração de uso de IA** transparente.

**Como saberemos que teve sucesso:**
- Todos os 10 cenários da suíte passam.
- Melhor/pior/médio caso e espaço deduzidos e consistentes com o benchmark.
- O aluno consegue responder a arguição sobre invariante, complexidade e originalidade.
- Entrega cobre 100% dos itens obrigatórios do enunciado.

---

## Fora do Escopo

- [ ] Otimização de performance bruta (não é critério de avaliação).
- [ ] Reaproveitar o DPES (`authorial.py`) como solução — é exemplo do professor.
- [ ] Implementação em C++ do autoral (o pacote tem baseline C++, mas o autoral será em Python).
- [ ] Qualquer feature além dos itens obrigatórios do enunciado.

---

## User Stories

- Como **aluno**, quero uma apostila ancorada nas referências reais da disciplina para que eu
  entenda de verdade os fundamentos antes de codar.
- Como **aluno**, quero um fluxo de sprints em janelas limpas para que a IA não entre na "Dumb Zone"
  e eu mantenha o controle e o aprendizado.
- Como **aluno**, quero escrever eu mesmo a maior parte do código/prova para que eu domine a solução
  e sobreviva à defesa oral.
- Como **avaliador (professor)**, quero ver autoria genuína, análise correta e declaração de IA para
  atribuir a nota com confiança.

---

## Restrições e Dependências

| Tipo | Descrição |
|------|-----------|
| Acadêmica | Deve passar em 100% da suíte; sem isso → nota 0,0 |
| Acadêmica | Declaração de IA obrigatória; sem ela → nota 0,0 |
| Acadêmica | Autoria genuína; variação cosmética de clássico → nota 0,0 |
| Bibliográfica | Ancorar teoria no CLRS (Cap. 2 citado oficialmente) |
| Técnica | Contrato de sort: `(arr) -> (lista, comparacoes, movimentacoes)` |
| Entrega | Formato = apresentação de slides + código executável |
| Prazo | Atividade prática (~1 semana, conforme Regras do Jogo) |

---

## Personas

**Aluno (Andreus / Dean):** autor do trabalho; quer aprender de fato e demonstrar uso inteligente
de IA (concorrendo ao bônus "Uso Excepcional de IA"). Escreve a maior parte do código.

**Professores (Diogo Mainart / Marcelo Luizelli):** avaliam raciocínio projetual, análise teórica,
corretude e capacidade de defesa oral.

---

## Referências

- `TP1.md` — enunciado oficial do trabalho.
- `Regras_do_Jogo.md` — integridade acadêmica, uso de IA, composição da nota (na pasta-mãe APA).
- `especificacoes-tp1-claude.md` — briefing do workflow de tutoria socrática.
- CLRS — *Algoritmos: Teoria e Prática*, Campus, 2002 (Cap. 2) — bibliografia oficial.
