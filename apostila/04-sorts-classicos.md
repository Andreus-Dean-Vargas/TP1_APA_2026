# M4 — Os 5 Sorts Clássicos

**Objetivo:** Conhecer os 5 algoritmos implementados em `classical.py` — intuição, complexidade,
estabilidade, in-place — para usá-los como referência comparativa no TP1.

---

## Tabela comparativa

| Algoritmo | Melhor | Pior | Médio | Espaço | Estável | In-place | Arquivo |
|-----------|--------|------|-------|--------|---------|----------|---------|
| Bubble Sort | O(n) | O(n²) | Θ(n²) | O(1) | ✓ | ✓ | `classical.py:9` |
| Selection Sort | Θ(n²) | Θ(n²) | Θ(n²) | O(1) | ✗ | ✓ | `classical.py:34` |
| Insertion Sort | O(n) | O(n²) | Θ(n²) | O(1) | ✓ | ✓ | `classical.py:58` |
| Merge Sort | Θ(n log n) | Θ(n log n) | Θ(n log n) | O(n) | ✓ | ✗ | `classical.py:87` |
| Quick Sort | Ω(n log n) | O(n²) | Θ(n log n) | O(log n)¹ | ✗ | ✓ | `classical.py:139` |

¹ Espaço da pilha de recursão com mediana-de-três.

---

## 1. Bubble Sort — `classical.py:9–31`

**Intuição:** Repetidamente passa pela lista comparando elementos adjacentes e trocando os que
estão fora de ordem. Os elementos "pesados" borbulham para o fim.

**Otimização implementada:** flag `swapped` na linha 21 — se nenhuma troca ocorreu, o vetor
já está ordenado e o algoritmo para em O(n).

**Números reais (benchmark seed=42, 2 trials):**

| Distribuição | N=100 (comps/moves) | N=1000 (comps/moves) |
|--------------|--------------------|--------------------|
| random | 4931 / 5153 | não medido (lento) |
| sorted | 99 / 0 | 999 / 0 |
| reverse | 4950 / 9900 | não medido |
| duplicates | 4729 / 3706 | 481633 / 403857 |

**Ponto-chave:** no melhor caso (sorted), 0 movimentações — a flag `swapped` paga dividendo.

---

## 2. Selection Sort — `classical.py:34–55`

**Intuição:** Busca o mínimo no subvetor não-ordenado e o coloca na posição correta. Faz
exatamente n−1 trocas no pior caso — mínimo de movimentações possível.

**Números reais:**

| Distribuição | N=100 (comps/moves) | N=1000 (comps/moves) |
|--------------|--------------------|--------------------|
| random | 4950 / 195 | 499500 / 1984 |
| sorted | 4950 / 0 | 499500 / 0 |
| reverse | 4950 / 100 | não medido |

**Ponto-chave:** comparações = n(n-1)/2 sempre (nunca para cedo); movimentações ≤ 2(n-1).
Ótimo quando mover é custoso, mas comparar é barato.

---

## 3. Insertion Sort — `classical.py:58–84`

**Intuição:** Mantém a parte esquerda do vetor ordenada. Para cada novo elemento, insere-o
na posição correta por deslocamento (shift) — como ordenar cartas na mão.

**Números reais:**

| Distribuição | N=100 (comps/moves) | N=1000 (comps/moves) |
|--------------|--------------------|--------------------|
| random | 2671 / 2774 | 247804 / 248809 |
| sorted | 99 / 198 | 999 / 1998 |
| reverse | 4950 / 5148 | 499500 / 501498 |
| almost_sorted | 361 / 461 | 32408 / 33407 |

**Ponto-chave:** quase-ordenado → excelente (O(n) + pequenas constantes). É o algoritmo de
referência para partições pequenas em algoritmos híbridos (como o DPES usa para n ≤ 16).

---

## 4. Merge Sort — `classical.py:87–136`

**Intuição:** Divide o vetor ao meio recursivamente, ordena cada metade e depois faz o merge
(intercalação) das duas metades já ordenadas.

**Números reais:**

| Distribuição | N=100 (comps/moves) | N=1000 (comps/moves) |
|--------------|--------------------|--------------------|
| random | 543 / 672 | 8688 / 9976 |
| sorted | 316 / 672 | 4932 / 9976 |
| reverse | 356 / 672 | 5044 / 9976 |
| duplicates | 525 / 672 | 8122 / 9976 |

**Movimentações sempre iguais** (= n·⌈log₂ n⌉ na prática) porque o merge sempre percorre todo
o vetor — independente da distribuição.

**Custo:** precisa de O(n) de memória auxiliar para o merge (linha 110: lista `merged`).

---

## 5. Quick Sort — `classical.py:139–204`

**Intuição:** Escolhe um pivô, particiona o vetor (menores à esquerda, maiores à direita) e
ordena as partições recursivamente. Pivô bem escolhido → partições equilibradas → O(n log n).

**Implementação:** pivô por mediana-de-três (`_median_of_three`, linha 153) para evitar o
pior caso em vetores já ordenados.

**Números reais:**

| Distribuição | N=100 (comps/moves) | N=1000 (comps/moves) |
|--------------|--------------------|--------------------|
| random | 996 / 365 | 13711 / 5351 |
| sorted | 795 / 0 | 10542 / 0 |
| reverse | 799 / 104 | 10549 / 1004 |
| duplicates | 932 / 467 | 11823 / 7674 |

**Ponto-chave:** poucas movimentações (trocas de elementos distantes) — mais cache-friendly
na prática que o Merge Sort, apesar do mesmo Θ(n log n).

---

## Como usar na defesa

Ao comparar seu autoral com os clássicos, mostre **ao menos 2** destas referências. A tabela
comparativa nos slides deve incluir comparações e movimentações para ≥2 distribuições.

---

## Referências

- **CLRS Cap. 2** (Insertion, Merge), **Cap. 7** (Quick Sort), **Cap. 8** — todos os sorts deste módulo.
  Livro: Cormen et al., *Algoritmos: Teoria e Prática*, Campus, 2002.
- **Sedgewick & Wayne, Cap. 2** — "Sorting" — cobertura completa dos 5 sorts com análise empírica.
  Online: <https://algs4.cs.princeton.edu/20sorting/>
- **Ziviani, Cap. 4** — "Ordenação" — Insertion, Selection e Merge em PT-BR com prova formal.
