# M5 — Recorrências e Divisão-e-Conquista

**Objetivo:** Aprender a modelar algoritmos recursivos com recorrências e resolvê-las com
substituição, árvore de recursão e Teorema Mestre — essencial se seu autoral for recursivo.

---

## 1. O paradigma Divisão-e-Conquista (D&C)

Um algoritmo D&C segue três etapas:

1. **Dividir** — partir o problema em subproblemas menores do mesmo tipo
2. **Conquistar** — resolver os subproblemas recursivamente
3. **Combinar** — juntar as soluções dos subproblemas

A recorrência geral de D&C é:

```
T(n) = a · T(n/b) + f(n)
```

onde `a` = número de subproblemas, `b` = fator de redução, `f(n)` = custo de dividir+combinar.

---

## 2. Merge Sort — recorrência e resolução

Recorrência (CLRS Cap. 2.3):

```
T(n) = 2·T(n/2) + Θ(n)
```

Divisão: 2 subproblemas de tamanho n/2.
Combinação: merge em Θ(n).

**Resolução por árvore de recursão:**

```
Nível 0:  n            →  custo = n
Nível 1:  n/2  n/2     →  custo = n
Nível 2:  n/4 x4       →  custo = n
…
Nível k:  1   x n      →  custo = n   (k = log₂ n níveis)
```

Total = n · log₂ n = **Θ(n log n)**

**Verificação pelo Teorema Mestre (caso 2):** a=2, b=2, f(n)=Θ(n).
n^{log_b a} = n^{log_2 2} = n^1 = n. f(n) = Θ(n^1) → **Caso 2: T(n) = Θ(n log n)**. ✓

---

## 3. Quick Sort — recorrência e pior caso

**Melhor caso** (partição perfeitamente equilibrada):

```
T(n) = 2·T(n/2) + Θ(n)  →  Θ(n log n)
```

**Pior caso** (pivô sempre mínimo ou máximo — ex: vetor sorted sem mediana-de-três):

```
T(n) = T(n-1) + T(0) + Θ(n) = T(n-1) + Θ(n)
```

Resolução por substituição: T(n) = Σ(k=1..n) k = n(n+1)/2 = **Θ(n²)**.

Na implementação de `classical.py:153`, a mediana-de-três garante que o vetor já ordenado
não degenera para O(n²) — mas a análise teórica do pior caso permanece Θ(n²).

---

## 4. Teorema Mestre (versão básica — CLRS Cap. 4.5)

Para T(n) = a·T(n/b) + f(n), com a ≥ 1, b > 1:

| Caso | Condição | Solução |
|------|----------|---------|
| Caso 1 | f(n) = O(n^{log_b a − ε}), ε > 0 | T(n) = Θ(n^{log_b a}) |
| Caso 2 | f(n) = Θ(n^{log_b a}) | T(n) = Θ(n^{log_b a} · log n) |
| Caso 3 | f(n) = Ω(n^{log_b a + ε}), ε > 0 | T(n) = Θ(f(n)) |

**Exemplos:**

| Recorrência | a | b | log_b a | Caso | Solução |
|-------------|---|---|---------|------|---------|
| T=2T(n/2)+n | 2 | 2 | 1 | 2 | Θ(n log n) |
| T=4T(n/2)+n | 4 | 2 | 2 | 1 | Θ(n²) |
| T=T(n/2)+1 | 1 | 2 | 0 | 2 | Θ(log n) |

---

## 5. Estudo de caso: DPES (`authorial.py`) — análise

O DPES é o algoritmo autoral do professor (use apenas como estudo, não como solução).

**Estrutura:** particionamento tripartite → 3 subproblemas + Insertion Sort para n ≤ 16.

Recorrência aproximada (três partições, sem garantia de equilíbrio):

```
T(n) ≈ 3·T(n/3) + Θ(n)
```

Teorema Mestre: a=3, b=3, log₃ 3 = 1. f(n)=Θ(n¹) → Caso 2: **T(n) = Θ(n log n)** (médio).

No pior caso (partições degeneradas), pode ser O(n²) — benchmark mostra ~8.000 comps
para n=500 em random, contra ~3.853 do Merge Sort.

**Para o seu autoral:** se for recursivo, escreva a recorrência T(n) explicitamente e
escolha um dos três métodos para resolvê-la.

---

## 6. Método da substituição — exemplo simples

Provar que T(n) = 2T(n/2) + n = O(n log n).

**Hipótese:** T(n) ≤ c·n·log n para algum c > 0.

**Passo indutivo:** assumindo T(n/2) ≤ c·(n/2)·log(n/2):

```
T(n) = 2T(n/2) + n ≤ 2·c·(n/2)·log(n/2) + n
     = c·n·(log n − 1) + n
     = c·n·log n − c·n + n
     ≤ c·n·log n         (para c ≥ 1)
```

✓ Hipótese confirmada.

---

## Referências

- **CLRS Cap. 4** — "Divide-and-Conquer" — métodos de substituição, árvore de recursão e
  Teorema Mestre com provas completas.
  Livro: Cormen et al., *Algoritmos: Teoria e Prática*, Campus, 2002, pp. 68–111.
- **CLRS Cap. 2.3** — recorrência do Merge Sort (T(n) = 2T(n/2) + Θ(n)).
- **Sedgewick & Wayne, Cap. 2.2** — "Mergesort" — análise da recorrência com diagramas.
  Online: <https://algs4.cs.princeton.edu/22mergesort/>
