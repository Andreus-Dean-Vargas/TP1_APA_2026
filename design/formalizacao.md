# Formalização — SCED (Seleção Convergente de Extremos Distintos)

> Artefato da **sprint-03**. Pseudocódigo + invariante de laço + exemplo numérico.
> Base conceitual: `conceito-autoral.md` (sprint-02). Decisões de design fechadas sem consulta
> prévia ao professor, por urgência de prazo (ver `duvidas-professor.md`, "Fechamento da sprint-02").

**Decisões de design adotadas nesta formalização:**
- **Atalho "já ordenado" mantido** — verificação O(n) prévia que, se o vetor já está em ordem
  não-decrescente, retorna direto (melhor caso Θ(n)). Tem argumento de corretude próprio,
  independente do núcleo (ver §4).
- **Contagem de movimentações:** 1 movimentação por elemento deslocado — uma troca (swap) entre
  duas posições conta **2** movimentações (convenção igual à de `classical.py`/`metrics.py`).
- **Estabilidade:** não é garantida (ver §5) — assumida como limitação documentada.

---

## 1. Pseudocódigo

```
CHECK-SORTED-AND-EXTREMES(A, n)
1  vmin ← vmax ← A[1]
2  sorted_asc ← TRUE
3  for k ← 2 to n
4      if A[k] < A[k-1]:  sorted_asc ← FALSE
5      if A[k] < vmin:    vmin ← A[k]
6      if A[k] > vmax:    vmax ← A[k]
7  return (sorted_asc, vmin, vmax)

PARTITION-CONVERGENT(A, low, high, vmin, vmax)
1  left ← low; i ← low; right ← high
2  mid_min ← NIL; mid_max ← NIL
3  while i ≤ right
4      if A[i] = vmin
5          if i ≠ left: troca A[i] ↔ A[left]
6          left ← left + 1; i ← i + 1
7      elif A[i] = vmax
8          if i ≠ right: troca A[i] ↔ A[right]
9          right ← right − 1              // i NÃO avança: valor trazido de "right" ainda não foi visto
10     else
11         if mid_min = NIL: mid_min ← mid_max ← A[i]
12         else:
13             if A[i] < mid_min: mid_min ← A[i]
14             if A[i] > mid_max: mid_max ← A[i]
15         i ← i + 1
16 return (left, right, mid_min, mid_max)

SCED-SORT(A, n)
1  if n ≤ 1: return A
2  (sorted_asc, vmin, vmax) ← CHECK-SORTED-AND-EXTREMES(A, n)
3  if sorted_asc: return A                 // melhor caso: atalho O(n)
4  low ← 1; high ← n; have_extremes ← TRUE
5  while low ≤ high
6      if not have_extremes
7          (vmin, vmax) ← varre A[low..high] achando mínimo e máximo
8      if vmin = vmax: break                // miolo restante é todo igual -> já ordenado por si
9      (low, high, mid_min, mid_max) ← PARTITION-CONVERGENT(A, low, high, vmin, vmax)
10     if low ≤ high and mid_min ≠ NIL
11         vmin ← mid_min; vmax ← mid_max; have_extremes ← TRUE
12     else
13         have_extremes ← FALSE
14 return A
```

---

## 2. Invariante de laço (núcleo — linhas 5–13 do `SCED-SORT`, sem o atalho)

**Enunciado do invariante**, válido no início de cada iteração do `while`:

> (I1) `A[1..low-1]` contém, em ordem não-decrescente, exatamente os `low-1` menores valores do
> array original (multiconjunto).
> (I2) `A[high+1..n]` contém, em ordem não-decrescente, exatamente os `n-high` maiores valores do
> array original.
> (I3) Todo elemento de `A[low..high]` é ≥ `A[low-1]` (se `low>1`) e ≤ `A[high+1]` (se `high<n`).
> (I4) `A[1..n]` é sempre uma **permutação** do array original (nenhum valor é criado/perdido —
> `PARTITION-CONVERGENT` só troca posições dentro de `[low..high]`).

- **Inicialização:** antes da 1ª iteração, `low=1, high=n`. `A[1..0]` e `A[n+1..n]` são intervalos
  vazios → (I1), (I2), (I3) valem trivialmente (vacuidade); (I4) vale pois `A[1..n]` é o próprio
  array original.

- **Manutenção:** suponha o invariante válido ao entrar na iteração, com `vmin`/`vmax` sendo o
  mínimo/máximo distintos de `A[low..high]`. `PARTITION-CONVERGENT` move **todas** as cópias de
  `vmin` para `A[low..left-1]` e **todas** as cópias de `vmax` para `A[right+1..high]`, deixando em
  `A[left..right]` apenas valores estritamente entre `vmin` e `vmax` (nem iguais a um nem a outro).
  - Como `vmin` é o mínimo de `A[low..high]` e, por (I3), `A[low..high] ≥ A[low-1]`, o novo prefixo
    `A[1..left-1] = A[1..low-1] ++ (cópias de vmin)` permanece não-decrescente e ≥ qualquer valor
    anterior — (I1) se estende para `low' = left`.
  - Simetricamente para `vmax` e o novo sufixo — (I2) se estende para `high' = right`.
  - Todo valor que permaneceu em `A[left..right]` satisfaz `vmin < valor < vmax`, e por (I3) antiga
    `vmin ≥ A[low-1]` e `vmax ≤ A[high+1]` → (I3) se mantém para a nova janela.
  - Nenhuma troca ocorre fora de `[low..high]` → (I4) preservado.

