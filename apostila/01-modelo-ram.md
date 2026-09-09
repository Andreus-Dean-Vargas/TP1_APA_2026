# M1 — Modelo RAM e Custo por Linha T(n)

**Objetivo:** Entender como o modelo RAM transforma código em expressão matemática T(n),
reproduzindo a análise do Insertion Sort que aparece nos slides 16–24 da Aula2 (baseados no CLRS
Cap. 2.2).

---

## 1. O Modelo RAM

O **modelo de acesso aleatório** (Random Access Machine) é uma máquina idealizada usada para
análise de algoritmos. Suas premissas:

- Cada operação primitiva (comparação, atribuição, aritmética, acesso a índice) custa **tempo
  constante** — chame de cᵢ, onde i é o número da linha.
- Memória é acessada em tempo constante, sem hierarquia de cache.
- Não há paralelismo: instruções executam uma de cada vez.

A **abstração do modelo RAM** permite ignorar detalhes de hardware e focar no crescimento com n.

---

## 2. T(n) = Σ cᵢ · (número de vezes que a linha i executa)

Para um algoritmo com linhas L₁, L₂, …, Lₖ:

```
T(n) = c₁·t₁ + c₂·t₂ + … + cₖ·tₖ
```

onde tᵢ é o número de vezes que a linha i é executada para uma entrada de tamanho n.

---

## 3. Exemplo: Insertion Sort passo a passo

Código de referência: `classical.py:58–84`.

```python
# linha  código                          custo   #vezes
#  1     for i in range(1, n):           c1      n
#  2         key = a[i]                  c2      n-1
#  3         moves += 1                  c3      n-1
#  4         j = i - 1                   c4      n-1
#  5         while j >= 0:               c5      Σtⱼ (j=2..n)
#  6             comps += 1              c6      Σ(tⱼ-1)
#  7             if a[j] > key:          c7      Σ(tⱼ-1)
#  8                 a[j+1] = a[j]       c8      Σ(tⱼ-1)   [pior caso]
#  9                 moves += 1          c9      Σ(tⱼ-1)
#  10                j -= 1             c10      Σ(tⱼ-1)
#  11        a[j+1] = key               c11      n-1
#  12        moves += 1                 c12      n-1
```

**tⱼ** = número de vezes que o `while` na iteração j é testado.

### Melhor caso — vetor já ordenado

Em cada iteração i, `a[j] <= key` imediatamente → tⱼ = 1 para todo j.

```
T(n) = c1·n + (c2+c3+c4+c11+c12)·(n-1) + c5·(n-1) + (c6+c7)·0 + …
     = An + B   →   T(n) = Θ(n)
```

O while nunca entra no corpo (vetor já ordenado ⇒ nenhuma comparação extra).

### Pior caso — vetor em ordem reversa

Em cada iteração i, o elemento `key` vai até o início → tⱼ = i.
Assim Σtⱼ = 2 + 3 + … + n = n(n+1)/2 − 1.

```
T(n) = c1·n + … + c5·[n(n+1)/2 - 1] + (c6+c7+c8)·[n(n-1)/2] + …
     = An² + Bn + C   →   T(n) = Θ(n²)
```

---

## 4. Exemplo numérico — entrada [5, 2, 4, 6, 1, 3]

| i | key | Comparações do while | Resultado parcial |
|---|-----|----------------------|-------------------|
| 1 | 2   | a[0]=5 > 2 → desloca | [2, 5, 4, 6, 1, 3] |
| 2 | 4   | a[1]=5 > 4 → desloca; a[0]=2 ≤ 4 → para | [2, 4, 5, 6, 1, 3] |
| 3 | 6   | a[2]=5 ≤ 6 → para | [2, 4, 5, 6, 1, 3] |
| 4 | 1   | a[2]=5, a[1]=4, a[0]=2, inicio → desloca 3× | [1, 2, 4, 5, 6, 3] |
| 5 | 3   | a[3]=5, a[2]=4, a[1]=2 ≤ 3 → para | [1, 2, 3, 4, 5, 6] |

Comparações totais: 1+2+1+4+3 = **11** (para n=6).
Benchmark real para Insertion Sort com n=100, random: **≈ 2671 comparações**.

---

## 5. Conexão com o código

| O quê | Onde |
|-------|------|
| Laço externo `for i` | `classical.py:69` |
| Extração da chave `key = a[i]` | `classical.py:70` |
| Laço interno `while j >= 0` | `classical.py:73` |
| Deslocamento `a[j+1] = a[j]` | `classical.py:76` |
| Inserção final `a[j+1] = key` | `classical.py:81` |
| Contabilização de `comps` e `moves` | `classical.py:74, 77, 71, 82` |

---

## Referências

- **CLRS Cap. 2.2** — "Analysing algorithms" — dedução linha a linha de T(n) para Insertion Sort.
  Livro: Cormen et al., *Algoritmos: Teoria e Prática*, Campus, 2002, pp. 28–32.
- **Sedgewick & Wayne, Cap. 2.1** — análise de custo dos sorts elementares.
  Online: <https://algs4.cs.princeton.edu/21elementary/>
- **Ziviani, Cap. 2** — "Análise de algoritmos" — terminologia em PT-BR e mesma dedução.
