"""
PROTÓTIPO EXPLORATÓRIO (sprint-02) — NÃO é a implementação oficial (essa vai para
student_template.py na sprint-04, com TDD). Objetivo: "grelhar" o conceito SCED,
achar falhas e gerar dados empíricos para embasar melhorias.

Convenção de contagem (igual a classical.py / metrics.py):
  - comparação de dois elementos  -> comps += 1
  - troca (swap)                   -> moves += 2
"""
import os
import random
import sys

# importar os clássicos para comparar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "TP1-Codigos-e-Benchmarks", "python"))
from classical import selection_sort, quick_sort, merge_sort  # noqa: E402


# --------------------------------------------------------------------------- #
# SCED v1 — "ingênuo": varre p/ achar min/max, depois 2 varreduras de coleta
# --------------------------------------------------------------------------- #
def sced_v1(arr):
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a, 0, 0
    comps = 0
    moves = 0
    lo, hi = 0, n - 1
    passes = 0

    while lo <= hi:
        passes += 1
        vmin = vmax = a[lo]
        for k in range(lo + 1, hi + 1):
            comps += 1
            if a[k] < vmin:
                vmin = a[k]
            comps += 1
            if a[k] > vmax:
                vmax = a[k]
        comps += 1
        if vmin == vmax:  # região toda igual -> encerra
            break
        # coleta todas as cópias de vmin na frente
        store = lo
        for i in range(lo, hi + 1):
            comps += 1
            if a[i] == vmin:
                if i != store:
                    a[i], a[store] = a[store], a[i]
                    moves += 2
                store += 1
        lo = store
        # coleta todas as cópias de vmax no fim
        store = hi
        for i in range(hi, lo - 1, -1):
            comps += 1
            if a[i] == vmax:
                if i != store:
                    a[i], a[store] = a[store], a[i]
                    moves += 2
                store -= 1
        hi = store

    return a, comps, moves, passes


# --------------------------------------------------------------------------- #
# SCED v2 — "esperto": acha min/max e faz UMA passada de partição tri-partite
# (==vmin p/ esquerda, ==vmax p/ direita, resto no meio) estilo Dutch flag
# --------------------------------------------------------------------------- #
def sced_v2(arr):
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a, 0, 0
    comps = 0
    moves = 0
    lo, hi = 0, n - 1
    passes = 0

    while lo <= hi:
        passes += 1
        vmin = vmax = a[lo]
        for k in range(lo + 1, hi + 1):
            comps += 1
            if a[k] < vmin:
                vmin = a[k]
            comps += 1
            if a[k] > vmax:
                vmax = a[k]
        comps += 1
        if vmin == vmax:
            break
        # partição em uma passada: left = fronteira dos vmin, right = fronteira dos vmax
        left = lo
        i = lo
        right = hi
        while i <= right:
            comps += 1
            if a[i] == vmin:
                if i != left:
                    a[i], a[left] = a[left], a[i]
                    moves += 2
                left += 1
                i += 1
            else:
                comps += 1
                if a[i] == vmax:
                    if i != right:
                        a[i], a[right] = a[right], a[i]
                        moves += 2
                    right -= 1
                    # não avança i: o elemento trazido de right ainda não foi visto
                else:
                    i += 1
        lo = left
        hi = right

    return a, comps, moves, passes


