def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        elemento_atual = arr[i]
        j = i - 1

        while j >= 0 and elemento_atual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = elemento_atual

def executar_insertion_sort(numero_repeticoes, vetor, tipo_instancia):
    soma_tempos = 0
    soma_consumos_memoria = 0
    media_tempos = 0
    media_consumos_memoria = 0
    tempos_insertion_sort = []
    consumos_memoria_insertion_sort = []

    for i in range(numero_repeticoes):
        tempo_inicial = 0
        tempo_final = 0
        memoria_inicial = 0
        memoria_final = 0

        memoria_inicial = sys.getsizeof(vetor)
        tempo_inicial = time.time()
        insertion_sort(vetor.copy())
        tempo_final = time.time()
        memoria_final = sys.getsizeof(vetor)

        tempos_insertion_sort.append((tempo_final - tempo_inicial) * 1000)  # Em milissegundos
        consumos_memoria_insertion_sort.append(memoria_final - memoria_inicial)

    soma_tempos = sum(tempos_insertion_sort)
    media_tempos = soma_tempos / numero_repeticoes

    soma_consumos_memoria = sum(consumos_memoria_insertion_sort)
    media_consumos_memoria = soma_consumos_memoria / numero_repeticoes

    print(f"""
        Algoritmo: Insertion Sort
        Tipo da Instância/Tamanho: {tipo_instancia}/{len(vetor)}
        Qtd. de Iterações: {numero_repeticoes}
        Média de Tempo Gasto: {media_tempos:.6f} ms
        Média de Consumo de Memória: {media_consumos_memoria:.4f} bytes
    """)
