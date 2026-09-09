# M2 — Notação Assintótica: O, Ω, Θ, o, ω

**Objetivo:** Dominar a linguagem formal de complexidade usada em análise de algoritmos —
definições precisas, como provar, e como aplicar a cada sort do pacote.

---

## 1. Por que notação assintótica?

T(n) exato depende do hardware, compilador e constantes. A notação assintótica captura o
**comportamento de crescimento** descartando constantes e termos de baixa ordem — que não importam
para n grande.

---

## 2. Definições formais (CLRS Cap. 3)

### O-grande — limite superior assintótico

```
f(n) = O(g(n))  ⟺  ∃ c > 0, n₀ > 0 : ∀ n ≥ n₀,  f(n) ≤ c·g(n)
```

Leitura: "f cresce **no máximo** tão rápido quanto g".

**Exemplo:** 2n² + 3n + 1 = O(n²)
Prova: para c = 6 e n₀ = 1: 2n² + 3n + 1 ≤ 2n² + 3n² + n² = 6n² para n ≥ 1. ✓

### Ω-grande — limite inferior assintótico

```
f(n) = Ω(g(n))  ⟺  ∃ c > 0, n₀ > 0 : ∀ n ≥ n₀,  f(n) ≥ c·g(n)
```

Leitura: "f cresce **pelo menos** tão rápido quanto g".

**Exemplo:** 2n² + 3n + 1 = Ω(n²)
Prova: para c = 2 e n₀ = 1: 2n² + 3n + 1 ≥ 2n². ✓

### Θ (theta) — limite exato

```
f(n) = Θ(g(n))  ⟺  f(n) = O(g(n))  E  f(n) = Ω(g(n))
```

Equivalente: ∃ c₁, c₂ > 0, n₀ : ∀ n ≥ n₀,  c₁·g(n) ≤ f(n) ≤ c₂·g(n).

**Exemplo:** 2n² + 3n + 1 = Θ(n²). Prova: usa os dois acima.

### o-pequeno e ω-pequeno — limites estritos

```
f(n) = o(g(n))  ⟺  lim_{n→∞} f(n)/g(n) = 0     (f cresce estritamente mais devagar)
f(n) = ω(g(n))  ⟺  lim_{n→∞} f(n)/g(n) = +∞    (f cresce estritamente mais rápido)
```

**Exemplos:**
- n = o(n²)   porque n/n² = 1/n → 0.
- n² = ω(n)   porque n²/n = n → ∞.

---

## 3. Hierarquia de crescimento (da mais lenta à mais rápida)

```
Θ(1)  <  Θ(log n)  <  Θ(√n)  <  Θ(n)  <  Θ(n log n)  <  Θ(n²)  <  Θ(n³)  <  Θ(2ⁿ)
```

Para n = 1.000:

| Função | Valor |
|--------|-------|
| log₂ n | ≈ 10 |
| n      | 1.000 |
| n log n| ≈ 10.000 |
| n²     | 1.000.000 |
| 2ⁿ     | > 10³⁰⁰ |

---

## 4. Como aplicar ao TP1

| Algoritmo | Melhor | Pior | Médio | Espaço |
|-----------|--------|------|-------|--------|
| Insertion Sort | O(n) | O(n²) | Θ(n²) | O(1) |
| Merge Sort | Θ(n log n) | Θ(n log n) | Θ(n log n) | O(n) |

Para o **seu autoral**:
- Pior caso: qual estrutura de entrada força mais comparações? → expressão O(…).
- Melhor caso: entrada mais favorável? → expressão Ω(…).
- Caso médio: costuma ser o mais difícil — use benchmark empírico para corroborar.

---

## 5. Erros comuns a evitar

| Erro | Correção |
|------|----------|
| Dizer "complexidade O(n²)" sem especificar se é pior, melhor ou médio | Sempre especificar o caso |
| Usar O quando deveria ser Θ (limite exato) | O diz "no máximo" — use Θ quando os dois lados são conhecidos |
| Esquecer espaço auxiliar na análise | É cobrado! Mencionar in-place vs O(n) |

---

## 6. Exemplo numérico — provando que n log n = O(n²)

Afirmação: n log₂ n = O(n²).

Prova: para n ≥ 1, log₂ n ≤ n (propriedade básica do logaritmo).
Portanto n log₂ n ≤ n · n = n².
Tome c = 1, n₀ = 1. ∎

---

## Referências

- **CLRS Cap. 3** — "Growth of Functions" — todas as definições e provas deste módulo.
  Livro: Cormen et al., *Algoritmos: Teoria e Prática*, Campus, 2002, pp. 47–65.
- **Sedgewick & Wayne, Cap. 1.4** — "Analysis of Algorithms" — análise empírica e assintótica lado a lado.
  Online: <https://algs4.cs.princeton.edu/14analysis/>
- **Ziviani, Cap. 2.2** — "Comportamento assintótico de funções" — terminologia PT-BR equivalente.
