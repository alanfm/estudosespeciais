def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
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

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        # Mesclando as listas ordenadas
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1


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

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Encontra o índice do menor elemento não ordenado
        indice_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        # Troca o menor elemento com o primeiro não ordenado
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]


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


