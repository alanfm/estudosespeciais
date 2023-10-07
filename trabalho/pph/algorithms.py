from sorting import *

def calc_R_conjunto(S, a0, b0):
    soma_a_t = sum(x[0] for x in S)
    soma_b_t = sum(x[1] for x in S)
    return (a0 + soma_a_t) / (b0 + soma_b_t)

def calcular_R(S, a, b, a0, b0):
    soma_a_t = sum(a[t] for t in S)
    soma_b_t = sum(b[t] for t in S)
    return (a0 + soma_a_t) / (b0 + soma_b_t)

# Teste:
"""O primeiro algoritmo inicia com R = a0/b0 e testa repetidamente se existe
algum par (ak, bk) que satisfaz as condições do lema. No caso afirmativo,
inclui o par no conjunto S, atualiza o valor de R e repete o teste. Observe que
se existir um elemento em S que não satisfaz às condições do lema, este
elemento deve ser removido. Este primeiro algoritmo deve executar em
O(n^2 )."""

def remove_valor_zerob(a,b):
    # Quando encontrar um valor 0 em b, remove o par (a,b) da lista
    i = 0
    while(i < len(b)):
        if b[i] == 0:
            a.pop(i)
            b.pop(i)
        i += 1



def q1(a, b):
    # remove_valor_zerob(a,b)
    R = a[0] / b[0]
    S = []
    for k in range(1, len(a)):
        if a[k] / b[k] > R:
            S.append((a[k], b[k]))
            R = calc_R_conjunto(S, a[0], b[0])
            i = 0
            while(i < len(S)):
                if S[i][0]/S[i][1] < R:
                    S.pop(i)
                    R = calc_R_conjunto(S, a[0], b[0])
                i += 1
    return S

# Q2 - a
def q2_bubble(a,b):
    R = a[0] / b[0]
    S = []
    pairs = [( a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]
    bubble_sort(pairs)
    i = 0
    for pair in reversed(pairs):
        ratio, ak, bk = pair
        if ratio > R:
            S.append((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break

    return S

def q2_insertion(a,b):
    R = a[0] / b[0]
    S = []
    pairs = [( a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]
    insertion_sort(pairs)
    i = 0
    for pair in reversed(pairs):
        ratio, ak, bk = pair
        if ratio > R:
            S.append((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break

    return S

def q2_selection(a,b):
    R = a[0] / b[0]
    S = []
    pairs = [( a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]
    selection_sort(pairs)
    i = 0
    for pair in reversed(pairs):
        ratio, ak, bk = pair
        if ratio > R:
            S.append((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break

    return S

def q2_heapsort(a, b):
    R = a[0] / b[0]
    S = []

    # Função para ajustar um nó em um heap máximo
    def heapify(pairs, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and pairs[left][0] > pairs[largest][0]:
            largest = left

        if right < n and pairs[right][0] > pairs[largest][0]:
            largest = right

        if largest != i:
            pairs[i], pairs[largest] = pairs[largest], pairs[i]
            heapify(pairs, n, largest)

    pairs = [(a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]

    n = len(pairs)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(pairs, n, i)

    i = 0
    while pairs:
        ratio, ak, bk = pairs[0]
        if ratio > R:
            S.append((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break
        pairs[0] = pairs.pop()
        heapify(pairs, len(pairs), 0)

    return S

def q2_mergesort(a,b):
    R = a[0] / b[0]
    S = []
    pairs = [( a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]
    pairs = merge_sort(pairs)
    i = 0
    for pair in reversed(pairs):
        ratio, ak, bk = pair
        if ratio > R:
            S.append((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break

    return S

def q2_quicksort(a,b):
    R = a[0] / b[0]
    S = []
    pairs = [( a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]
    pairs = quick_sort(pairs)
    i = 0
    for pair in reversed(pairs):
        ratio, ak, bk = pair
        if ratio > R:
            S.append((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break

    return S

# Algoritmo O(n)
def q3_quickselect(a,b):
    R = a[0] / b[0]
    S = set()
    pairs = [( a[i] / b[i], a[i], b[i]) for i in range(1, len(a))]

    # Eu vou o quickselect para pegar o maior elemento de pairs e adicionar no conjunto S
    # quando o elemento for adicionado, eu removo ele de pairs. Se o maior elemento for menor que R atual, eu paro;
    # caso contrário, eu continuo até que pairs esteja vazio.
    while pairs:
        ind, maior = quickselect(pairs, 0, len(pairs) - 1, 0)
        ratio, ak, bk = pairs.pop(ind)
        if ratio > R:
            S.add((ak, bk))
            R = calc_R_conjunto(S, a[0], b[0])
        else:
            break

    return S