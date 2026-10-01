"""
TEMPLATE PARA O ALUNO — TRABALHO PRÁTICO 1 (TP1)
Disciplina: Análise e Projetos de Algoritmos (APA)

Instruções:
1. Implemente seu método de ordenação autoral na função `my_authorial_sort`.
2. O retorno deve ser obrigatoriamente a tupla: (lista_ordenada, total_comparacoes, total_movimentacoes).
3. Execute este arquivo diretamente para rodar a suíte de testes de corretude e o benchmark rápido.
"""

from typing import Any, List, Tuple
import unittest


def _partition_convergent(a, low, high, vmin, vmax):
    """PARTITION-CONVERGENT: move todas as cópias de vmin para o início e de vmax
    para o fim de a[low..high], rastreando min/max do miolo que sobrar."""
    comps = 0
    moves = 0
    left, i, right = low, low, high
    mid_min = mid_max = None

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
                # i NÃO avança: o valor trazido de "right" ainda não foi visto
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

    return left, right, mid_min, mid_max, comps, moves


def my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """
    SCED — Seleção Convergente de Extremos Distintos.

    Em cada passada, acha o menor e o maior valor distinto ainda não posicionados
    e move todas as suas cópias para as duas extremidades da região não resolvida,
    convergindo de fora para dentro. Adaptação declarada do Bingo Sort (NIST DADS)
    com extensão bidirecional convergente — ver design/conceito-autoral.md e
    design/formalizacao.md (pseudocódigo + prova do invariante de laço).

    Parâmetros:
        arr (List[Any]): Lista de entrada a ser ordenada.

    Retorno:
        Tuple[List[Any], int, int]:
            - Lista ordenada
            - Total de comparações realizadas
            - Total de movimentações/trocas realizadas (1 por elemento deslocado)
    """
    a = list(arr)
    n = len(a)
    comps = 0
    moves = 0

    if n <= 1:
        return a, comps, moves

    # Atalho: verificação O(n) de "já ordenado" + extremos globais na mesma varredura.
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
        return a, comps, moves

    low, high = 0, n - 1
    have_extremes = True

    while low <= high:
        if not have_extremes:
            vmin = vmax = a[low]
            for k in range(low + 1, high + 1):
                comps += 1
                if a[k] < vmin:
                    vmin = a[k]
                comps += 1
                if a[k] > vmax:
                    vmax = a[k]

        if vmin == vmax:
            break

        left, right, mid_min, mid_max, c, m = _partition_convergent(a, low, high, vmin, vmax)
        comps += c
        moves += m
        low, high = left, right

        if low <= high and mid_min is not None:
            vmin, vmax = mid_min, mid_max
            have_extremes = True
        else:
            have_extremes = False

    return a, comps, moves


# =============================================================================
# SUÍTE DE TESTES AUTOMÁTICA DE VALIDAÇÃO
# =============================================================================
class TestStudentAuthorialSort(unittest.TestCase):
    def assert_sorted(self, original: List, result: List):
        self.assertEqual(len(result), len(original), "Tamanho divergente!")
        self.assertEqual(sorted(original), result, "A lista não foi ordenada corretamente!")

    def test_empty(self):
        res, _, _ = my_authorial_sort([])
        self.assert_sorted([], res)

    def test_single(self):
        res, _, _ = my_authorial_sort([99])
        self.assert_sorted([99], res)

    def test_sorted(self):
        data = list(range(100))
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_reverse(self):
        data = list(range(100, 0, -1))
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_identical(self):
        data = [5] * 50
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_random(self):
        import random
        random.seed(42)
        data = [random.randint(-1000, 1000) for _ in range(200)]
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)


if __name__ == "__main__":
    print("🧪 Executando testes unitários no seu algoritmo autoral...")
    unittest.main(verbosity=2)
