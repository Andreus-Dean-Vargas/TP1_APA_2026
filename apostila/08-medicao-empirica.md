# M8 — Medição Empírica

**Objetivo:** Entender a infraestrutura de medição do pacote (metrics.py, benchmark.py) e
interpretar os números reais extraídos da suíte — para validar a análise teórica do autoral.

---

## 1. Infraestrutura de medição

### `metrics.py` — o que instrumenta

| Classe/Função | O que faz | Arquivo:linha |
|---------------|-----------|---------------|
| `SortMetrics` | Dataclass com algorithm_name, input_size, distribution, elapsed_time_sec, comparisons, swaps_or_moves, is_sorted | `metrics.py:12` |
| `InstrumentedList` | Wrapper de lista: `__setitem__` incrementa `moves`; `compare()` incrementa `comparisons` | `metrics.py:23` |
| `InstrumentedList.swap(i,j)` | Troca contabilizando exatamente 2 moves | `metrics.py:63` |
| `measure_sort()` | Executa sort_fn, mede tempo com `time.perf_counter()`, retorna (data_sorted, SortMetrics) | `metrics.py:73` |

Os algoritmos em `classical.py` **não usam** `InstrumentedList` — contam comps/moves
internamente com variáveis explícitas. O `InstrumentedList` está disponível para quem quiser
usá-lo no autoral.

### `benchmark.py` — o que mede

- `generate_dataset(n, distribution)` — gera entrada com 5 distribuições (`random`, `sorted`,
  `reverse`, `duplicates`, `almost_sorted`) — `benchmark.py:27`
- `run_benchmark()` — para cada algoritmo × tamanho × distribuição × trial, mede tempo_ms,
  comparações e movimentações médias — `benchmark.py:49`
- `print_markdown_summary()` — imprime tabela Markdown — `benchmark.py:100`

**Comando para rodar:**

```bash
cd TP1-Codigos-e-Benchmarks/python
python benchmark.py --trials 3 --plot benchmark_results.png
```

---

## 2. Dados reais — extraídos com seed=42, 2 trials

Formato: `comparações / movimentações` para cada (N, distribuição).

### RANDOM

| Algoritmo | N=10 | N=50 | N=100 | N=500 | N=1000 |
|-----------|------|------|-------|-------|--------|
| Bubble Sort | 44/59 | 1194/1235 | 4931/5153 | 124359/124116 | — |
| Selection Sort | 45/14 | 1225/91 | 4950/195 | 124750/984 | — |
| Insertion Sort | 35/47 | 664/715 | 2671/2774 | 62550/63056 | 247804/248809 |
| Merge Sort | 22/34 | 222/286 | 543/672 | 3853/4488 | 8688/9976 |
| Quick Sort | 55/23 | 412/155 | 996/365 | 6505/2403 | 13711/5351 |
| DPES (ref) | 35/47 | 401/269 | 1024/624 | 8013/3733 | 18122/8528 |

### SORTED

| Algoritmo | N=100 | N=1000 |
|-----------|-------|--------|
| Bubble Sort | 99 / 0 | 999 / 0 |
| Selection Sort | 4950 / 0 | 499500 / 0 |
| Insertion Sort | 99 / 198 | 999 / 1998 |
| Merge Sort | 316 / 672 | 4932 / 9976 |
| Quick Sort | 795 / 0 | 10542 / 0 |
| DPES (ref) | 751 / 182 | 14191 / 1838 |

### REVERSE (pior caso para a maioria)

| Algoritmo | N=100 | N=1000 |
|-----------|-------|--------|
| Bubble Sort | 4950 / 9900 | — |
| Selection Sort | 4950 / 100 | — |
| Insertion Sort | 4950 / 5148 | 499500 / 501498 |
| Merge Sort | 356 / 672 | 5044 / 9976 |
| Quick Sort | 799 / 104 | 10549 / 1004 |
| DPES (ref) | 886 / 336 | 15218 / 2892 |

### ALMOST_SORTED (onde Insertion Sort brilha)

| Algoritmo | N=100 | N=1000 |
|-----------|-------|--------|
| Insertion Sort | 361 / 461 | 32408 / 33407 |
| Merge Sort | 426 / 672 | 7602 / 9976 |
| Quick Sort | 863 / 67 | 10881 / 351 |
| DPES (ref) | 766 / 206 | 15822 / 5200 |

---

## 3. Como interpretar os dados

### Comparações vs. teoria

| Algoritmo | Teórico (random, pior) | Empírico N=100 random | Coerente? |
|-----------|----------------------|-----------------------|-----------|
| Insertion Sort | n(n-1)/2 = 4950 | 2671 | ✓ (caso médio ≈ n²/4) |
| Selection Sort | n(n-1)/2 = 4950 | 4950 | ✓ (sempre exatamente n(n-1)/2) |
| Merge Sort | ~n log n ≈ 665 | 543 | ✓ |
| Quick Sort | ~1.39 n log n ≈ 925 | 996 | ✓ |

Selection Sort confirma a análise: sempre exatamente n(n-1)/2 comparações, independente
da distribuição. Isso é visível na tabela (4950 em random, sorted e reverse).

### Movimentações — o que revelam

- Bubble Sort em vetor sorted: **0 movimentações** — flag `swapped` funciona.
- Merge Sort: movimentações **constantes por distribuição** (sempre ≈ n·⌈log₂ n⌉).
  Isso ocorre porque o merge sempre percorre todo o vetor combinado.
- Quick Sort random: poucas movimentações — trocas de elementos distantes são eficientes.

---

## 4. Como adicionar seu autoral ao benchmark

Em `benchmark.py`, o dicionário `algorithms` (linha 161) lista os algoritmos:

```python
algorithms = {
    "Bubble Sort": bubble_sort,
    # ...
    "Authorial (DPES)": dpes_sort,   # ← substituir pelo seu após sprint-04
}
```

Após implementar `my_authorial_sort` em `student_template.py`, importe e adicione:

```python
from student_template import my_authorial_sort
algorithms["Meu Autoral"] = my_authorial_sort
```

---

## 5. O que o gráfico deve mostrar (sprint-05)

Para validar a análise teórica, o gráfico de comparações × N deve mostrar:
- Algoritmos O(n²) → curva parabólica
- Algoritmos O(n log n) → curva subquadrática
- Seu autoral deve se encaixar na curva esperada pela teoria

Se a curva empírica não bater com a teoria, investigue a instrumentação antes de aceitar
a divergência (regra do SPEC).

---

## Referências

- **CLRS Cap. 2.2** — "Analysing algorithms" — base da análise de custo que valida o benchmark.
- **Sedgewick & Wayne, Cap. 1.4** — "Analysis of Algorithms" — doubling hypothesis e análise empírica.
  Online: <https://algs4.cs.princeton.edu/14analysis/>
- Código: `metrics.py`, `benchmark.py`, `classical.py` — todos em `TP1-Codigos-e-Benchmarks/python/`.