# --------------------------------------------------------------------------- #
# SCED v3 — v2 + melhoria A (fim de jogo antecipado p/ já-ordenado)
#                + melhoria B (min/max do miolo calculado na própria partição)
# --------------------------------------------------------------------------- #
def sced_v3(arr):
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a, 0, 0, 0
    comps = 0
    moves = 0
    passes = 0

    # (A) passada única inicial: acha min/max global E detecta já-ordenado
    vmin = vmax = a[0]
    sorted_asc = True
    for k in range(1, n):
        comps += 1
        if a[k] < a[k - 1]:
            sorted_asc = False
        comps += 1
        if a[k] < vmin:
            vmin = a[k]
        comps += 1
        if a[k] > vmax:
            vmax = a[k]
    if sorted_asc:
        return a, comps, moves, 1  # já ordenado -> O(n)

    lo, hi = 0, n - 1
    have_minmax = True  # vmin/vmax de [lo..hi] já conhecidos (da passada inicial ou de B)

    while lo <= hi:
        passes += 1
        if not have_minmax:
            vmin = vmax = a[lo]
            for k in range(lo + 1, hi + 1):
                comps += 1
                if a[k] < vmin:
                    vmin = a[k]
                comps += 1
                if a[k] > vmax:
                    vmax = a[k]
        comps += 1
        if vmin == vmax:
            break

        # partição tri-partite (v2) + (B) rastreio de min/max do miolo
        left = lo
        i = lo
        right = hi
        mid_min = None
        mid_max = None
        while i <= right:
            comps += 1
            if a[i] == vmin:
                if i != left:
                    a[i], a[left] = a[left], a[i]
                    moves += 2
                left += 1
                i += 1
            else:
                comps += 1
                if a[i] == vmax:
                    if i != right:
                        a[i], a[right] = a[right], a[i]
                        moves += 2
                    right -= 1
                else:
                    if mid_min is None:
                        mid_min = mid_max = a[i]
                    else:
                        comps += 1
                        if a[i] < mid_min:
                            mid_min = a[i]
                        comps += 1
                        if a[i] > mid_max:
                            mid_max = a[i]
                    i += 1
        lo = left
        hi = right
        if lo <= hi and mid_min is not None:
            vmin, vmax = mid_min, mid_max
            have_minmax = True
        else:
            have_minmax = False

    return a, comps, moves, passes


# --------------------------------------------------------------------------- #
# ÁRVORE — BST com contador por nó (a ideia "cada valor distinto é um nível").
# Insere tudo (duplicados incrementam contador) e emite in-order.
# Convenção: 1 comparação (3-vias) por nó visitado na inserção;
#            1 movimentação por elemento escrito de volta no vetor.
#            memória auxiliar = nº de nós = d (valores distintos).
# --------------------------------------------------------------------------- #
class _Node:
    __slots__ = ("val", "count", "left", "right")

    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None


def tree_sort_counts(arr):
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a, 0, 0, 0  # comps, moves, nós
    comps = 0
    moves = 0
    nodes = 1
    root = _Node(a[0])
    for idx in range(1, n):
        x = a[idx]
        cur = root
        while True:
            comps += 1  # 1 comparação de 3 vias por nó
            if x == cur.val:
                cur.count += 1
                break
            elif x < cur.val:
                if cur.left is None:
                    cur.left = _Node(x)
                    nodes += 1
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = _Node(x)
                    nodes += 1
                    break
                cur = cur.right

    out = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        for _ in range(cur.count):
            out.append(cur.val)
            moves += 1
        cur = cur.right
    return out, comps, moves, nodes


# --------------------------------------------------------------------------- #
# Geradores de cenários
# --------------------------------------------------------------------------- #
def gen(kind, n, seed=42):
    rnd = random.Random(seed)
    if kind == "aleatorio_amplo":      # quase todos distintos
        return [rnd.randint(-10**6, 10**6) for _ in range(n)]
    if kind == "aleatorio_estreito":   # muitas repetições (range pequeno)
        return [rnd.randint(0, 9) for _ in range(n)]
    if kind == "poucos_distintos":     # d = 5 fixo
        return [rnd.choice([1, 7, 13, 42, 99]) for _ in range(n)]
    if kind == "todos_iguais":
        return [5] * n
    if kind == "ordenado":
        return list(range(n))
    if kind == "reverso":
        return list(range(n, 0, -1))
    if kind == "floats":
        return [rnd.uniform(-1000, 1000) for _ in range(n)]
    if kind == "com_negativos":
        return [rnd.randint(-500, 500) for _ in range(n)]
    raise ValueError(kind)


