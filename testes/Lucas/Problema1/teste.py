import sorting_algos as sorting
import random

def calcular_pivot(lista_a, lista_b):
    soma_a = sum(lista_a)
    soma_b = sum(lista_b)
    return (lista_a[0] + soma_a) / (lista_b[0] + soma_b)

def particionar(lista, inicio, fim, pivot):
    i = inicio
    j = fim

    while True:
        while lista[i] < pivot and i < len(lista):
            i = i + 1
        while lista[j] > pivot and j >= 0:
            j = j - 1

        if i >= j:
            return j

        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1

def quick_sort_com_pivot(lista_a, lista_b):
    if len(lista_a) <= 1:
        return lista_a

    pivot = round(calcular_pivot(lista_a, lista_b))
    indice_pivo = particionar(lista_a, 0, len(lista_a) - 1, pivot)

    lista_a_esquerda = lista_a[:indice_pivo+1]
    lista_a_direita = lista_a[indice_pivo+1:]

    lista_b_esquerda = lista_b[:indice_pivo+1]
    lista_b_direita = lista_b[indice_pivo+1:]

    return quick_sort_com_pivot(lista_a_esquerda, lista_b_esquerda) + quick_sort_com_pivot(lista_a_direita, lista_b_direita)

# Exemplo de uso
lista_a = [4, 5, 2, 8]
lista_b = [7, 3, 6, 9]

resultado = quick_sort_com_pivot(lista_a, lista_b)
print(resultado)