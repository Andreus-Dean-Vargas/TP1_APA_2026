# M7 — Limite Inferior Ω(n log n) por Comparação

**Objetivo:** Entender a prova de que nenhum algoritmo de ordenação por comparação pode ser
melhor que Ω(n log n) no pior caso — e por que Counting Sort e Radix Sort escapam desse limite.

---

## 1. O limite fundamental

**Teorema (CLRS Cap. 8.1):** qualquer algoritmo de ordenação baseado em comparações requer
Ω(n log n) comparações no pior caso.

Isso significa que Merge Sort e Heap Sort são **ótimos** (Θ(n log n)) para algoritmos por
comparação. Você nunca conseguirá fazer melhor usando apenas `a[i] < a[j]`.

---

## 2. Prova pela árvore de decisão

### O modelo

Um algoritmo de ordenação por comparação pode ser modelado como uma **árvore de decisão binária**:

- Cada nó interno representa uma comparação `a[i] : a[j]`
- Cada ramo é o resultado (≤ ou >)
- Cada **folha** representa uma permutação final da entrada

### Limite na altura da árvore

Para n elementos, há **n! permutações possíveis** — uma por folha.

Uma árvore binária de altura h tem no máximo 2^h folhas. Logo:

```
2^h ≥ n!
h ≥ log₂(n!)
```

### Aplicando a aproximação de Stirling

```
log₂(n!) = log₂(n · (n-1) · … · 1)
          ≥ log₂((n/2)^{n/2})    (produto dos n/2 maiores termos)
          = (n/2) · log₂(n/2)
          = (n/2) · (log₂ n − 1)
          = Ω(n log n)
```

Portanto, todo algoritmo de comparação tem altura h = Ω(n log n), o que significa que existe
uma entrada que requer Ω(n log n) comparações.

### Interpretação visual para n = 3

Entrada: [a, b, c]. 3! = 6 permutações → árvore com ≥ 6 folhas → altura ≥ ⌈log₂ 6⌉ = 3.

```
            a:b
           /   \
         ≤      >
        a:c    a:c
       /   \  /   \
      ≤    > ≤    >
    [abc] [acb] [cab] b:c
                    /   \
                  ≤      >
               [bac]   b:c
                       /  \
                      ≤    >
                   [bca] [cba]
```

Toda folha representa uma permutação. Há pelo menos uma folha à profundidade ≥ 3.

---

## 3. Exemplo numérico — contando o mínimo de comparações

Para n = 4: n! = 24 permutações. Altura mínima da árvore = ⌈log₂ 24⌉ = 5.
Portanto, qualquer sort por comparação com n=4 precisa de ≥ 5 comparações no pior caso.

Inserção Sort com n=4, reverso: compara 3+2+1 = 6. Está acima do mínimo teórico — não ótimo.
Merge Sort com n=4: usa ≈ 5 comparações. Próximo ao ótimo.

---

## 4. Por que Counting Sort e Radix Sort escapam?

Esses algoritmos **não comparam elementos entre si** — usam o valor numérico como índice.

| Algoritmo | Comparações? | Complexidade | Limitação |
|-----------|-------------|-------------|-----------|
| Counting Sort | Não | O(n + k), k = max valor | k deve ser O(n) |
| Radix Sort | Não | O(d · n), d = dígitos | Só funciona com chaves inteiras/fixas |

O limite Ω(n log n) vale **apenas para o modelo de comparação**. Se você tem informação extra
sobre os valores (ex: inteiros em [0, k]), pode usá-la para quebrar o limite.

**Para o seu autoral:** se usar apenas comparações (`<`, `>`, `==`), você está sujeito ao
limite. Se seu algoritmo for O(n log n) no médio, isso é ótimo — e você pode dizer isso na
defesa.

---

## 5. Implicação para o TP1

| Cenário | O que dizer na defesa |
|---------|----------------------|
| Seu autoral é Θ(n log n) médio | "Atinge o limite ótimo para algoritmos por comparação" |
| Seu autoral é O(n²) pior | "Tem pior caso subótimo, similar ao Quick Sort sem garantia de balanceamento" |
| Seu autoral é O(n) em casos especiais | Impossível por comparação para o caso geral — explique qual restrição de entrada permite isso |

---

## Referências

- **CLRS Cap. 8.1** — "Lower bounds for sorting" — prova completa com árvore de decisão.
  Livro: Cormen et al., *Algoritmos: Teoria e Prática*, Campus, 2002, pp. 165–170.
- **CLRS Cap. 8.2** — "Counting Sort" — O(n+k).
- **CLRS Cap. 8.3** — "Radix Sort" — O(d·n).
- **Sedgewick & Wayne, Cap. 2.4** — "Priority Queues" e referências a lower bounds.
  Online: <https://algs4.cs.princeton.edu/24pq/>
- **Knuth, TAOCP Vol. 3, Sec. 5.3.1** — prova original do limite inferior por árvore de decisão.
