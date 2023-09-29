
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

def executar_merge_sort(numero_repeticoes, vetor, tipo_instancia):
    soma_tempos = 0
    soma_consumos_memoria = 0
    media_tempos = 0
    media_consumos_memoria = 0
    tempos_merge_sort = []
    consumos_memoria_merge_sort = []

    for i in range(numero_repeticoes):
        tempo_inicial = 0
        tempo_final = 0
        memoria_inicial = 0
        memoria_final = 0

        memoria_inicial = sys.getsizeof(vetor)
        tempo_inicial = time.time()
        merge_sort(vetor.copy())
        tempo_final = time.time()
        memoria_final = sys.getsizeof(vetor)

        tempos_merge_sort.append((tempo_final - tempo_inicial) * 1000)  # Em milissegundos
        consumos_memoria_merge_sort.append(memoria_final - memoria_inicial)

    soma_tempos = sum(tempos_merge_sort)
    media_tempos = soma_tempos / numero_repeticoes

    soma_consumos_memoria = sum(consumos_memoria_merge_sort)
    media_consumos_memoria = soma_consumos_memoria / numero_repeticoes

    # Log de saída
    print(f"""
        Algoritmo: Merge Sort
        Tipo da Instância/Tamanho: {tipo_instancia}/{len(vetor)}
        Qtd. de Iterações: {numero_repeticoes}
        Média de Tempo Gasto: {media_tempos:.6f} ms
        Média de Consumo de Memória: {media_consumos_memoria:.4f} bytes
    """)
