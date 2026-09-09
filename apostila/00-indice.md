# M0 — Mapa do TP1

**Objetivo:** Entender exatamente o que é avaliado, quais são os critérios de nota e o que
causa nota 0,0 — antes de estudar qualquer teoria.

---

## O que é o TP1

Você deve **conceber um método de ordenação autoral**, apresentá-lo em slides e defendê-lo
oralmente. "Autoral" significa que a ideia central é sua — não é renomear um clássico, não é
mesclar dois sem diferencial claro.

O trabalho tem três pilares indissociáveis:

| Pilar | O que mostra |
|-------|-------------|
| Teoria (invariante + análise) | Que você entende por que o algoritmo funciona |
| Código executável | Que a ideia é concreta e verificável |
| Defesa oral | Que você domina — não só reproduz |

---

## Itens obrigatórios (checklist de entrega)

- [ ] **Intuição/metáfora** — explicar a ideia sem fórmulas
- [ ] **Pseudocódigo** — inequívoco, traduzível diretamente para código
- [ ] **Invariante de laço** — inicialização / manutenção / término (veja M3)
- [ ] **Exemplo numérico passo a passo** — executado à mão
- [ ] **Análise assintótica** — melhor caso O, pior caso O, caso médio Θ, espaço auxiliar
- [ ] **Tabela comparativa** — seu algoritmo vs ≥ 2 clássicos (comparações, movimentações)
- [ ] **Gráficos empíricos** — curvas de comparações/movimentações × N
- [ ] **Código Python executável** — contrato `(arr) → (lista_ordenada, comps, moves)`
- [ ] **100% de aprovação em `test_suite.py`** — todos os 10 cenários passam
- [ ] **Declaração de uso de IA** — ferramenta, por quê, como, o que foi modificado, como validado

---

## O que causa nota 0,0

| Situação | Por quê é fatal |
|----------|----------------|
| Algoritmo é variação cosmética de clássico | Sem originalidade — critério central do TP |
| Qualquer cenário de `test_suite.py` falha | Código incorreto invalida tudo |
| Ausência de declaração de IA | Regra explícita do enunciado |
| Sem código executável | Não há como verificar |
| Aluno não sabe defender invariante/complexidade | A nota vem da arguição |

---

## Mapa da apostila e conexão com as sprints

| Módulo | Conteúdo | Para qual sprint serve |
|--------|----------|----------------------|
| M1 | Modelo RAM — como medir custo de algoritmo | sprint-05 (análise) |
| M2 | Notação O/Ω/Θ — linguagem formal de complexidade | sprint-05 |
| M3 | Invariante de laço — prova de corretude | sprint-03 (formalização) |
| M4 | Os 5 clássicos — benchmark e referência | sprint-02 (brainstorming) |
| M5 | Recorrências — análise de algoritmos recursivos | sprint-05 |
| M6 | Estabilidade e in-place — propriedades do autoral | sprint-02 e sprint-03 |
| M7 | Limite inferior Ω(n log n) — por que não dá para fazer melhor | sprint-05 |
| M8 | Medição empírica — como rodar e interpretar o benchmark | sprint-04 e sprint-05 |
| M9 | Guia de defesa oral — perguntas prováveis + anti-nota-0 | sprint-06 (apresentação) |

---

## Referências do TP1

- **CLRS** — Cormen, Leiserson, Rivest, Stein. *Algoritmos: Teoria e Prática*, Campus, 2002.
  Capítulos 2 (fundamentos), 3 (notação), 4 (D&C), 7 (QuickSort), 8 (limite inferior).
  *Fonte primária.* Citada no slide 27 da Aula2.
- **Sedgewick & Wayne** — *Algorithms*, 4ª ed. Addison-Wesley, 2011.
  Material online: <https://algs4.cs.princeton.edu/home/>
- **Ziviani** — *Projeto de Algoritmos*, Thomson, 2004. Terminologia em PT-BR.
- **Knuth** — *TAOCP Vol. 3: Sorting and Searching*. Addison-Wesley, 1998. Referência histórica.
