def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        elemento_atual = arr[i]
        j = i - 1

        while j >= 0 and elemento_atual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = elemento_atual




def merge(left, right):
    vetor = []

    while left and right:
        if left[0] < right[0]:
            vetor.append(left.pop(0))
        else:
            vetor.append(right.pop(0))

    return vetor + left + right

def merge_sort(vetor):
    if len(vetor) < 2:
        return vetor

    meio = len(vetor) // 2
    left = vetor[:meio]
    right = vetor[meio:]

    return merge(merge_sort(left), merge_sort(right))


def quick_sort(vetor):
    tamanho_vetor = len(vetor)

    if tamanho_vetor <= 1:
        return vetor

    pivo = vetor[-1]
    left = []
    right = []

    for i in range(tamanho_vetor - 1):
        if vetor[i] < pivo:
            left.append(vetor[i])
        else:
            right.append(vetor[i])

    return quick_sort(left) + [pivo] + quick_sort(right)

def selection_sort(vetor):
    tamanho_vetor = len(vetor)

    for i in range(tamanho_vetor - 1):
        menor_valor_indice = i

        for j in range(i, tamanho_vetor):
            if vetor[j] < vetor[menor_valor_indice]:
                menor_valor_indice = j

        if vetor[i] > vetor[menor_valor_indice]:
            vetor[i], vetor[menor_valor_indice] = vetor[menor_valor_indice], vetor[i]


# Implementação do heap-sort

def heapify(vetor, tamanho_vetor, indice_raiz):
    maior = indice_raiz
    indice_esquerda = 2 * indice_raiz + 1
    indice_direita = 2 * indice_raiz + 2

    if indice_esquerda < tamanho_vetor and vetor[indice_esquerda] > vetor[maior]:
        maior = indice_esquerda

    if indice_direita < tamanho_vetor and vetor[indice_direita] > vetor[maior]:
        maior = indice_direita

    if maior != indice_raiz:
        vetor[indice_raiz], vetor[maior] = vetor[maior], vetor[indice_raiz]
        heapify(vetor, tamanho_vetor, maior)


def heap_sort(vetor):
    tamanho_vetor = len(vetor)

    for i in range(tamanho_vetor, -1, -1):
        heapify(vetor, tamanho_vetor, i)

    for i in range(tamanho_vetor - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapify(vetor, i, 0)



def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return pivot_index, arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)
    return low, arr[low]