- **Término:** o laço para quando `low > high` (janela vazia — (I1)+(I2) já cobrem o array inteiro
  em ordem) **ou** quando `vmin = vmax` é detectado (todos os valores restantes em `A[low..high]`
  são iguais a um único valor `v` com `A[low-1] ≤ v ≤ A[high+1]`, por (I3) — um bloco constante é
  trivialmente ordenado). Em ambos os casos, (I1) + (miolo, se houver) + (I2) implica `A` ordenado;
  (I4) garante que é o mesmo multiconjunto do array original. **Corretude do núcleo provada.**

---

## 3. Exemplo numérico passo a passo

`A = [4, 1, 4, 2, 1, 3]` (n=6, não ordenado → atalho não dispara; vmin=1, vmax=4 da varredura inicial).

**Passada 1** — `low=1, high=6, vmin=1, vmax=4`:
`PARTITION-CONVERGENT` varre e troca: `[4,1,4,2,1,3]` → ... → `[1,1,3,2,4,4]`.
Resultado: `left=3, right=4` (meio ainda não resolvido = posições 3–4, valores `{3,2}`),
`mid_min=2, mid_max=3`. Novo `low=3, high=4, vmin=2, vmax=3`.
*Checagem do invariante:* `A[1..2]=[1,1]` ✓ ordenado e mínimo; `A[5..6]=[4,4]` ✓ ordenado e máximo.

**Passada 2** — `low=3, high=4, vmin=2, vmax=3`:
`PARTITION-CONVERGENT` sobre `A[3..4]=[3,2]` → troca para `[2,3]` → array completo
`[1,1,2,3,4,4]`. Resultado: `left=4, right=3` → `low=4 > high=3` → laço termina.

**Resultado final:** `A = [1,1,2,3,4,4]` = `sorted([4,1,4,2,1,3])`. ✓.

---

## 4. Corretude do atalho (independente do núcleo)

`CHECK-SORTED-AND-EXTREMES` testa `A[k] < A[k-1]` para todo `k=2..n`. Se nenhuma dessas comparações
for verdadeira, então `A[k] ≥ A[k-1]` para todo `k`, o que por transitividade implica
`A[1] ≤ A[2] ≤ ... ≤ A[n]` — a própria definição de ordenado. É um teste **direto** (não depende do
núcleo convergente), então sua corretude não herda nenhum risco do núcleo.

**Ressalva honesta (documentada desde a sprint-02):** quando o atalho dispara, o núcleo convergente
não é exercitado nesse cenário. Por isso o protótipo exploratório (`_grill_sced.py`, v2 — sem
atalho) foi usado para validar o núcleo isoladamente contra o cenário "ordenado".

---

## 5. Propriedades

- **Estável?** Não. Ao mover todas as cópias de `vmin`/`vmax` via troca (swap), a ordem relativa
  entre elementos de mesmo valor pode mudar. Contraexemplo mínimo: `A = [(2,a), (1,x), (2,b)]`
  (pares valor,rótulo) — `vmin=1` é trocado com a posição 1, mas isso não afeta a ordem de `(2,a)`
  e `(2,b)` neste caso trivial; em janelas maiores com múltiplas trocas em cadeia, a ordem relativa
  de cópias do mesmo valor não é preservada em geral (ex.: cópias de `vmax` tocadas por swaps
  sucessivos trocam de posição relativa entre si). **Limitação assumida e documentada**, não
  perseguida nesta entrega (perseguir estabilidade exigiria buffer auxiliar, custando o in-place).
- **In-place?** Sim — `O(1)` de memória auxiliar (só variáveis escalares: `low, high, vmin, vmax,
  left, right, mid_min, mid_max`), todas as movimentações são trocas dentro do próprio `A`.

---

## 6. Hipótese de complexidade (a confirmar na sprint-05)

Seja `d` = nº de valores distintos em `A[low..high]` a cada chamada de `PARTITION-CONVERGENT`.
Cada passada remove ≥2 valores distintos (vmin e vmax, exceto a última) em `O(janela)` comparações.
- **Melhor caso:** `Θ(n)` — atalho dispara (vetor já ordenado).
- **Pior caso:** `Θ(n·d) = Θ(n²)` quando `d = n` (todos distintos) e o atalho não dispara (ex:
  reverso).
- **Caso médio:** `Θ(n·d)`.
- **Espaço auxiliar:** `O(1)`.
