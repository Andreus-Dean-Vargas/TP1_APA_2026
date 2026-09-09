# M6 — Estabilidade e In-place

**Objetivo:** Entender as propriedades de estabilidade e in-place de algoritmos de ordenação,
saber prová-las (ou refutá-las) e reconhecer os trade-offs — cobertos na defesa oral.

---

## 1. Estabilidade

### Definição

Um algoritmo de ordenação é **estável** se, para quaisquer dois elementos iguais a[i] = a[j]
com i < j na entrada, a[i] aparece antes de a[j] na saída.

Em outras palavras: **elementos iguais preservam sua ordem relativa original**.

### Por que importa?

Ao ordenar registros por múltiplas chaves (ex: nome dentro de departamento), a estabilidade
garante que uma segunda ordenação não desfaz a primeira.

### Como provar estabilidade

Mostre que o algoritmo **nunca troca dois elementos iguais de posição**.

Para o Insertion Sort (`classical.py:73–80`): o `while` entra apenas quando `a[j] > key`
(linha 75) — se `a[j] == key`, para imediatamente. Logo, elementos iguais nunca são
reordenados. **Insertion Sort é estável.** ✓

Para refutar (Selection Sort): construa um contra-exemplo concreto.

| Entrada | Esperado (estável) | Selection Sort produz |
|---------|-------------------|-----------------------|
| [(3,a), (1,b), (3,c), (2,d)] | [(1,b),(2,d),(3,a),(3,c)] | pode trocar (3,a) com (1,b) diretamente |

A troca direta (linha 52 de `classical.py`) pode pular elementos iguais — logo não é estável.

---

## 2. Classificação dos 5 sorts

| Algoritmo | Estável? | Justificativa |
|-----------|----------|---------------|
| Bubble Sort | ✓ | Só troca adjacentes quando estritamente maior (`a[j] > a[j+1]`) |
| Selection Sort | ✗ | Troca direta pode alterar ordem relativa de iguais |
| Insertion Sort | ✓ | Desloca apenas quando `a[j] > key` (não ≥) |
| Merge Sort | ✓ | Merge prefere o elemento da esquerda quando iguais (`left[i] <= right[j]`) |
| Quick Sort | ✗ | Troca de elementos não-adjacentes pode inverter iguais |

Código: Merge Sort (`classical.py:114`): `if left[i] <= right[j]` — o `<=` garante que
elementos iguais da metade esquerda venham primeiro.

---

## 3. In-place

### Definição

Um algoritmo é **in-place** se usa O(1) de memória auxiliar além da entrada — ou seja,
a quantidade de memória extra não cresce com n.

Variações aceitas na literatura: pilha de recursão de O(log n) (ex: Quick Sort) é
considerada in-place por alguns autores (CLRS, p. 149).

### Classificação

| Algoritmo | In-place? | Memória auxiliar |
|-----------|-----------|-----------------|
| Bubble Sort | ✓ | O(1) — só variáveis de controle |
| Selection Sort | ✓ | O(1) |
| Insertion Sort | ✓ | O(1) — só `key` e índices |
| Merge Sort | ✗ | O(n) — lista `merged` (`classical.py:110`) |
| Quick Sort | ✓* | O(log n) de pilha de recursão |

---

## 4. Trade-offs para o seu autoral

| Decisão | In-place | Não in-place |
|---------|----------|--------------|
| Vantagem | Não aloca memória extra | Mais fácil de implementar (merge) |
| Custo | Mais trocas, maior complexidade de implementação | Usa O(n) ou mais de espaço |

| Decisão | Estável | Não estável |
|---------|---------|-------------|
| Vantagem | Útil para ordenações multi-chave | Pode fazer menos trocas |
| Como garantir | Nunca trocar elementos iguais; usar `<` e não `<=` nos predicados de troca | — |

**Na defesa:** você deve saber dizer explicitamente se seu autoral é estável ou não, e por quê.
Se não for estável, mostre um contra-exemplo concreto para provar que você entende.

---

## 5. Exemplo numérico — refutando estabilidade com contra-exemplo

Entrada: `[3a, 1, 3b, 2]` (3a e 3b têm o mesmo valor 3, ordem original: a antes de b).

Aplicar um algoritmo instável hipotético que troca `3a` com `1` na primeira passagem:

```
Passo 1: troca 3a e 1  →  [1, 3a, 3b, 2]
Passo 2: troca 3a e 3b? Se sim, produz [1, 3b, 3a, 2] → instável!
```

Para provar que *seu* algoritmo é estável, mostre que esse caso não acontece na implementação.

---

## Referências

- **CLRS Cap. 2** — estabilidade mencionada na discussão de Merge Sort (p. 37).
- **CLRS Cap. 8.1** — "Lower bounds for sorting" — menciona propriedades de sorts por comparação.
- **Sedgewick & Wayne, Cap. 2.5** — "Sorting Applications" — estabilidade aplicada e exemplos práticos.
  Online: <https://algs4.cs.princeton.edu/25applications/>
- **Ziviani, Cap. 4.1** — "Estabilidade" — definição formal e classificação em PT-BR.
