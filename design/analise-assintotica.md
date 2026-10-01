# Análise Assintótica — SCED

> Artefato da **sprint-05**. Dedução formal de complexidade de tempo (melhor/pior/médio) e espaço,
> validada contra o benchmark empírico (`benchmark.py`, `benchmark_results.png`).

## 1. Modelo de custo

Seja `n = |A|` e `d` = número de valores **distintos** em `A[low..high]` no início de cada passada
de `PARTITION-CONVERGENT`. O atalho `CHECK-SORTED-AND-EXTREMES` custa sempre `Θ(n)` (uma varredura,
3 comparações por posição — ver pseudocódigo em `formalizacao.md`).

Cada passada do núcleo convergente custa `Θ(w)`, onde `w` é o tamanho da janela `[low..high]`
naquela passada, e remove pelo menos os valores `vmin` e `vmax` do conjunto de distintos restantes
(ou encerra, se `vmin = vmax`). Logo o número de passadas é `⌈d/2⌉` no pior caso de redução (uma
passada remove exatamente os dois extremos; pode remover mais se o "miolo" ficar vazio antes).

## 2. Melhor caso — Θ(n)

Quando o vetor de entrada já está em ordem não-decrescente, o atalho dispara na primeira varredura
e retorna sem executar nenhuma passada do núcleo: **3n − 3 comparações, 0 movimentações**.
Confirmado empiricamente: `n=1000` → `comps=2997 = 3·999`. **Θ(n)**, independente de `d`.

## 3. Pior caso — Θ(n·d) = Θ(n²) quando d = n

No pior caso, cada passada remove exatamente 2 valores distintos (quando os extremos não têm
muitas cópias e o miolo nunca esvazia antes), totalizando `d/2` passadas, cada uma custando
`Θ(w_i)` onde `w_i` é a janela da i-ésima passada. No piso, `Σ w_i ≤ n · (d/2)` (cada passada
revisita até `n` posições) — formalmente, como cada passada varre a janela corrente completa e as
janelas encolhem monotonicamente, `Σ w_i = Θ(n·d)` no caso em que a maioria dos elementos só é
"vista" pela primeira vez na sua própria passada de remoção (caso de poucas repetições por
passada, típico quando `d` é grande).

Quando **todos os elementos são distintos** (`d = n`), isso se reduz a `Θ(n²)` — confirmado
empiricamente (`reverso`, `n=1000`: `comps=1.001.499 ≈ n² + n`; `n=5000`: `comps≈24.97M ≈ n²`).
O vetor **estritamente decrescente** é o pior caso real observado: o atalho nunca dispara (o
vetor nunca está ordenado ascendente) e `d=n`.

## 4. Caso médio — Θ(n·d)

Para uma entrada aleatória uniforme, `d` tende a ser próximo de `n` (poucas colisões se o domínio
de valores for grande), reduzindo ao mesmo regime do pior caso: `Θ(n²)`. Quando o domínio de
valores é pequeno (muita repetição, `d = O(1)`), o custo cai para `Θ(n·d) = Θ(n)` — confirmado:
`n=5000`, `d=5` → `comps=37.003 ≈ n·d·1,5` (overhead de ≈1,5× por passada vem das comparações de
rastreio do "miolo" `mid_min`/`mid_max`, que ocorrem para cada elemento que não é `vmin` nem `vmax`).

**Esta é a assinatura distintiva do SCED**: a complexidade não depende do *intervalo* de valores
(como Counting Sort) nem é *sempre* quadrática (como Selection Sort) — depende do número de
**valores distintos**, uma propriedade que nenhum dos clássicos comparados explora diretamente.

## 5. Espaço auxiliar — O(1)

Todas as variáveis de `SCED-SORT` e `PARTITION-CONVERGENT` são escalares (`low, high, vmin, vmax,
left, right, mid_min, mid_max`); não há estrutura auxiliar proporcional a `n`. **In-place.**

## 6. Validação empírica (benchmark.py, trials=3, ver `benchmark_results.png`)

| Cenário | n | d | Comparações SCED | n·d (referência) |
|---|---|---|---|---|
| aleatório amplo | 1000 | 1000 | 1.001.499 | 1.000.000 |
| reverso | 1000 | 1000 | 1.001.499 | 1.000.000 |
| poucos distintos (d=5) | 1000 | 5 | 7.395 | 5.000 |
| já ordenado | 1000 | 1000 | 2.997 | — (Θ(n), não Θ(n·d)) |
| aleatório amplo | 5000 | 4992 | 24.969.356 | 24.960.000 |
| reverso | 5000 | 5000 | 25.007.499 | 25.000.000 |

A curva empírica de comparações cresce com `n·d` conforme previsto — divergência máxima observada
de ~1,5× (overhead constante do rastreio de `mid_min`/`mid_max`), não de ordem de grandeza.
Nos gráficos de `benchmark_results.png`: SCED tem a **melhor** curva de tempo no cenário `sorted`
(atalho) e no cenário `duplicates` (d pequeno), e a **pior** curva (equivalente a Insertion/
Selection, pior que Merge/Quick) nos cenários `random` e `reverse` — exatamente o padrão previsto
pela dependência em `d`, não em `n` isoladamente.

## 7. Comparação com a literatura (CLRS Cap. 2, 6–8)

| Método | Melhor | Pior | Médio | Espaço | Estável | In-place |
|---|---|---|---|---|---|---|
| **SCED (autoral)** | **Θ(n)** | Θ(n·d)=Θ(n²) | Θ(n·d) | O(1) | Não | Sim |
| Insertion Sort | Θ(n) | Θ(n²) | Θ(n²) | O(1) | Sim | Sim |
| Selection Sort | Θ(n²) | Θ(n²) | Θ(n²) | O(1) | Não | Sim |
| Merge Sort | Θ(n log n) | Θ(n log n) | Θ(n log n) | O(n) | Sim | Não |
| Quick Sort | Θ(n log n) | Θ(n²) | Θ(n log n) | O(log n) | Não | Sim |

**Diferencial do SCED frente aos clássicos:** nenhum dos quatro tem seu custo diretamente em
função de `d` (nº de distintos) — Insertion/Selection são sempre O(n²) no pior caso independente
de repetições; Merge/Quick são O(n log n) independente de `d`. O SCED troca essa garantia
assintótica fixa por uma sensibilidade a `d`: imbatível quando há poucos valores distintos ou a
entrada já está ordenada, mas pior que os O(n log n) quando os valores são majoritariamente
distintos — trade-off coerente com o enunciado ("performance bruta não é o foco"; o que importa é
a justificativa teórica do trade-off, não vencer o Quick Sort).