SCENARIOS = [
    "aleatorio_amplo", "aleatorio_estreito", "poucos_distintos",
    "todos_iguais", "ordenado", "reverso", "floats", "com_negativos",
]


def is_ok(res, original):
    return res == sorted(original)


def main():
    n = 500
    print(f"n = {n}  (comparacoes; d = valores distintos)\n")
    header = (f"{'cenario':<20}{'d':>5}  {'v2 comp':>10}{'v3 comp':>10}"
              f"{'v3 vs v2':>10}{'selec':>10}{'quick':>10}")
    print(header)
    print("-" * len(header))
    for kind in SCENARIOS:
        base = gen(kind, n)
        d = len(set(base))

        r1, c1, m1, p1 = sced_v1(base)
        r2, c2, m2, p2 = sced_v2(base)
        r3, c3, m3, p3 = sced_v3(base)
        rs, cs, ms = selection_sort(base)
        rq, cq, mq = quick_sort(base)

        ok = all([is_ok(r1, base), is_ok(r2, base), is_ok(r3, base),
                  is_ok(rs, base), is_ok(rq, base)])
        delta = f"{(c3 / c2 - 1) * 100:+.0f}%" if c2 else "-"
        flag = "" if ok else "  <-- ERRO DE ORDENACAO!"
        print(f"{kind:<20}{d:>5}  {c2:>10}{c3:>10}{delta:>10}{cs:>10}{cq:>10}{flag}")

    print("\nPassadas (v2 vs v3) — foco nas falhas 1 e 3:")
    print(f"{'cenario':<20}{'v2 pass':>9}{'v3 pass':>9}{'v3 moves':>10}")
    print("-" * 48)
    for kind in SCENARIOS:
        base = gen(kind, n)
        _, _, _, p2 = sced_v2(base)
        _, _, m3, p3 = sced_v3(base)
        print(f"{kind:<20}{p2:>9}{p3:>9}{m3:>10}")

    print("\nEscala no pior caso (aleatorio_amplo, ~todos distintos):")
    print(f"{'n':>6}{'v2 comp':>12}{'v3 comp':>12}{'selec':>12}{'quick':>12}")
    for nn in (100, 200, 400, 800):
        base = gen("aleatorio_amplo", nn)
        _, c2, _, _ = sced_v2(base)
        _, c3, _, _ = sced_v3(base)
        _, cs, _ = selection_sort(base)
        _, cq, _ = quick_sort(base)
        print(f"{nn:>6}{c2:>12}{c3:>12}{cs:>12}{cq:>12}")

    # ------------------------------------------------------------------- #
    # SCED (in-place) vs ÁRVORE (BST c/ contador) — o duelo do fork
    # ------------------------------------------------------------------- #
    import math
    print("\n=== SCED v3 (in-place, O(1)) vs ARVORE BST (O(d) memoria) ===")
    hdr = (f"{'cenario':<20}{'d':>5}{'SCED comp':>11}{'ARV comp':>10}"
           f"{'ARV bal~':>10}{'ARV mem':>9}{'SCED mem':>9}")
    print(hdr)
    print("-" * len(hdr))
    for kind in SCENARIOS:
        base = gen(kind, n)
        d = len(set(base))
        r3, c3, m3, p3 = sced_v3(base)
        rt, ct, mt, nodes = tree_sort_counts(base)
        # referencia teorica de uma arvore BALANCEADA: ~ n * log2(d)
        bal = int(n * math.log2(d)) if d > 1 else n
        ok = is_ok(r3, base) and is_ok(rt, base)
        flag = "" if ok else "  <-- ERRO!"
        print(f"{kind:<20}{d:>5}{c3:>11}{ct:>10}{bal:>10}{nodes:>9}{'O(1)':>9}{flag}")
    print("\nLeitura: 'ARV comp' = BST desbalanceada real; 'ARV bal~' = referencia")
    print("teorica de arvore balanceada (~n*log2 d). 'ARV mem' = nos = d (aux).")


if __name__ == "__main__":
    main()
