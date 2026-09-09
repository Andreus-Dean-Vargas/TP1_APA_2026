# M3 — Invariantes de Laço

**Objetivo:** Entender o que é um invariante de laço, como formular um e como usá-lo para
provar que um algoritmo de ordenação está correto — habilidade exigida na defesa oral (sprint-03).

---

## 1. O que é um invariante de laço?

Um **invariante de laço** é uma propriedade sobre o estado do programa que é verdadeira:

1. **Antes do laço começar** (inicialização)
2. **No início de cada iteração**, dado que era verdadeira no início da anterior (manutenção)
3. **Ao final do laço** (término) — e neste ponto implica que o algoritmo está correto

A estrutura lembra uma prova por indução matemática: o invariante é a hipótese, a inicialização
é o caso base, a manutenção é o passo indutivo.

---

## 2. Insertion Sort — invariante formal

Código de referência: `classical.py:58–84`.

**Invariante:** No início de cada iteração do `for i`, o subvetor `a[0..i-1]` contém os
mesmos elementos que estavam em `a[0..i-1]` originalmente, **em ordem crescente**.

### 2.1 Inicialização (i = 1)

`a[0..0]` tem apenas um elemento. Um vetor de um elemento está trivialmente ordenado. ✓

### 2.2 Manutenção (i → i+1)

Hipótese: `a[0..i-1]` está ordenado.

O laço interno (`while j >= 0`) desloca elementos de `a[0..i-1]` que são maiores que `key`
uma posição para a direita, e então insere `key` na posição correta. Ao final do `while`,
`a[0..i]` está ordenado.

Por que o while termina? `j` decrementa a cada iteração e tem limite inferior (`j >= 0`).
Além disso, `a[0] ≤ a[1] ≤ … ≤ a[j]` (hipótese indutiva) garante que encontramos a posição
correta ou chegamos ao início. ✓

### 2.3 Término (i = n)

Quando o `for` termina, `i = n`. O invariante diz que `a[0..n-1]` está ordenado.
Como `a[0..n-1]` é todo o vetor, o algoritmo está correto. ✓

---

## 3. Exemplo numérico passo a passo

Entrada: `[5, 2, 4, 6, 1, 3]`

| i | key | Estado de a[0..i-1] antes | Ação do while | a[0..i] após |
|---|-----|--------------------------|---------------|--------------|
| 1 | 2   | [5] — ordenado           | 5 > 2 → desloca 5; insere 2 em 0 | [2, 5] |
| 2 | 4   | [2, 5] — ordenado        | 5 > 4 → desloca; 2 ≤ 4 → para; insere 4 em 1 | [2, 4, 5] |
| 3 | 6   | [2, 4, 5] — ordenado     | 5 ≤ 6 → para imediatamente | [2, 4, 5, 6] |
| 4 | 1   | [2, 4, 5, 6] — ordenado  | 6,5,4,2 > 1 → desloca 4×; insere 1 em 0 | [1, 2, 4, 5, 6] |
| 5 | 3   | [1, 2, 4, 5, 6] — ordenado | 5,4 > 3 → desloca 2×; 2 ≤ 3 → para | [1, 2, 3, 4, 5, 6] |

**Invariante verificado em cada linha:** o subvetor sombreado `a[0..i-1]` está sempre ordenado
antes do `while` começar.

---

## 4. Casos de borda que o invariante deve cobrir

| Caso | O invariante aguenta? |
|------|-----------------------|
| N = 0 (vazio) | `for` não executa — `a[0..-1]` é vazio, trivialmente ordenado ✓ |
| N = 1 | `for` não executa (range(1,1) é vazio) — vetor de 1 elemento já está ordenado ✓ |
| Todos iguais | `while` para imediatamente em cada iteração — nenhuma troca, invariante mantido ✓ |

---

## 5. Como formular o invariante para o SEU autoral (sprint-03)

Perguntas-guia:

1. Qual parte do vetor está "resolvida" ao início de cada iteração?
2. Qual propriedade essa parte garante?
3. Como a iteração atual estende a parte resolvida sem quebrar a propriedade?
4. Quando o laço termina, a parte resolvida é todo o vetor?

Se você responder essas quatro perguntas precisamente, o invariante está completo.

---

## Conexão com o código

| O quê | Onde em `classical.py` |
|-------|------------------------|
| Laço externo (incrementa a parte resolvida) | linha 69 |
| Extração da chave | linha 70 |
| Laço interno (desloca elementos maiores) | linha 73–80 |
| Inserção na posição correta | linha 81 |

---

## Referências

- **CLRS Cap. 2.1** — "Insertion Sort" — invariante de laço formalizado com prova completa.
  Livro: Cormen et al., *Algoritmos: Teoria e Prática*, Campus, 2002, pp. 17–24.
- **CLRS Cap. 2.1, p. 19** — definição de inicialização, manutenção e término.
- **Sedgewick & Wayne, Cap. 2.1** — "Elementary Sorts" — análise de corretude dos sorts O(n²).
  Online: <https://algs4.cs.princeton.edu/21elementary/>
